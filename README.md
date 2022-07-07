# fast-api

## Basic Installation and setup
- https://www.youtube.com/watch?v=Wr1JjhTt1Xg
- Create a venv - `python3 -m venv venv-fastapi`
- Access the venv - `source venv-fastapi/bin/activate`
- Install below dependencies:
  - Fast API module - `pip install fastapi`
  - Server to run the API - `pip install uvicorn`
- Create a `main.py` file in folder current folder. (Not insid the fastapi venv folder.)
- Follow the code in the video and run the below command to run the server.
- To run the code - `uvicorn main:app --reload`

## FASTAPI with PostgreSQL and SQLAlchemy
- FASTAPI framework for API development. 
- UVICORN will be our Asynchronous Server Gateway Interface.
- SQLAlchemy will be used for ORM.
- psycopg2 is a postgres driver.
- ALEMBIC is a lightweight database migration tool for usage with the SQLAlchemy Database Toolkit for Python.
- To install all the dependencies - `pip install -r requirements.txt`
- 
