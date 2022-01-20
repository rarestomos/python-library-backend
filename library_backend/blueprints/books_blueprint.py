import logging

from flask import Blueprint, request

from library_backend.api import BookApi, app_response

logger = logging.getLogger(__name__)

books = Blueprint("books", __name__)


@books.route('/books', methods=['GET'])
def get_books():
    book_api = BookApi()
    book_name = request.args.get("name")
    author_name = request.args.get("author")
    if book_name:
        response = book_api.get_books_by_name(book_name.strip("\"\'"))
    elif author_name:
        response = book_api.get_books_by_author(author_name.strip("\"\'"))
    else:
        response = book_api.get_books()
    return app_response(response)


@books.route('/books', methods=['POST'])
def create_book():
    book = request.get_json(force=True)
    book_api = BookApi()
    response = book_api.create_book(book)
    return app_response(response)


@books.route('/books/<book_id>', methods=['GET'])
def get_book(book_id):
    book_api = BookApi()
    response = book_api.get_book(book_id)
    return app_response(response)


@books.route('/books/<book_id>', methods=['PUT'])
def edit_book(book_id):
    new_book = request.get_json(force=True)
    book_api = BookApi()
    response = book_api.update_book(book_id=book_id, new_book=new_book)
    return app_response(response)


@books.route('/books/<book_id>', methods=['DELETE'])
def delete_book(book_id):
    book_api = BookApi()
    response = book_api.delete_book(book_id)
    return app_response(response)
