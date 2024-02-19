# Simple Note-Taking Application RESTful API

This README provides an overview of the RESTful API for a simple note-taking application. The API allows users to perform basic CRUD operations (Create, Read, Update, Delete) on notes. It includes information about endpoints, data model, validation, error handling, testing, and best practices.

## Endpoints

### User Authentication
- **POST /login**: Create a simple login view.
- **POST /signup**: Create a single user sign-up view.

### Notes
- **POST /notes/create**: Create a new note.
- **GET /notes/{id}**: Retrieve a specific note by its ID.
- **POST /notes/share**: Share the note with other users.
- **PUT /notes/{id}**: Update an existing note.
- **GET /notes/version-history/{id}**: Get all the changes associated with the note.

## Data Model

The application utilizes an efficient schema to support all the functionalities. It includes a user model and a note model.

### User Model
- Username
- Email
- Password (hashed)

### Note Model
- Title
- Content
- Created_at
- Updated_at
- User (Foreign key to User model)
- Shared_with (Many-to-Many relationship with User model)

## Validation

Basic input validation is implemented for creating and updating notes. Required fields are checked, and appropriate data types are enforced.

## Error Handling

Errors are handled gracefully, and meaningful error responses with appropriate HTTP status codes are returned for different scenarios.

## Testing

Unit tests are written to ensure the functionality and integrity of the API endpoints. Automated testing tools like Postman or cURL can be used to test the APIs.

## Best Practices

- Django's built-in user authentication system is utilized for user registration and login.
- Serializers are used for API data validation.
- Necessary error handling is implemented.
- Appropriate responses are provided for different scenarios.
- Proper authentication and authorization mechanisms are in place.
- Updates to existing shared notes are carefully handled to ensure data integrity.

---
By Jotirmay Manik
