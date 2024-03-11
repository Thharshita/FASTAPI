# Python API with FastAPI 
This repository contains a series of Python files that serve as a guide for mastering FastAPI, a fast and modern web framework for building APIs with Python.

## Overview

FastAPI is a tool that helps developers create web applications with Python really quickly.
It's especially good at handling lots of requests at the same time, so it's fast. 
It's also easy to use because it gives you helpful tools to make sure your code works properly and documents it automatically.

Please visit file in following order:
## Project Structure

- `basic.py`: Introduces the basics of creating a FastAPI application. It covers setting up a FastAPI instance, defining routes for handling GET and POST requests, and demonstrating simple route implementations.
- `bestpractice.py`: Demonstrates best practices for implementing CRUD (Create, Read, Update, Delete) operations in FastAPI. It uses a hardcoded Python list as a database. There's a Pydantic model named Post representing the structure of a post, which includes fields for title, content, and published status.
- `status.py`: Explores how to handle exceptions gracefully using HTTPException in FastAPI. Different HTTP status codes are demonstrated to handle various scenarios effectively.
- `app.py`: The application connects to a PostgreSQL database using psycopg2.This code utilizes psycopg2 directly for database operations, which involves writing and executing raw SQL queries. 
To run any of the files locally, ensure you have Python installed on your machine. You can install the necessary dependencies by executing:
- `app2.py`: Instead of dealing directly with SQL queries like in `app.py`, here we use SQLAlchemy, a Python library that simplifies working with databases. SQLAlchemy lets us interact with our database using Python objects  providing a higher level of abstraction, making our code cleaner and easier to maintain.

Install FastApi
```bash
pip install fastapi
```
To run your application: 
```bash
uvicorn basic:app --relaod  #if u r executing basic file
```
To connect to Postgress database , install driver psycopg2: 
```bash
pip install psycopg2
```
To use SqlAlchemy : 
```bash
pip istall sqlalchemy

```

