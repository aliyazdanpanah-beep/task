# Project Management API

A RESTful API built with FastAPI, SQLAlchemy, and PostgreSQL for managing projects.

## Requirements

Before running the project, make sure the following are installed:

* Python 3.10+
* PostgreSQL
* pip

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd <project-folder>
```

### 2. Create and activate a virtual environment

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## PostgreSQL Setup

### 1. Create a PostgreSQL database

Example:

```sql
CREATE DATABASE project_db;
```

### 2. Update the database connection settings

Configure the PostgreSQL connection string in the project settings.

Example:

```text
postgresql://username:password@localhost:5432/project_db
```

Replace:

* `username` with your PostgreSQL username
* `password` with your PostgreSQL password
* `project_db` with your database name

### 3. Create the required table

Run the following SQL script in pgAdmin or PostgreSQL:

```sql
DROP TABLE IF EXISTS project;

CREATE TABLE project (
    id SERIAL PRIMARY KEY,
    title VARCHAR(280),
    location VARCHAR(200),
    start_date INTEGER,
    budget BIGINT
);
```

## Running the Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

If your application entry point has a different filename, replace `main` with the appropriate file name.

## API Documentation

After starting the server, open:

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

## Technologies Used

* FastAPI
* SQLAlchemy
* PostgreSQL
* Pydantic
* Uvicorn

## Notes

* Ensure PostgreSQL is running before starting the application.
* Make sure the database connection settings are correctly configured.
* Install all dependencies from `requirements.txt` before running the project.
