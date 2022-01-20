# Description
A basic backend service for a simple library app to be used for learning RestApi automation testing

# Requirements for running the application
* python 3.6 - https://www.python.org/downloads/release/python-360/
* pip - https://www.liquidweb.com/kb/install-pip-windows/

# Running the application
* clone the repository
* install requirements: _pip install -r requirements.txt_
* run the app.py file: _python app.py_
* do requests to http://127.0.0.1:50000

# Reset the database and re-add generic data
* remove/delete the db.sqlite file
* run the app.py script again - it will recreate the database and init some test data

# Functionality
* the app exposes endpoints for users, books, reservations
## User Endpoints
### Available endpoints
* get all users: Get /users
* create user: Post /users
* get user: Get /users/<user_id>
* delete user: Delete /users/<user_id>
* edit user: Put /users/<user_id>
### User payload:
```python
{
    "id": "",
    "first_name": "",
    "last_name": "",
    "email": ""
}
```
### Constraints:
* email should be unique

## Book Endpoints
### Available endpoints
* get all books: Get /books
* create book: Post /books
* get book: Get /books/<book_id>
* delete book: Delete /books/<book_id>
* edit book: Put /books/<book_id>

### Book payload:
```python
{
    "id": "",
    "name": "",
    "author": ""
}
```

## Reservation endpoints
### Available endpoints
* get all reservations: Get /reservations
* create reservation: Post /reservations
* get reservation by book_id: Get /reservations/book/<book_id>
* get reservation by user_id: Get /reservations/user/<user_id>
* get reservation by user_id and book_id: Get /reservations/user/<user_id>/book/<book_id>
* delete reservation: Delete /reservations/user/<user_id>/book/<book_id>
* delete reservation by book_id: Delete /reservations/book/<book_id>
* delete reservation by user_id: Delete /reservations/user/<user_id>
* edit reservation: Put /reservations/user/<user_id>/book/<book_id>

### Reservations payload
#### Create
```python
{
    "book_id":"",
    "user_id":"",
    "reservation_date": "",
    "reservation_expiration_date": ""
}
```

#### Get
```python
{
        "user": {
            "id": "",
            "first_name": "",
            "last_name": "",
            "email": ""
        },
        "book": {
            "id": "",
            "name": "",
            "author": ""
        },
        "reservation_date": "",
        "reservation_expiration_date": ""
    }
```