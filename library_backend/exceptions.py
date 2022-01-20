class InvalidUser(Exception):
    def __init__(self, value):
        super().__init__(f"Invalid user {value}")


class ResourceNotFound(Exception):
    def __init__(self, resource_type, field,  value):
        super().__init__(f"{resource_type} with {field} = {value} was not found")


class UserAlreadyExists(Exception):
    def __init__(self, value):
        super().__init__(f"User with email: {value['email']} already exists")


class InvalidBook(Exception):
    def __init__(self, value):
        super().__init__(f"Invalid book {value}")


class BookAlreadyExists(Exception):
    def __init__(self, value):
        super().__init__(f"Book with name: {value['name']} written by author: {value['author']} already exists")


class ReservationAlreadyExists(Exception):
    def __init__(self, value):
        super().__init__(f"Reservation for user: {value['user_id']} and book: {value['book_id']} already exists")


class ReservationIsInvalid(Exception):
    def __init__(self, value):
        super().__init__(f"Reservation for user: {value['user_id']} and book: {value['book_id']} is invalid")


class RequiredFieldException(ValueError):
    def __init__(self, field_name):
        super().__init__(f"'{field_name}' is required")


class InvalidFieldException(ValueError):
    def __init__(self, field_name):
        super().__init__(f"'{field_name}' is invalid")


class RequiredCharactersLengthException(ValueError):
    def __init__(self, field_name, min=3, max=70):
        super().__init__(f"'{field_name}' must be between {min} and {max} characters")


class DatabaseCommunicationIssue(Exception):
    def __init__(self, action):
        super().__init__(f"There was an error performing the {action}")


class AlphanumericException(ValueError):
    def __init__(self, field_name):
        super().__init__(f"'{field_name}' is invalid, it must contain only alphanumeric characters")
