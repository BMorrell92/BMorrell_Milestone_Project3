import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/get_notes")
def get_notes():
    notes = list(mongo.db.notes.find())
    return render_template("notes.html", notes=notes)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    notes = list(mongo.db.notes.find({"$text": {"$search": query}}))
    return render_template("notes.html", notes=notes)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_note", methods=["GET", "POST"])
def add_note():
    if request.method == "POST":
        high_importance = "on" if request.form.get("high_importance") else "off"
        note = {
            "category_name": request.form.get("category_name"),
            "note_name": request.form.get("note_name"),
            "note_description": request.form.get("note_description"),
            "high_importance": high_importance,
            "note_date": request.form.get("note_date"),
            "created_by": session["user"]
        }
        mongo.db.notes.insert_one(note)
        flash("Note Successfully Added")
        return redirect(url_for("get_notes"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_note.html", categories=categories)


@app.route("/edit_note/<note_id>", methods=["GET", "POST"])
def edit_note(note_id):
    if request.method == "POST":
        high_importance = "on" if request.form.get("high_importance") else "off"
        submit = {
            "category_name": request.form.get("category_name"),
            "note_name": request.form.get("note_name"),
            "note_description": request.form.get("note_description"),
            "high_importance": high_importance,
            "note_date": request.form.get("note_date"),
            "created_by": session["user"]
        }
        mongo.db.notes._update_retryable({"_id": ObjectId(note_id)}, submit)
        flash("Task Successfully Updated")

    note = mongo.db.notes.find_one({"_id": ObjectId(note_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_note.html", note=note, categories=categories)


@app.route("/delete_note/<note_id>")
def delete_note(note_id):
    mongo.db.notes.delete_one({"_id": ObjectId(note_id)})
    flash("Note Successfully Deleted")
    return redirect(url_for("get_notes"))


@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update_one({"_id": ObjectId(category_id)}, submit)
        flash("Category Successfully Updated")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.delete_one({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("get_categories"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
    