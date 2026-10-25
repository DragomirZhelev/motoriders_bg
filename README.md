# MotoRiders BG

MotoRiders BG is a Django web application for motorcycle riders in Bulgaria.

The application allows riders to create profiles, organize group rides, join and leave planned rides, publish ride reviews, and create roadside assistance requests.

## Features

### Rider Profiles

- Create, view, edit, and delete rider profiles
- Search riders by first name, last name, or nickname
- Store motorcycle brand, model, type, and riding experience
- Store contact information and an optional short biography
- Upload an optional profile photo
- Select a Bulgarian city from a predefined list
- Provide a custom city or village when `Other` is selected
- Prevent custom locations from being entered when a standard city is selected
- Display the number of rides organized by each rider
- Display the number of reviews submitted by each rider

### Rides

- Create, view, and delete rides, edit rides only in status Planned
- Search rides by:
  - Ride title
  - Organizer name or nickname
  - Participant name or nickname
  - Meeting point
  - Destination
  - Road type
  - Road difficulty
  - Description
- Filter rides by status
- Sort rides by creation date
- Store:
  - Ride organizer
  - Meeting point
  - Starting city
  - Destination
  - Departure date and time
  - Estimated duration
  - Distance
  - Multiple road types
  - Road difficulty
  - Ride status
  - Maximum participant capacity
  - Ride description
- Preserve selected road types when editing a ride
- Display the current participant count
- Display the number of remaining participant slots
- Display ride statuses using custom template filters
- Allow riders to join planned rides
- Allow existing participants to leave rides
- Prevent the ride organizer from joining as a participant
- Prevent the same rider from joining twice
- Prevent riders from joining completed or canceled rides
- Prevent riders from joining a ride when its capacity has been reached

### Ride Reviews

- Create, view, edit, and delete ride reviews
- Search reviews by ride title or reviewer name
- Rate:
  - Overall ride experience
  - Road conditions
  - Scenery
  - Riding difficulty
- Display rating descriptions using custom template filters
- Restrict reviews to the ride organizer or existing participants
- Allow reviews only for rides with Completed Status
- Enforce one review per rider for each ride through a database constraint

### Road Assistance

- Create, view and delete roadside assistance requests; edit requests only in status Open
- Record:
  - Rider requesting assistance
  - Request title
  - Issue description
  - Urgency level
  - Location
  - Request status
- Filter requests by `Open` or `Closed` status

## Additional Functionality

- Create, view, edit and delete functionality for all models with editing restricted by status for rides and help requests
- Search, filtering, and sorting through GET query parameters
- Custom form validation
- Custom model validators
- Custom error messages
- Customized labels, help texts, placeholders, and widgets
- Disabled fields in delete confirmation forms
- Dedicated delete confirmation pages
- Custom template tags
- Custom template filters
- Built-in template tags and filters
- Custom 404 error page
- Join and leave ride functionality
- Bootstrap-based responsive design
- Dark motorcycle-themed user interface
- Shared navigation and footer across all pages
- Reusable partial templates for cards, navigation, header, and footer
- Support for an empty database without fixtures or prepopulated data

## Technologies

- Python
- Django
- SQLite
- HTML
- CSS
- Bootstrap 5
- Django Template Language
- Pillow for image uploads

Exact dependency versions are available in `requirements.txt`.

## Project Structure

```text
motoriders_bg/
├── motoriders_bg/        # Project settings and root URL configuration
├── common/               # Shared choices, validators, mixins and home page
├── riders/               # Rider profiles
├── rides/                # Rides, ride reviews and ride participation
├── assistance/           # Road assistance requests
├── templates/            # Application templates and reusable partials
├── media/                # Uploaded files during local development
├── manage.py
├── requirements.txt
└── README.md
```

## Main Models

### Rider

Stores rider profile information, motorcycle details, location, contact information, profile photo, riding experience, and biography.

### Ride

Stores organized motorcycle rides, route information, road types, participant capacity, ride status, and participants.

### RideReview

Stores feedback and ratings submitted by ride organizers or participants.

### HelpRequest

Stores roadside assistance requests created by riders.

## Database Relationships

### Many-to-One Relationships

- Multiple rides can be organized by one rider
- Multiple reviews can belong to one ride
- Multiple reviews can be written by one rider
- Multiple help requests can be created by one rider

### Many-to-Many Relationship

- One ride can have multiple participants
- One rider can participate in multiple rides

## Installation and Running

### 1. Clone the repository

```bash
git clone https://github.com/DragomirZhelev/motoriders_bg
cd motoriders_bg
```


### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

On Windows Command Prompt:

```cmd
.venv\Scripts\activate
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply database migrations

```bash
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

### 7. Open the application

Open the following address in a browser:

```text
http://127.0.0.1:8000/
```

## Environment Variables and Credentials

No environment variables or external credentials are required to run the project locally with its default configuration.

The project is configured for local development and uses Django's default development settings.

The custom 404 error page is available in the project. To preview it locally, temporarily set DEBUG = False in motoriders_bg/settings.py and set ALLOWED_HOSTS to include 127.0.0.1 and localhost. Restore the development settings after testing.

## Main Pages

- `/` - Home page
- `/riders/list/` - Rider profiles
- `/rides/list/` - Rides
- `/rides/ride-review/list/` - Ride reviews
- `/assistance/list/` - Road assistance requests

All application objects can be created and managed through the available navigation links. Direct database manipulation and the Django admin panel are not required.

## Empty Database Support

The application is designed to work with an empty database.

After applying the migrations, the evaluator can create all required objects manually through the user interface in the following order:

1. Create one or more riders
2. Create a ride and select an existing rider as organizer
3. Join riders to a planned ride
4. After the departure date has passed, edit the ride and set its status to Completed
5. Create a review for that completed ride, using its organizer or a participant as the reviewer
6. Create roadside assistance requests

The project does not rely on fixtures, custom data migrations, or initialization scripts.

## Database and Uploaded Files

The project uses SQLite by default.

Django creates the local `db.sqlite3` file when migrations are applied.

Rider profile photos are stored under:

```text
media/riders_photos/
```

The local database and uploaded media files are runtime data and are not included in version control.

## Forms and Validation

The application includes:

- Model forms for all main models
- A dedicated form for joining rides
- Model-level validators
- Field-specific cleaning methods
- Cross-field validation with form `clean()` methods
- User-friendly validation messages
- Customized labels, help texts, placeholders, and widgets
- Disabled fields on deletion confirmation forms
- CSRF protection for all POST forms

## Templates

The project uses:

- A shared base template
- Template inheritance
- Reusable header, navigation, and footer templates
- Reusable card templates for all main models
- Built-in Django template tags and filters
- Custom template tags and filters
- A custom 404 error page
- Bootstrap 5 for layout and visual styling

## Authentication

Authentication and Django User management are intentionally not implemented because they are excluded from the project requirements.

The application does not provide login, logout, registration, or role-based permissions.

## Author

Dragomir Zhelev