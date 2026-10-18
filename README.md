# Multi-Database Management System

A full-stack web application that demonstrates how one application can access and modify data stored in three separate PostgreSQL databases.

The project was created as a database programming assignment. The application provides a React user interface where the user can select a database and perform CRUD operations on its data.

## Features

The application allows the user to:

- Select between three separate PostgreSQL databases
- View records stored in the selected database
- Add new records
- Edit existing records
- Delete records
- Refresh the displayed data
- Use pre-populated dummy data for testing

The application implements the four basic CRUD operations:

- **Create** - Add a new record
- **Read** - View existing records
- **Update** - Modify an existing record
- **Delete** - Remove a record


## Technologies

### Frontend

- React
- JavaScript
- Vite
- CSS

### Backend

- Python
- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn
- Psycopg

### Database

- PostgreSQL

### Development tools

- Visual Studio Code
- pgAdmin 4
- Git
- GitHub

---

## Application Architecture

The frontend and backend are separated into two parts.

```text
React + Vite
    |
    | HTTP / JSON
    v
FastAPI REST API
    |
    v
SQLAlchemy
    |
    +-----------------------+
    |           |           |
    v           v           v
customers_db vehicles_db services_db
    |           |           |
customers   vehicles     service_records
    |
PostgreSQL
```

React communicates with the FastAPI backend using HTTP requests and JSON.

FastAPI uses SQLAlchemy to access the three PostgreSQL databases.

---

## Databases

The application uses three separate PostgreSQL databases.

### 1. customers_db

Contains customer information.

Table:

```text
customers
```

Fields:

```text
id
name
email
phone
```

Example:

```text
1 | Matti Meikäläinen | matti@example.com | 0401234567
```

---

### 2. vehicles_db

Contains vehicle information.

Table:

```text
vehicles
```

Fields:

```text
id
registration_number
manufacturer
model
year
customer_id
```

Example:

```text
1 | ABC-123 | Mercedes-Benz | C-Class | 2022 | 1
```

`customer_id` logically refers to a customer stored in `customers_db`.

---

### 3. services_db

Contains vehicle service records.

Table:

```text
service_records
```

Fields:

```text
id
vehicle_id
service_date
description
mileage
```

Example:

```text
1 | 1 | 2026-04-12 | Annual maintenance | 45000
```

`vehicle_id` logically refers to a vehicle stored in `vehicles_db`.

---

## Database Relationships

Because the entities are stored in physically separate PostgreSQL databases, relationships between them are handled at the application level.

The logical relationship is:

```text
customers_db
Customer
|
| customer_id
v
vehicles_db
Vehicle
|
| vehicle_id
v
services_db
Service Record
```

Cross-database foreign key constraints are therefore not used in this project.

---

## REST API

FastAPI provides REST endpoints for each database.

### Customers

```text
GET /api/customers
POST /api/customers
PUT /api/customers/{customer_id}
DELETE /api/customers/{customer_id}
```

### Vehicles

```text
GET /api/vehicles
POST /api/vehicles
PUT /api/vehicles/{vehicle_id}
DELETE /api/vehicles/{vehicle_id}
```

### Services

```text
GET /api/services
POST /api/services
PUT /api/services/{service_id}
DELETE /api/services/{service_id}
```

The backend also provides a health check endpoint:

```text
GET /api/health
```

---

## Project Structure

```text
data_intensive_A2/
│
├── README.md
├── .gitignore
│
├── backend/
│ ├── .env.example
│ ├── requirements.txt
│ ├── seed.py
│ │
│ └── app/
│ ├── __init__.py
│ ├── database.py
│ ├── models.py
│ ├── schemas.py
│ └── main.py
│
└── frontend/
├── package.json
├── package-lock.json
├── vite.config.js
│
└── src/
├── main.jsx
├── App.jsx
├── api.js
└── index.css
```

The Python virtual environment, Node.js dependencies and environment variables are excluded from Git using `.gitignore`.

---

# Installation

## Prerequisites

Install the following software before running the project:

- Python
- PostgreSQL
- Node.js and npm
- Git

pgAdmin 4 can be used to manage and inspect the PostgreSQL databases.

---

## 1. Create the PostgreSQL Databases

Create the following three databases:

