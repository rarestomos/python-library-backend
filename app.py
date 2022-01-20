import logging

from flask import Flask
from library_backend.blueprints.books_blueprint import books
from library_backend.blueprints.reservations_blueprint import reservations
from library_backend.blueprints.users_blueprint import users
from library_backend.database import SQLiteDatabaseConnection

logger = logging.getLogger(__name__)

app = Flask("LibraryBackend")

app.register_blueprint(users)
app.register_blueprint(books)
app.register_blueprint(reservations)


if __name__ == '__main__':
    db = SQLiteDatabaseConnection()
    with db:
        db.create_tables_if_not_exists()
    with db:
        db.add_some_data_if_does_not_exist()
    app.run(host="127.0.0.1", port=50000, debug=True)
