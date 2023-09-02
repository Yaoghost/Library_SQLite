# Library Management Web App

## Introduction

This project is a simple web application built using Flask and SQLite, designed to help users manage their book collections. Users can add new books to the library, edit book ratings, and view the entire collection through a user-friendly web interface.

## Features

- **Add New Books**: Users can input book details, including title, author, and rating, to add new books to their library.

- **Edit Book Ratings**: Existing book ratings can be modified by selecting the "Edit rating" option for a particular book.

- **Display Library**: The application displays all stored books, including their titles, authors, and current ratings on the homepage.

## Technologies Used

- Python
- Flask (Web Framework)
- SQLite (Database)
- SQLAlchemy (Object-Relational Mapping)
- HTML (for rendering web pages)

## Usage

1. Install the required dependencies listed in the `requirements.txt` file.

2. Run the Flask application using `python main.py`.

3. Access the web interface by opening a web browser and navigating to `http://localhost:5000`.

4. Interact with the library by adding new books, editing ratings, and viewing your collection.

## Project Structure

- `main.py`: The main application script containing Flask routes and database interactions.

- `templates/`: This directory contains HTML templates for rendering web pages.

- `new-books-collection.db`: The SQLite database file for storing book data.

- `requirements.txt`: Lists the required Python packages and their versions.

## Contribution

Contributions to this project are welcome! Feel free to open issues, suggest improvements, or fork the repository and submit pull requests.


