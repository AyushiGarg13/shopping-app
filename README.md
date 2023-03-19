# Shopping App
Shopping App is a mini learning project. It is a REST API application with features to add items, stores, tags and users.


## Built With

* [![Python](https://img.shields.io/badge/python-3.11-brightgreen)](https://docs.python.org/3/)
* [![Flask](https://img.shields.io/badge/flask-v2.2.2-blue)](https://flask.palletsprojects.com/en/2.2.x/)


## Requirements

This application requires the following python libraries:

- marshmallow
- flask
- flask-smorest
- python-dotenv
- SQLAlchemy
- Flask-SQLAlchemy
- flask-jwt-extended
- passlib
- flask-migrate
- gunicorn
- psycopg2
- requests
- rq
- redis


## Installation

1. Clone the repo
   ```sh
   git clone https://github.com/AyushiGarg13/first_app.git
   ```
2. Install python libraries
   ```sh
   pip install -r requirements.txt
   ```
3. Build the docker image and run it to start the application.


## Configuration

To run the application locally, .env file must be created at the root folder with following details:

1. DATABASE_URL: PostgreSQL as a Service, [_ElephantSQL_](https://www.elephantsql.com/)
2. MAILGUN_API_KEY: Generated using [_Mailgun_](https://www.mailgun.com/)
3. MAILGUN_DOMAIN: Provided by [_Mailgun_](https://www.mailgun.com/)
4. REDIS_URL: Used service provided by [_Render_](https://render.com/) 


## Acknowledgments

This project was built entirely by following the Udemy Course [REST APIs with Flask and Python](https://www.udemy.com/course/rest-api-flask-and-python/). 

![image](https://d3f1iyfxxz8i1e.cloudfront.net/courses/course_image/1b20b2e41ed4.jpg)

This course has been very helpful in understanding the concepts of REST APIs and building it with Flask and Python. I recommend this course to everyone who wants to start out with their journey of REST API development.