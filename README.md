## Building a POST/PATCH/DELETE API
This project is a Flask application providing an API for managing games, reviews, and users, supporting CRUD operations: POST, GET, PUT, and DELETE requests.

## Table of Contents
Installation
Database Setup
Seeding the Database
Running the Application
API Endpoints
Postman Examples
License
Installation
Clone the repository:

## bash
Copy code
bash Copy code git clone https://github.com/learn-co-curriculum/python-p4-building-post-patch-delete-api Create a virtual environment:
Create and activate a virtual environment:

bash
Copy code
python -m venv venv
venv\Scripts\activate    # On Windows
source venv/bin/activate # On macOS/Linux
Install dependencies:

# bash
Copy code
pip install -r requirements.txt
Database Setup
Initialize the database:
# bash
Copy code
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
Seeding the Database
Run the seed script:
# bash
Copy code
python seed.py
Running the Application
Run the Flask application:

# bash
Copy code
python app.py
Access the application:

Copy code
http://127.0.0.1:5000
API Endpoints
Games
GET /games: Retrieve all games.
POST /games: Create a new game.
GET /games/int:id: Retrieve a specific game by ID.
PUT /games/int:id: Update a specific game by ID.
DELETE /games/int:id: Delete a specific game by ID.
Reviews
GET /reviews: Retrieve all reviews.
POST /reviews: Create a new review.
GET /reviews/int:id: Retrieve a specific review by ID.
PUT /reviews/int:id: Update a specific review by ID.
DELETE /reviews/int:id: Delete a specific review by ID.
Users
GET /users: Retrieve all users.
POST /users: Create a new user.
GET /users/int:id: Retrieve a specific user by ID.
PUT /users/int:id: Update a specific user by ID.
DELETE /users/int:id: Delete a specific user by ID.
Postman Examples
Games
GET /games

## Open Postman.
Create a new GET request.
Set the URL to http://127.0.0.1:5000/games.
Send the request and view the response.
POST /games

## Open Postman.
Create a new POST request.
Set the URL to http://127.0.0.1:5000/games.
In the Body tab, select raw and JSON, then add:
json
Copy code
{
    "title": "New Game",
    "genre": "Genre",
    "platform": "Platform",
    "price": 60
}
Send the request and view the response.
Reviews
GET /reviews

## Open Postman.
Create a new GET request.
Set the URL to http://127.0.0.1:5000/reviews.
Send the request and view the response.
POST /reviews

## Open Postman.
Create a new POST request.
Set the URL to http://127.0.0.1:5000/reviews.
In the Body tab, select raw and JSON, then add:
json
Copy code
{
    "score": 9,
    "comment": "Amazing game!",
    "game_id": 1,
    "user_id": 1
}
Send the request and view the response.
Users
GET /users

## Open Postman.
Create a new GET request.
Set the URL to http://127.0.0.1:5000/users.
Send the request and view the response.
POST /users
## Open Postman.
Create a new POST request.
Set the URL to http://127.0.0.1:5000/users.
In the Body tab, select raw and JSON, then add:
json
Copy code
{
    "name": "New User"
}
Send the request and view the response.
## License
This project is licensed under the MIT [LICENSE](LICENSE).