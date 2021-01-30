# Project_4_backend

## Back end Tech
* Python
* Postgres
* Flask
* Peewee
* bcrypt

## Models
* Users
* Palettes
* Colors
* ColorPalette (N:M)
* UserPalette (1:M)
* UserFavorites (N:M)

## RESTful Routes
CRUD | Route | Description
----|----|------
GET | / or /home | Home
GET | /profile | User's profile
GET | /palette/:id | Palette detail
POST | /signup | Sign Up
POST | /login | Login
POST | /palette/:id | Save palette
PUT | /palette/:id | Edit palette (including private/public and upvoting?)
DELETE | /palette/:id | Delete palette