# Building a POST/PATCH/DELETE API

This project is a Flask application that provides an API for managing games, reviews, and users. The API supports CRUD operations, including POST, GET, PUT, and DELETE requests.

## Table of Contents
- [Installation](#installation)
- [Database Setup](#database-setup)
- [Seeding the Database](#seeding-the-database)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Templates](#templates)
- [License](#license)

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/yourrepository.git
    cd yourrepository
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Database Setup

1. **Initialize the database**:
    ```bash
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

## Seeding the Database

1. **Run the seed script to populate the database with initial data**:
    ```bash
    python seed.py
    ```

## Running the Application

1. **Run the Flask application**:
    ```bash
    python app.py
    ```

2. **Access the application in your web browser**:
    ```
    http://127.0.0.1:5000
    ```

## API Endpoints

### Games

- **GET /games**: Retrieve all games.
    - Response: 
    ```json
    [
        {
            "id": 1,
            "title": "Game 1",
            "genre": "Genre",
            "platform": "Platform",
            "price": 50
        },
        ...
    ]
    ```

- **POST /games**: Create a new game.
    - Request Body: 
    ```json
    {
        "title": "New Game",
        "genre": "Genre",
        "platform": "Platform",
        "price": 60
    }
    ```

- **GET /games/<int:id>**: Retrieve a specific game by ID.
    - Response: 
    ```json
    {
        "id": 1,
        "title": "Game 1",
        "genre": "Genre",
        "platform": "Platform",
        "price": 50
    }
    ```

- **PUT /games/<int:id>**: Update a specific game by ID.
    - Request Body (partial or full):
    ```json
    {
        "title": "Updated Game",
        "genre": "Updated Genre",
        "platform": "Updated Platform",
        "price": 70
    }
    ```

- **DELETE /games/<int:id>**: Delete a specific game by ID.
    - Response: 
    ```json
    {
        "delete_successful": True,
        "message": "Game deleted."
    }
    ```

### Reviews

- **GET /reviews**: Retrieve all reviews.
    - Response: 
    ```json
    [
        {
            "id": 1,
            "score": 8,
            "comment": "Great game!",
            "game_id": 1,
            "user_id": 1
        },
        ...
    ]
    ```

- **POST /reviews**: Create a new review.
    - Request Body: 
    ```json
    {
        "score": 9,
        "comment": "Amazing game!",
        "game_id": 1,
        "user_id": 1
    }
    ```

- **GET /reviews/<int:id>**: Retrieve a specific review by ID.
    - Response: 
    ```json
    {
        "id": 1,
        "score": 8,
        "comment": "Great game!",
        "game_id": 1,
        "user_id": 1
    }
    ```

- **PUT /reviews/<int:id>**: Update a specific review by ID.
    - Request Body (partial or full):
    ```json
    {
        "score": 9,
        "comment": "Even better after replaying!"
    }
    ```

- **DELETE /reviews/<int:id>**: Delete a specific review by ID.
    - Response: 
    ```json
    {
        "delete_successful": True,
        "message": "Review deleted."
    }
    ```

### Users

- **GET /users**: Retrieve all users.
    - Response: 
    ```json
    [
        {
            "id": 1,
            "name": "User 1"
        },
        ...
    ]
    ```

- **POST /users**: Create a new user.
    - Request Body: 
    ```json
    {
        "name": "New User"
    }
    ```

- **GET /users/<int:id>**: Retrieve a specific user by ID.
    - Response: 
    ```json
    {
        "id": 1,
        "name": "User 1"
    }
    ```

- **PUT /users/<int:id>**: Update a specific user by ID.
    - Request Body (partial or full):
    ```json
    {
        "name": "Updated User"
    }
    ```

- **DELETE /users/<int:id>**: Delete a specific user by ID.
    - Response: 
    ```json
    {
        "delete_successful": True,
        "message": "User deleted."
    }
    ```

## Templates
 in the `templates` directory:
- `index.html`: To display the list of games.
- `reviews.html`: To display the list of reviews.
- `game_detail.html`: To display details of a specific game.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
