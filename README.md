
# LogIt (Online Notebook) 

## Milestone Project 3 - Backend Development 


* LogIt is a web application that allows users to create, read, update, and delete notes with ease. This is a responsive website to allow for use with any device   

* This is my Milestone Project 3 submission for Code Institute's Diploma in Web Application Development course. My website features one page and is built using technologies that I have learnt including HTML, CSS and JavaScript. My website uses non-relational databases, features full CRUD functionality and is built using technologies that I have learnt including HTML, CSS, JavaScript, Python and Flask.


<h2><img src=></h2>

## Live Project 

[View the live project here.](https://bmorrell92.github.io/)

## Repository

[Find the project repository here](https://github.com/BMorrell92/)

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
  + [Unresolved](#Unresolved)
- [Credits](#credits)
  + [Content](#content)
  + [Media](#media)


## User Stories

The audience of this website will be those who would like a secure location to create, store and access their notes:

* As a user, I would like to create and categorise my notes. 
* As a user, I would like to access my notes on demand.
* As a user, I would like to update my notes.
* As a user, I would like my notes to be secure. 

## Website Structure and Features

### Wireframes

[View my wireframes in PDF format here.](https://github.com/BMorrell92/BMorrell_Milestone_Project3/blob/main/assets/wireframes/MS3Wireframes.pdf) It should be noted, that the wireframes do not exactly match the final product, however, it does capture the main structure.

### Typograhpy

The text uses Fuzzy Bubbles whilst the title uses FreeHand. These fonts are visually appealing, playful and perpetuate a hand-written effect, which is in keeping with the theme of the website.

### Website Architecture

The website consists of 6 pages. Each page has its own function for users to register, log in and access their notes. All pages were structured using the [Materialize Framework](https://materializecss.com/about.html). 

- Home Page:
<p align="center"><img src="https://github.com/BMorrell92/Milestone_Project_2/blob/main/assets/images/Time%20Section.JPG"></p>

- Log In Page:
<p align="center"><img src=""></p>

- Registration Page:
<p align="center"><img src=""></p>

- Profile Page:
<p align="center"><img src=""></p>

- New Notes Page:
<p align="center"><img src=""></p>

- Edit Notes Page:
<p align="center"><img src=""></p>


### Current Features

- **Responsive Design:**

  - By designing with a Mobile First philosophy the website can be viewed on any device, adjusting the layout according to the device.  
  - Materilize grid systems have been used to acheive the responsive design.

- **Account Log In/Registration:**

    - Time Selection: The user sets the timer by selecting a time.
    - Play/Pause Button: The user can play or pause the timer which also controls the audio.
    - Sound Selection: The user can select a sound which will also set a background GIF specific to the selected sound.

- **Note Managment:**

    - Time Selection: The user sets the timer by selecting a time.
    - Play/Pause Button: The user can play or pause the timer which also controls the audio.
    - Sound Selection: The user can select a sound which will also set a background GIF specific to the selected sound.

### Future Features

- Automatic Date.

## Database

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
  - index.html: 0 errors were returned when passing through the official W3C validator
  <p align="center"><img src="https://github.com/BMorrell92/Milestone_Project_2/blob/main/assets/images/HTML%20Validator.jpg"></p>

  
- **CSS:**
  - No errors were found when passing through the official W3C validator 
 <p align="center"><img src="https://github.com/BMorrell92/Milestone_Project_2/blob/main/assets/images/CSS%20Validator.JPG"></p>


- **Javascript:**
    - No errors were found when passing through the JSHint Validator or Chrome Developer Tool
 <p align="center"><img src="https://github.com/BMorrell92/Milestone_Project_2/blob/main/assets/images/JS%20Validator.JPG"></p>
 <p align="center"><img src="https://github.com/BMorrell92/Milestone_Project_2/blob/main/assets/images/JS%20Chrome.jpg"></p>


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

- The following registration & login functionalities were tested and confirmed to be working:

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

I asked a small group of friends and colleagues to test the application. I implemented some changes following feedback, but some changes were added to the "Future Features" section. The Feedback was as follows:

- *"It would be nice to have a box to input a specific time rather than having to select from defined options."* - **Future Feature**
- *"The grainy background GIFs give the site a nice aesthetic, but it would look more professional with some high quality videos in the background"* - **Future Feature**
- *"Is it possible to incorporate a timer bar?"* - **Implemented into project**
- *"A wider selection of sounds would be cool"* - **Future Feature**


## Bugs

### Resolved
- **HTML Validation:**
    - When I first validated my game page HTML, the validator came back with an error; “Attribute ‘type' not allowed on element label at this point”. To solve the issue I ommitted the type attribute from all label elements as they were not needed.

- **Background Wallpaper not Resetting from "Dawn" Sound:**
    - When I was first manually testing the website for all it's interactive features, I noticed that the background wallpaper was sticking on the "Dawn" audio, and the website need to be refreshed to restore functionality. I solved this bug by adjusting the reset and set audio & background functions in the JS code. 

### Unresolved
- **Rendering Speed:**
  - It has been noticed that rendering issues occur with poor internet speeds, which can occasionally affect the user experience. On this occassion, all media content is being hosted within the source code, however, any future improvments will have to utilise CDN's to improve the rendering time of the website.

## Credits 

I would like to credit Code Institute for providing easy-to-follow content and all the necessary source code from their tutorials. Much of the source code from the CodeInstitutes Task Manager mini project has been repurposed for this project.   

### Content 

- The icons used were taken from [Font Awesome](https://fontawesome.com/)



