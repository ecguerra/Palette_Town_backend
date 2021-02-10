# Project_4_backend

BACKEND
- [x] link to frontend repo
- [] link to deployed api
- [] explanation of backend tech used
- [] general approach (a couple paragraphs)
- [] installation instructions
- [] table with RESTful routes & resources available at each endpoint
- [] unsolved problems / major hurdles

[Frontend Repo](https://github.com/ecguerra/Project_4_frontend)

## Backend Tech
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
GET | /api/palette/:id | Palette detail
GET | /api/colors | View all colors
GET | /api/colors/:id | View one color
POST | /signup | Sign Up
POST | /login | Login
POST | /api/colors/new | Create a color
POST | /api/palette/new | Save palette
PUT | /palette/:id | Edit palette (including private/public and upvoting?)
DELETE | /palette/:id | Delete palette