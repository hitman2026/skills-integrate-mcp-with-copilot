# Mergington High School Activities API

A super simple FastAPI application that allows students to view and sign up for extracurricular activities.

## Features

- View all available extracurricular activities
- Sign up for activities
- Persistent storage using SQLite and SQLAlchemy

## Getting Started

1. Install the dependencies:

   ```
   pip install -r requirements.txt
   ```

2. Initialize the database:

   ```
   python src/init_db.py
   ```

3. Run the application:

   ```
   python src/app.py
   ```

4. Open your browser and go to:
   - API documentation: http://localhost:8000/docs
   - Alternative documentation: http://localhost:8000/redoc

## API Endpoints

| Method | Endpoint                                                          | Description                                                         |
| ------ | ----------------------------------------------------------------- | ------------------------------------------------------------------- |
| GET    | `/activities`                                                     | Get all activities with their details and current participant count |
| POST   | `/activities/{activity_name}/signup?email=student@mergington.edu` | Sign up for an activity                                             |
| DELETE | `/activities/{activity_name}/unregister?email=student@mergington.edu` | Unregister from an activity                                    |

## Data Model

The application uses a database model:

1. **Activities**
   - Name (unique)
   - Description
   - Schedule
   - Maximum number of participants allowed
   - List of participant emails

2. **Participants**
   - Email
   - Activity (foreign key)

All data is stored in a SQLite database (`activities.db`).
