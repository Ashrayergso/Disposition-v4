# Crew Assignment Automation App

This is a Django application designed to automate the crew assignment process for cruise ships. The primary goal is to minimize mistakes, avoid contract violations, ensure that all ships are staffed with a fully qualified crew, and maintain an updated and accurate sailing schedule.

## Tech Stack

- Django framework for building the application
- PostgreSQL for the database

## Getting Started

1. **Environment Setup**
   - Install Python, Django, PostgreSQL: Follow platform-specific instructions.
   - Create Virtual Environment: Use Conda or virtualenv.
   - Create Django Project: Run `django-admin startproject project_name`.
   - Create Django App: Inside the project, run `python manage.py startapp app_name`.

2. **Database Configuration**
   - Install PostgreSQL: Follow installation instructions for your OS.
   - Create Database: Create a new PostgreSQL database.
   - Configure Django Settings: Update `project_name/settings.py` with database settings.

## Application Structure

The main components of the application are:

- Models: Defined in `app_name/models.py`. These include `Crew`, `Ship`, `Assignment`, `ShipSailingSchedule`, `PositionAndContractLength`, `ShipCrewAllowance`, and `CertificateTypesAndExpiry`.
- Views: Defined in `app_name/views.py`. These include CRUD operations for the models and the logic for automatic crew assignment.
- URLs: Defined in `app_name/urls.py`. These include paths for the views and names for URL reversing.
- Templates: Located in `app_name/templates/app_name/`. These include HTML files for the views.
- Static Files: Located in `app_name/static/app_name/`. These include CSS and JavaScript files for styling and interactivity.

## Running the Application

1. Run migrations: `python manage.py makemigrations` and `python manage.py migrate`.
2. Start the server: `python manage.py runserver`.

## Testing

Tests are located in `app_name/tests.py`. Run them with `python manage.py test`.

## Deployment

Follow the instructions in `deployment_instructions.txt` to deploy the application.

## API Endpoints

The application provides the following RESTful API endpoints:

- GET `/api/ships/`: Retrieve the list of ships.
- POST `/api/assignments/`: Create a new assignment.
- PUT `/api/crew_members/<id>/`: Update a specific crew member's details.

## Contributing

Please follow the SOLID and DRY principles when contributing. Also, use a consistent naming pattern across the project:

- Models: Singular nouns (e.g., `Crew`, `Ship`)
- Views: Descriptive function names (e.g., `list_crew_members`, `assign_crew_to_ship`)
- URLs: Descriptive paths (e.g., `crew_list`, `ship_detail`)
- Templates: Match view names (e.g., `crew_list.html`, `ship_detail.html`)

Consider using a linter like flake8 to enforce naming conventions and code style.