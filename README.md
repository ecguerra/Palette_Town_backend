# Palette Town - Backend

## [Heroku](https://palette-town-api-heroku.herokuapp.com/)
## [Frontend Repo](https://github.com/ecguerra/Project_4_frontend)


## Installation Instructions
* Download and install all dependencies
* Create a SQL database named color_app
* Add DB info and SECRET_KEY to a file named config.py
* run app.py to create tables and start the app


## Backend Tech
* Python
* Postgres/SQL
* Flask
* Peewee
* bcrypt


## General Approach
I wanted to do a project in Flask to get more comfortable in Python. I started with a fairly simple concept, but wanted to give the app room to grow. I made sure to have 1:M and N:M models as well as full CRUD to be sure I covered all the basics.


## Obstacles
Understanding how to build the join tables and learning how to call the information I needed was the most difficult part of building the backend. Fortunately I had some prior knowledge of SQL and was able to use that to "translate" what I needed to do into Flask and Peewee. It definitely had a learning curve, but ultimately I was successful.

Once I tried to connect to the frontend, the biggest challenge became getting auth credentials passed from the backend to the frontend. I learned a lot about CORS because of this project, and especially about how seemingly small things can make a huge mess. I did eventually get everything to connect, but I'm never going to look at a stray '/' the same way again.


## Models
* AppUser
* Palette
* Color
* ColorPalette (N:M)
* SavedPalette (N:M)

[Lucidchart ERD](https://lucid.app/lucidchart/invitations/accept/1f29d2ef-6220-4f3a-9188-a495efec36b3)

## RESTful Routes
CRUD | Route | Description
----|----|------
GET | / or /home | Home
POST | /api/app_users/signup | Sign up
POST | /api/app_users/login | Log in
GET/POST | /api/app_users/logout | Log out
GET | /api/app_users/current | Get current user
GET | /api/palettes/ | Get current user's palettes
GET | /api/palettes/all | Get all palettes
GET | /api/palettes/id | Through the ColorPalette table, get a specific palette & associated colors
GET | /api/palettes/name/id | Get a specific palette's information
POST | /api/palettes/new | Create a new palette
PUT | /api/palettes/id | Edit a specific palette's information
DELETE | /api/palettes/id | Delete a specific palette
GET | /api/colors/ | Get all colors
POST | /api/colors/new | Find or create a color
POST | /api/color_palettes/ | Create a new color_palette
DELETE | /api/color_palettes/id | Delete a specific color_palette
POST | /api/saved_palettes/ | Create a new saved_palette
DELETE | /api/saved_palettes/id | Delete a specific saved_palette


## Acknowledgements
Thank you to my General Assembly instructors and IAs (Billie, Mateen, Fatima, and Khoury) for your knowledge, help, and support.

Big shoutout to the "Room 5 crew" (Monica, Dan, Taylor, Camille, Salima, Gabe, Lam, Vanessa, and Naomi) for the debugging, sanity checks, and commiserating.

And of course, thank you to Andy for making sure I ate regularly and for putting up with a grouchy code gremlin for 6 months.


## [Heroku](https://palette-town-api-heroku.herokuapp.com/)
## [Frontend Repo](https://github.com/ecguerra/Project_4_frontend)