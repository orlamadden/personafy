# Personafy

## Project Overview

Personafy is an online tool for creating custom user personas in minutes. Users have the ability to search for pre-built templates, or sign up to create their own personas based on their own personal / business needs.

Using CRUD functionality, users can (C)reate, (R)ead, (U)pdate and (D)elete users personas using Personafy.

## Table of Contents

1. [**UX**](#UX)
    - [**Project Goals**](#project-goals)
    - [**User Stories**](#user-stories)
    - [**Wireframes**](#wireframes)
    - [**Design Choices**](#design-choices)
2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Recommendations for future implementation**](#recommendations-for-future-implementation)
3. [**Technology**](#technology)
    - [**Technologies used**](#frontend-technologies-used)
    - [**Other**](#other)
4. [**Testing**](#testing)
    - [**Validators used**](#validators-used)
    - [**Manual Tests**](#manual-tests)
    - [**Bugs found**](#bugs-found)
    - [**User Story Testing**](#user-story-testing)
5. [**Deployment**](#deployment)
    - [**Publishing to GitHub Pages**](#publishing-to-github-pages)
    - [**Deployment to Heroku**](#deployment-to-heroku)
6. [**Credits**](#credits)
    - [**Code**](#code)
    - [**Content**](#content)
    - [**Media**](#media)
    - [**Acknowledgements**](#acknowledgements)

---

## UX

### Project purpose

The goal of this project is to showcase user personas for developers, designers or marketeers who are in the process of creating and/or updating websites. The users who access to website will be able to view pre-built user personas in a particular industry or role, or create their own specific user personas for their own business needs.

### User Stories

- As a user I want to view the site from any device (mobile, tablet and desktop).
- As a user I want to view pre-made personas for inspiration.
- As a user, I want to be able to print a persona so I can bring it to my team meeting.
- As a user, I want to read about user personas and best practice, tips and tricks for using a user persona in my projects.

- As a user-contributor, I want to be able to create my own profile.
- As a user-contributor, I want to be able to create my own personas.
- As a user-contributor, I want to be able to keep my personas private because I am using them for my team at my company workplace.
- As a user-contributor, I want to be able to edit/modify an existing persona.
- As a user-contributor, I want to be able to delete an existing persona.
- As a user-contributor, I want to have a confirmation/warning before deleting an entry.
- As a user-contributor, I want to be able to log out of my account.

### Wireframes

I used Balsamiq to complete my wireframes as part of the design and planning process for this project. I usually use Adobe Illustrator to create my wireframes, but I enjoyed learning Balsamiq and using its pre-built components. I made minor changes throughout the development stage of the project, so my website looks slightly different than the wireframes based on user feedback as part of my development iteration process. The core concept is of the website is still there.

I opted to not create wireframes for tablet as in this case the tablet view is mirrored in mobile view. The business case for this website is that Personafy would be used by designers, developers and marketeers, so desktop view took priority as it is invisioned that it would be used in an office setting.

**Home page**

- [Desktop](https://res.cloudinary.com/orla2020/image/upload/v1595017199/milestone-three/desktop-home_dzrzo7.png)
- [Mobile](https://res.cloudinary.com/orla2020/image/upload/v1595017199/milestone-three/mobile-home_rbyjei.png)

**Public personas listings page**

*Note - My Personas listings page is the same as public listings page

- [Desktop](https://res.cloudinary.com/orla2020/image/upload/v1595017199/milestone-three/desktop-list-view-public-personas_wb4szx.png)
- [Mobile](https://res.cloudinary.com/orla2020/image/upload/v1595017199/milestone-three/mobile-public-persona_bkibtv.png)

**Add persona page**

*Note - Edit persona page is the same as add persona page

- [Desktop](https://res.cloudinary.com/orla2020/image/upload/v1595017199/milestone-three/desktop-add-persona_snmykf.png)
- [Mobile](https://res.cloudinary.com/orla2020/image/upload/v1595017199/milestone-three/mobile-add-persona_p1iga0.png)

**View persona page**

- [Desktop](https://res.cloudinary.com/orla2020/image/upload/v1595017199/milestone-three/desktop-view-entry_df96fy.png)
- [Mobile](https://res.cloudinary.com/orla2020/image/upload/v1595017199/milestone-three/mobile-view-persona_rqioxf.png)

### Design Choices

#### Font

Roboto from Google Fonts was the font choice for this project. I opted for Roboto due to legibility on all devices and it's professional look. It's simple,easy for users to read and has a vast selection of font weights and font styles that can be implemented if necessary.

#### Colours

For this project, I kept design and color to a minimum so users could focus on the core functionality of the website. The primary colours of the website is blue, white and light grey. The colour blue tends to be used for websites that are trusthworthy and want to give the impression of a professional look and feel, that's why I chose blue. The light colours of white and grey help the blue to stand out more when it is used.

![https://res.cloudinary.com/orla2020/image/upload/v1595092085/milestone-three/MS3-color-palette_j1zjz4.png](https://res.cloudinary.com/orla2020/image/upload/v1595092085/milestone-three/MS3-color-palette_j1zjz4.png)

## Features

### Existing Features

#### Navbar

- The navbar contains the main navigation of the website. The brand logo always redirects back to the home page. The navigation links contents change depending on whether the user is logged in as registered user or not.

1. Registered user view of navbar:
- Home
- Public Personas
- Learning
- Add Persona
- My Persona
- Username
- Logout

2. Non-registered user view of navbar:
- Home
- Public Personas
- Learning
- Login
- Register

#### Register

- Visitors to the website can sign up to the website and have an account. Users need to fill out a basic form which requires entering a username and password. Username and password are stored in the users collection in the database.

#### Log in

- If users register to the website, they have the ability to log in using the same simple form containing their username and password. This gives registered users the possibility to add personas, edit them and delete them.

#### Log out

- Users can log out from their session on the website by pressing the 'logout' button in the navbar.

#### Add a user persona

- When users are logged in, they can create or 'add' a user persona using a form. Details required for the user persona are 'name', 'age', 'bio', 'occupation', 'industry', 'goals' and 'frustrations'. Using an image with the user persona is optional, a randomly generated image will be used in this case.

#### View user personas

- Read or 'view' user personas, either from the public personas page, or the my perosnas page when the user is logged in. Users can also view an individual user persona. From there, users can print personas, or if a user is logged in, they can also edit their own persona from this screen.

#### Edit a user persona

- Logged in users can edit or modify their user personas and update the database with the user personas updated information. The edit form is similar to the 'create' user persona form.

#### Delete a user persona

- Logged in users can delete any user persona that they have made. Before a user persona is deleted, a pop up modal displays asking the user if they are sure they want to delete it.

#### Persona card

- A persona card displays on the Public Personas page and My Personas page when a user creates a user persona. The user persona card contains an image (submitted by the user or a placeholder image), the user persona name, their industry, their occupation and their age.

#### Make personas public or private

- Registered users have the ability to keep personas private and not for public viewing. This is a required user story as the user may be using the user persona for a business project.

### Recommended features for future implementation

#### Exanded user persona Details

- I would like to add more information about the user persona for a more narrow scope, such as demographics and tasks that are usually performed throughout a praticular webite/mobile application process.

#### Search functionality

- In the future, I would like to add the ability for users to search for user personas based on industry or occupation. This would give users more control over what they can find on the site.

#### Add new occupation and industry

- Give users the ability to create new job titles and industries and submit them to the database. This will give users more options when creating user personas.

#### Content submission

- I would like to add a form where users can submit useful videos, articles and other resources that might be useful for creating user personas. The submission would be reviewed by an admin (me) before published.

#### Admin dashboard

- When a user is signed in, I would like to create a personalised dashboard for them, containing add/edit/delete user persona functionality in one place, how many user personas they have created and join date.

## Technologies Used

The languages, frameworks and other tools used for this project:

- HTML - page structure and content
- CSS - custom styling
- JQuery - for print functionality
- Python3 - backend processing and application logic
- Bootstrap framework - used as the core structuring layout for the application which ensures mobile-first design
- Git - used for version control
- Github - used for remote version control storage
- Flask framework - template language written in Python, contains Jinja2 and Werkzeug
- Heroku - used to host the app
- MongoDB Atlas - used to store the project's database information

## Information Architecture

This project utilises the NoSQL database MongoDB to store data. The reason for this is it is recommended to use this type of database for the Milestone 3 project. 

### Database Schema

This project's database contains 4 main collections to store data.
- Personas - stores data about user personas created by registered users (example)
- Industry - stores data about industries
- Occupation - stores data about occupations
- Users - stores username and hashed passwords from registered users (example)

### Data Storage Types

The types of data stored in MongoDB for this project are:

- ObjectId
- String
- Array
- Boolean

### Database Collections Structure

## Testing

Automatic testing was not conducted due to time constraints and a knowledge gap.

### Manual Testing

To ensure the best user experience, I performed multiple manual tests to ensure the app worked across various devices and on multiple browsers.

### Validators used

[W3C HTML Validator](https://validator.w3.org/)

- 7 errors found, 1 warning.
   - **_Element li not allowed as child of element div in this context. (Suppressing further errors from this subtree.)_** - this error was found 5 times on the home page. The ```<li>``` tags in the footer were not contained within a ```<ul>``` or ```<ol>``` tag. This was fixed.
   - **_End tag br_** - incorrect syntax for the ```<br>``` tag, this was fixed.
   - **_Duplicate ID delete-modal_** - there was an id duplication on the pop up modal, this was fixed.

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)

- No errors.

### Bugs Found

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

#### Solved bugs

1. **Database displaying null values**

- In the early stages of creating the project, when a form was submitted from the add user persona page, the database was displaying null values with the associated key.
- A name attribute was missing from the input tag in the form, this was causing the associated value to not display any information. The solution was found here on [W3Schools](https://www.w3schools.com/tags/att_input_name.asp#:~:text=Definition%20and%20Usage,passed%20when%20submitting%20a%20form.).

2. **'Please select' option being submitted from form**

- The create user persona form has a 'please select' option in the occuption and industry dropdown which display as a placeholder value when users open the form. During development, this value was able to be submitted.
- To stop this value from being submitted, I inserted the 'disabled' attribute to the option so it was not clickable.

3. **An existing username could be registered more than once**

- When users decide to create a username for Personafy, the same username could be input more than once.
- To stop this from occuring, an if-else statement was created in the register function in app.py. It checks if a username already exists. If it exists, it flashes an error on the registration page and asks the user to try another name.

## Deployment

### Local Deployment

To run this project locally on your machine, you will need to install/use the following:

- Python 3
- PIP
- Git
- MongoDB
- An IDE such as Visual Studio Code or PyCharm.

To use this project, complete the following steps:

- Go to the Repository link at the top of this document and click on the Code button and copy the link provided, or alternatively download the zip-file. Be sure to unzip the file first.

![https://res.cloudinary.com/orla2020/image/upload/v1594882567/milestone-three/code-screenshot_ojcwmc.png](https://res.cloudinary.com/orla2020/image/upload/v1594882567/milestone-three/code-screenshot_ojcwmc.png)

- Open the project in your preferred IDE.
- Install the required dependencies for this project by running the following command in your terminal:
```
pip3 install -r requirements.txt
```
- In the root directory of you project, create an env.py file where you will store sensitive information.
- Inside your env.py file, be sure to create a SECRET_KEY variable and a MONGO_URI to link to your own database.
- Sign up for an account (free) at MongoDB and create a new database. You can call this database whatever you want, but to hook it up with this project, it is recommended to call the database Personafy.
- In the database, you should have the following collections:

**Users**
```
_id: <ObjectId>
username: <string>
password: <string>
```

**Persona**
```
_id: <ObjectId>
name: <string>
age: <string>
bio: <string>
profile: <string>
occupation_title: <ObjectId>
industry_title: <ObjectId>
goals: <array>
frustrations: <array>
creator: <string>
make_public: <boolean>
```

**Occupation**
```
_id: <ObjectId>
occupation_title: <string>
```

**Industry**
```
_id: <ObjectId>
industry_title: <string>
```
### Deployment to Heroku

To deploy this project to Heroku, the following steps were taken:

1. Create a ```requirements.txt``` file using the command ```pip freeze > requirements.txt```.
2. Create a ```Procfile``` to inform Heroku what type of app is being deployed. Inside the Procfile insert ```web: python3 app.py```. If your file is called run.py, be sure to swap it with app.py.
3. Commit ```requirements.txt``` and ```Procfile``` to Git.
4. Log in to Heroku (if you have yet to sign up for Heroku, do so before proceeding)
5. Create new app in Heroku. Make sure to give the app a unique name. Select your region and create the app.
6. On the dashboard, click 'settings' and then click 'reveal config vars'.
7. Set the following key/value settings for the config vars:

| Key | Value |
 --- | ---
IP | 0.0.0.0
MONGO_URI | `mongodb+srv://<username>:<password>@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority`
PORT | 5000
SECRET_KEY | `YOUR SECRET KEY`

8. In the CLI of IDE input the following:

```
$ heroku login
$ heroku git:remote -a personafy-app
$ git push heroku master
```
9. The option is there to connect to Github, but I used the CLI method of manually pushing to Heroku each time a change is to be made.
10. Open Heroku. Open the app and the Personafy app should be running.

## Credits

### Code

- Register and user login was adapted from this [repository](https://github.com/MiroslavSvec/DCD_lead/blob/master/app.py).
- Logout user was adapted from this [Stack Overflow post](https://stackoverflow.com/questions/27747578/how-do-i-clear-a-flask-session#:~:text=There%20is%20no%20way%20to,session%20dictionary%20will%20get%20erased.&text=I%20use%20session%20like%20this%20with%20flask%2C%20it%20does%20work.).
- Clear session cache on logout was used from this [Stack Overflow post](https://stackoverflow.com/questions/27747578/how-do-i-clear-a-flask-session) (the respective links are on the Hot Tips page.)

### Content

- All page content on Personafy was written by me.
- Content on the 'Hot Tips' page was directly taken from [NNGroup](https://www.nngroup.com/).

### Media

- Hero image on the home page was downloaded from [Stories by Freepik](https://stories.freepik.com/)
- Blue placeholder image that displays if a user does not submit a profile image, was created by me in Adobe Illustrator.
- Other images that are on display on the Public Personas page or My Personas page have been created by the respective registered user.

### Acknowledgements

- I would like to thank my mentor Antonio Rodriquez for his help and support throughout this project.
