
# LogIt (Online Notebook) 

## Milestone Project 3 - Backend Development 


* LogIt is a web application that allows users to create, read, update, and delete notes with ease. This is a responsive website to allow for use with any device   

* This is my Milestone Project 3 submission for Code Institute's Diploma in Web Application Development course. My website features one page and is built using technologies that I have learnt including HTML, CSS and JavaScript. My website uses non-relational databases, features full CRUD functionality and is built using technologies that I have learnt including HTML, CSS, JavaScript, Python and Flask.


## Live Project 

[View the live project here.](https://notes-ben-ms3.herokuapp.com/)

## Repository

[Find the project repository here](https://github.com/BMorrell92/BMorrell_Milestone_Project3)

# Table of Contents  

## Contents
- [User Stories](#user-stories)
- [Website Structure and Features](#Website-Structure-and-Features)
  + [Wireframes](#wireframes)
  + [Typography](#typography)
  + [Website Architecture](#website-architecture)
  + [Current Feautures](#current-features)
  + [Future Feautures](#future-features)
- [Technologies and Libaries Used](#Technologies-and-Libaries-Used)
- [Testing](#testing)
  + [Validator Testing](#validtor-testing)
  + [Browser Compatability](#browser-compatability)
  + [Device Compatability](#device-compatability)
  + [Manual Testing](#manual-testing)
  + [Challenging User Stories](#Challenging-User-Stories)
  + [User Feedback](#User-Feedback)
- [Bugs](#bugs)
  + [Resolved](#resolved)
- [Credits](#credits)
  + [Content](#content)
  + [Media](#media)


## User Stories

The audience of this website will be those who would like a secure location to create, read, update and delete their notes:

* As a user, I would like to create and categorise my notes. 
* As a user, I would like to access my notes on demand.
* As a user, I would like to update my notes.
* As a user, I would like to delete my notes.
* As a user, I would like my notes to be secure. 

## Website Structure and Features

### Wireframes

[View my wireframes in PDF format here.](https://github.com/BMorrell92/BMorrell_Milestone_Project3/blob/main/assets/wireframes/MS3Wireframes.pdf) It should be noted, that the wireframes do not exactly match the final product, however, it does capture the main structure.

### Typograhpy

The text uses Fuzzy Bubbles whilst the title uses FreeHand. These fonts are visually appealing, playful and perpetuate a hand-written effect, which is in keeping with the theme of the website.

### Website Structure & Features

The website consists of 6 pages. Each page has its own function for users to register, log in and access their notes. Page structuring and functionality was structured using the [Materialize Framework](https://materializecss.com/about.html). 

- Home Page:
When first visiting the website, users are greeted with a homepage which introduces the purpose of LogIt:
<p align="center"><img src="https://github.com/BMorrell92/BMorrell_Milestone_Project3/blob/main/assets/images/home.JPG"></p>

- Log In Page:
From the Log In page returning users can enter their credentials into the form to access their profile:
<p align="center"><img src="https://github.com/BMorrell92/BMorrell_Milestone_Project3/blob/main/assets/images/log%20in.JPG"></p>

- Registration Page:
From the Registration page new users can enter their desired credentials into the form to create a profile:
<p align="center"><img src="https://github.com/BMorrell92/BMorrell_Milestone_Project3/blob/main/assets/images/register.JPG"></p>

- Profile Page:
From the the Profile/Notes page users can access, search and delete their notes:
<p align="center"><img src="https://github.com/BMorrell92/BMorrell_Milestone_Project3/blob/main/assets/images/profile.JPG"></p>

- New Notes Page:
From the New Notes page users can add new notes to thier profile by filling in the new notes form:
<p align="center"><img src="https://github.com/BMorrell92/BMorrell_Milestone_Project3/blob/main/assets/images/new.JPG"></p>

- Edit Notes Page:
From the Edit Notes page users can add new notes to thier profile by filling in the new notes form.
<p align="center"><img src="https://github.com/BMorrell92/BMorrell_Milestone_Project3/blob/main/assets/images/edit.JPG"></p>

## Technologies and Libaries Used
1. [HTML5](https://www.w3.org/TR/html52/)
2. [CSS3](https://www.w3.org/Style/CSS/Overview.en.html)
3. [Javascript](https://www.javascript.com/)
4. [Materialize framework for structuring](http://getbootstrap.com/)
5. [Github for Repo creation and managment](https://github.com/)
6. [Gitpod for file creation and code editing](https://gitpod.io/)
7. [Figma was used to create Wireframes for the project](https://www.figma.com/)
8. [Google Chrome's Dev Tools were used while building the project to test responsiveness, functionality and for debugging](https://developer.chrome.com/docs/devtools/)
9. [The icons used were taken from Font Awesome](https://fontawesome.com/)
10. [MongoDB to create and manage the database](https://mongodb.com)
11. [Heroku to deploy the application](https://www.heroku.com/) 

## Testing 

### Validator Testing 

- **HTML:**
  - No errors were returned when passing through the official W3C validator:
  <p align="center"><img src="https://github.com/BMorrell92/BMorrell_Milestone_Project3/blob/main/assets/images/HTML%20Validator.JPG"></p>

  
- **CSS:**
  - No errors were found when passing through the official W3C validator: 
 <p align="center"><img src="https://github.com/BMorrell92/BMorrell_Milestone_Project3/blob/main/assets/images/CSS%20Validator.JPG"></p>


- **Javascript:**
    - No errors were found when passing through the JSHint Validator:
 <p align="center"><img src="https://github.com/BMorrell92/BMorrell_Milestone_Project3/blob/main/assets/images/JS%20Validator.JPG"></p>
 
 - **Python:**
    - No errors were found when passing through the Python Tester
 <p align="center"><img src="https://github.com/BMorrell92/BMorrell_Milestone_Project3/blob/main/assets/images/Python%20Validator.JPG"></p>


### Browser Compatability
The website has been tested on the following browsers:

- Chrome
- Edge/IE
- Firefox
- Opera
- Safari

The wesbite and all it's functionalities work as intended on all broswers. 

### Device Compatability
By using Google Chrome's Dev Tool, compatability was checked on the following devices:

- IPhone SE
- IPhone XR
- IPhone 12 Pro
- Pixel 5
- Samsung Galaxy S8+
- Samsung Galaxy Ultra S20 Ultra
- Surface Pro 7
- IPad
- IPad Pro

 The website was found to be responsive on all devices.

### Manual Testing 

- User authentication was tested and confirmed to be working. The following elements were tested:

  - Successful registration.  
  - Failed registration if username exists.
  - Successful Login.
  - Unsuccesful login if username does not exist.
  - Unsuccesful login if password incorrect.


- The following notes managment functionalities were tested and confirmed to be working:

  - Notes are saved and retreived to profile page.  
  - Notes can be created, updated and deleted.
  
### Challenging User Stories 

- *"As a user, I would like to create and categorise my notes."* - **The user can add notes to their account and assign a selection of four categories to those notes**
- *"As a user, I would like to access my notes on demand."* - **The user can access their notes at any time by logging into their account**
- *"As a user, I would like to update my notes."* - **The user can edit or delete their notes**
- *"As a user, I would like my notes to be secure."* - **The users notes are secured in their own account**

### User Feedback

I asked a small group of friends and colleagues to test the application. Any criticisms will be considiered for future developments. The Feedback was as follows:

- *"Easy to use and good for simple notes. However, it's a bit too simple if you want to start getting a bit more complex with your notes"*
- *"Slightly 90's looking, but it does a good job, and I might even start using it myself!"* 
- *"Good work! Only thing i'd suggest is a custom field for the categories."* 


## Bugs

### Resolved
- **HTML Validation:**
    - When I first passed the website through the html validator it was returning the following errors:
    <p align="center"><img src="https://github.com/BMorrell92/BMorrell_Milestone_Project3/blob/main/assets/images/HTML%20Error.JPG"></p>
    To fix this I deleted the divs that were nesting the li elements.

- **App Methods:**
  - Whilst following the Code Institute Task Manager mini project I noticed some of the methods they were using were not working in my case. Specifically, the delete funtion used the "remove" method to delete an item from the database on the tutorial, but the "delete_one" method worked for me. Furthermore, the edit funtion used the "update" method to update items on the database on the tutorial, but the "update_retryable" worked for me. 

## Credits 

I would like to credit Code Institute for providing easy-to-follow content and all the necessary source code from their tutorials. Much of the source code from the Code Institutes Task Manager mini project has been repurposed for the benefit of this deliverable.   

### Content 

- The icons used were taken from [Font Awesome](https://fontawesome.com/)



