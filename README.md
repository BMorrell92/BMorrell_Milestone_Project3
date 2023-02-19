![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# LogIt (Meditation Website) 

## Milestone Project 3 - Backend Development 


* LogIt is a general purpose note storage website. Users are able to create, save and edit their notes. This is a responsive website to allow for use with any device   

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
* As a user, I would like my notes to be stored and reaccessed on demand.
* As a user, I would like to delete my notes. 
* As a user, I would like my notes to be secure. 

## Website Structure and Features

### Wireframes

[View my wireframes in PDF format here.](https://github.com/BMorrell92/Milestone_Project_2/blob/main/assets/wireframes/MS2%20Wireframe.pdf) It should be noted, that the wireframes do not exactly match the final product, however, it does capture the main structure.

### Typograhpy

All text is in Fuzzy Bubbles. This font is visually appealing and playful. Since the website has minimal text, it is the chosen font throughout.

### Website Architecture

The website consists of one simple page which intergrates all the interactive features. There are three sections where the user can provide input to achieve the desired output; the Time Selection, Play/Pause and Sound Selection sections. The content on the landing page has been styled using [Bootrap Jumbotron Components](https://getbootstrap.com/docs/4.0/components/jumbotron/) to fill as much space as possible. 

- Time Selection:
<p align="center"><img src="https://github.com/BMorrell92/Milestone_Project_2/blob/main/assets/images/Time%20Section.JPG"></p>

- Play/Pause Section:
<p align="center"><img src="https://github.com/BMorrell92/Milestone_Project_2/blob/main/assets/images/Play%20Section%201.JPG"></p>
<p align="center"><img src="https://github.com/BMorrell92/Milestone_Project_2/blob/main/assets/images/Play%20Section%202.JPG"></p>
<p align="center"><img src="https://github.com/BMorrell92/Milestone_Project_2/blob/main/assets/images/Play%20Section%203.JPG"></p> 

- Sound Selection:
<p align="center"><img src="https://github.com/BMorrell92/Milestone_Project_2/blob/main/assets/images/Sound%20Section.JPG"></p>

### Current Features

- **Responsive Design:**

  - By designing with a Mobile First philosophy the website can be viewed on any device, adjusting the layout according to the device.  
  - Visulize grid systems have been used to acheive the responsive design.

 - **Interactive Features:**

    - Time Selection: The user sets the timer by selecting a time.
    - Play/Pause Button: The user can play or pause the timer which also controls the audio.
    - Sound Selection: The user can select a sound which will also set a background GIF specific to the selected sound.

### Future Features

- A time input function that allows the user to input a precise time.
- Addition of high quality background videos, as opposed to GIF's.
- A larger selection of sounds.

## Technologies and Libaries Used
1. [HTML5](https://www.w3.org/TR/html52/)
2. [CSS3](https://www.w3.org/Style/CSS/Overview.en.html)
3. [Javascript](https://www.javascript.com/)
4. [Bootstrap framework for structuring](http://getbootstrap.com/)
5. [Github for Repo creation and managment](https://github.com/)
6. [Gitpod for file creation and code editing](https://gitpod.io/)
7. [Figma was used to create Wireframes for the project](https://www.figma.com/)
8. [Google Chrome's Dev Tools were used while building the project to test responsiveness, functionality and for debugging](https://developer.chrome.com/docs/devtools/)
9. [The icons used were taken from Font Awesome](https://fontawesome.com/)

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

- Timer Function:

  - All four time inputs have been tested and proven to work.  
  - Play/Pause button has been tested and proven to work.
  - Timer duration animation has been observed to work in sync with all times.


- Audio and Background Wallpaper:

  - All four audio selections have been tested and proven to work.  
  - Background wallpaper changes as intended when specific sound is selected.
  - Audio sucessfully loops through for the whole duration.

### Challenging User Stories 

- *"As a user, I would like to have control over the amount of time I wish to hear ambient sounds."* - **The user has a selection of four different times**
- *"As a user, I would like to be able to play and pause the ambient sounds as and when required."* - **The user can play or pause the sounds using the play/pause button**
- *"As a user, I would like to choose from a selection of ambient sounds."* - **The user has a selection of four different ambient sounds**
- *"As a user, I would like to see a background image/video of the selected ambient sound for added effect."* - **The background wallpaper changes with each selected sound to match the theme**

### User Feedback

I asked a small group of friends and colleagues to test the website. I implemented some changes following feedback, but some changes were added to the "Future Features" section. The Feedback was as follows:

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

I would like to credit Code Institute for providing easy-to-follow content and all the necessary source code from their tutorials.  

### Content 

- The icons used were taken from [Font Awesome](https://fontawesome.com/)
- The JS code was developed using this [Youtube tutorial](https://www.youtube.com/watch?v=oMBXdZzYqEk) and various other sources.

### Media

- The GIFs used for the background wallpaper were taken from open source website https://giphy.com/explore/open-source
- The sound used for the website was sourced from a free sound effect website https://www.zapsplat.com/

