# Personafy

Personafy is an online tool for creating custom user personas in minutes. Users have the ability to search for pre-built templates, or sign up to create their own personas based on their own personal / business needs.

Using CRUD functionality, users can (C)reate, (R)ead, (U)pdate and (D)elete users personas using Personafy.
 
## UX

#### User Stories
 
- As a user I want to view the site from any device (mobile, tablet and desktop).
- As a user I want to have a search box so I can search for personas related to my business area(s). - edit/delete
- As a user I want to view pre-made personas for inspiration.
- As a user, I want to be able to print a persona so I can bring it to my team meeting.
- As a user, I want to read about user personas and best practice, tips and tricks for using a user person in my projects.

- As a user-contributor, I want to be able to create my own profile.
- As a user-contributor, I want to be able to create my own personas.
- As a user-contributor, I want to be able to keep my personas private because I am using them for my team at my company workplace. -delete
- As a user-contributor, I want to be able to make some of my personas public. - delete
- As a user-contributor, I want to be able to edit/modify an existing persona. 
- As a user-contributor, I want to be able to delete an existing persona.
- As a user-contributor, I want to have a confirmation/warning before deleting an entry.
- As a user-contributor, I want to be able to log out of my account.
- As a user-contributor, I want to be able to delete my account if I do not want to use the website any more.


## Features
 
### Existing Features

#### Register

- Visitors to the website can sign up to the website and have an account. Users need to fill out a basic form which requires entering a username and password. Username and password are stored in the users collection in the database.

#### Log in 

- If users register to the website, they have the ability to log in using the same simple form containing their username and password. This gives registered users the possibility to add personas, edit them and delete them. 

#### Log out

- Users can log out from their session on the website.

#### Add a user persona

- When users are logged in, they can create or 'add' a user persona using a form. Details required for the user persona are 'name', 'age', 'bio', 'occupation', 'industry', 'goals' and 'frustrations'. Using an image with the user persona is optional, a randomly generated image will be used in this case.

#### View user personas

- Read or 'view' user personas, either from the public personas page, or the my perosnas page when the user is logged in. Users can also view an individual user persona. From there, users can print personas, or if a user is logged in, they can also edit their own persona from this screen.

#### Edit a user persona

- Logged in users can edit or modify their user personas and update the database with the user personas updated information. The edit form is similar to the 'create' user persona form.

#### Delete a user persona

- Logged in users can delete any user persona that they have made. Before a user persona is deleted, a pop up modal displays asking the user if they are sure they want to delete it.


### Features Left to Implement

- Another feature idea 

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

### Database Choice

### Database Schema

This project's database contains 3 main collections to store data.

### Data Storage Types

The types of data stored in MongoDB for this project are:

- ObjectId
- String
- Array

### Database Collections Structure

## Testing

### Manual Testing

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

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- Register and user login was adapted from this [repo](https://github.com/MiroslavSvec/DCD_lead/blob/master/app.py)
- Logout user was adapted from this [Stack Overflow post](https://stackoverflow.com/questions/27747578/how-do-i-clear-a-flask-session#:~:text=There%20is%20no%20way%20to,session%20dictionary%20will%20get%20erased.&text=I%20use%20session%20like%20this%20with%20flask%2C%20it%20does%20work.)
- Dropdown on hover from this [Stack Overflow post](https://stackoverflow.com/questions/42183672/how-to-implement-a-navbar-dropdown-hover-in-bootstrap-v4)
- Clear session cache on logout was used from this [Stack Overflow post](https://stackoverflow.com/questions/27747578/how-do-i-clear-a-flask-session)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X