```sql
CREATE DATABASE customers_db;
```

```sql
CREATE DATABASE vehicles_db;
```

```sql
CREATE DATABASE services_db;
```

The commands should be executed separately.

---

## 2. Backend Setup

Open a terminal in the project directory and navigate to the backend:

```powershell
cd backend
```

Create a Python virtual environment:

```powershell
python -m venv .venv
```

Activate the virtual environment in PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

If above script does not run in your terminal, you might need to change your ExecutionPolicy temporarely
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Install the Python dependencies:

```powershell
python -m pip install -r requirements.txt
```

---

## 3. Configure Database Connections

Create a file named:

```text
backend/.env
```

Use `backend/.env.example` as the template.

Example:

```env
CUSTOMERS_DATABASE_URL=postgresql+psycopg://postgres:YOUR_PASSWORD@localhost:5432/customers_db
VEHICLES_DATABASE_URL=postgresql+psycopg://postgres:YOUR_PASSWORD@localhost:5432/vehicles_db
SERVICES_DATABASE_URL=postgresql+psycopg://postgres:YOUR_PASSWORD@localhost:5432/services_db
```

Replace:

```text
YOUR_PASSWORD
```

with the password of the local PostgreSQL user.

The `.env` file is excluded from Git and should not be committed because it contains database credentials.

---

## 4. Create the Database Tables

The SQLAlchemy models define the database tables used by the application.

The required tables are:

```text
customers_db
└── customers

vehicles_db
└── vehicles

services_db
└── service_records
```

The application uses the SQLAlchemy models in the backend to represent these tables.

---

## 5. Add Dummy Data

The project contains a seed script:

```text
backend/seed.py
```

Run it from the backend directory:

```powershell
python seed.py
```

The script creates example data for:

- Customers
- Vehicles
- Service records

The dummy data can be used to test the application.

---

## 6. Start the Backend

From the backend directory with the virtual environment activated:

```powershell
uvicorn app.main:app --reload
```

The FastAPI backend will run locally on port `8000`.

FastAPI's interactive API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

The API documentation can be used to test the CRUD endpoints directly.

---

## 7. Frontend Setup

Open another terminal and navigate to the frontend directory:

```powershell
cd frontend
```

Install the frontend dependencies:

```powershell
npm install
```

Start the Vite development server:

```powershell
npm run dev
```

If PowerShell prevents the npm PowerShell script from running, the corresponding command can be run using:

```powershell
npm.cmd run dev
```

Vite will display the local address of the frontend in the terminal.

---

# Running the Application

The application requires both the backend and frontend to run.

## Terminal 1 - Backend

```powershell
cd backend
.\.venv\Scripts\Activate.ps1
uvicorn app.main:app --reload
```

## Terminal 2 - Frontend

```powershell
cd frontend
npm run dev
```

The architecture during development is:

```text
Browser
|
v
React / Vite
localhost:5173
|
| /api/*
v
Vite Proxy
|
v
FastAPI
127.0.0.1:8000
|
v
SQLAlchemy
|
v
PostgreSQL
localhost:5432
```

---

# Using the Application

The application provides three database selections:

```text
Customers
Vehicles
Services
```

Selecting a database loads its records into the table.

For each database the user can:

### Add

Fill in the form and select:

```text
Add Record
```

### Edit

Select:

```text
Edit
```

next to a record.

The selected data is loaded into the form.

After editing the values, select:

```text
Save Changes
```

### Delete

Select:

```text
Delete
```

next to a record.

The application asks for confirmation before deleting the record.

### Refresh

Select:

```text
Refresh
```

to reload the currently selected database.

---

# Dummy Data

The seed data contains example:

- Customers
- Vehicles belonging logically to customers
- Service records belonging logically to vehicles

This provides enough sample data to demonstrate the functionality of all three databases.

---

# Security

Database passwords are stored locally in:

```text
backend/.env
```

This file is excluded through `.gitignore`.

Only the example file:

```text
backend/.env.example
```

should be committed to the repository.

The following directories are also excluded from Git:

```text
backend/.venv/
frontend/node_modules/
frontend/dist/
```

Dependencies can instead be recreated using:

```text
backend/requirements.txt
frontend/package.json
frontend/package-lock.json
```

---

# Author

joonasaf

