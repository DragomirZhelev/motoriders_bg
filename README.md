# Motoriders BG

A Django web application for motorcycle riders in Bulgaria.

## Features

### Riders
- Create rider profiles
- View rider details
- Edit rider profiles
- Delete rider profiles
- List all riders

### Rides
- Create rides
- View ride details
- Edit rides
- Delete rides
- List all rides
- Support for different road types
- Ride difficulty and status tracking
- Participant management

### Ride Reviews
- Create ride reviews
- View ride review details
- Edit ride reviews
- Delete ride reviews
- List all ride reviews
- Ratings for:
  - Overall experience
  - Road conditions
  - Scenery
  - Riding difficulty

### Road Assistance
- Create help requests
- View help request details
- Edit help requests
- Delete help requests
- List all help requests
- Urgency and status tracking

## Technologies

- Python 3
- Django
- SQLite
- HTML
- CSS
- Django Template Language (DTL)

## Project Structure

- common
- riders
- rides
- assistance

## Models

- Rider
- Ride
- RideReview
- HelpRequest

## Implemented Functionality

- Full CRUD for Rider
- Full CRUD for Ride
- Full CRUD for RideReview
- Full CRUD for HelpRequest
- Custom model validation
- Custom form validation
- Custom error messages
- Labels
- Help texts
- Placeholders
- Disabled delete forms
- Foreign Key relationships
- Many-to-Many relationships
- Database constraints
- Timestamp model inheritance

## Installation

Clone the repository.

Create a virtual environment.

Install dependencies.

Apply migrations.

Run the server.

## Database

The application works with an empty database.

All required objects can be created through the user interface without using the Django admin panel.

## Current Status

### Completed
- Rider CRUD
- Ride CRUD
- RideReview CRUD
- HelpRequest CRUD
- Forms customization
- Form validation
- Model validation
- Custom error messages
- Labels, help texts and placeholders
- URL routing
- CRUD templates
- Disabled delete forms
- Model relationships and constraints

### In Progress
- Home page
- Navigation menu
- Search and filtering
- Custom template tags and filters
- Bootstrap styling
- Custom 404 page
- Final project documentation

## Author

Dragomir Zhelev