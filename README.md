# TrainingDjango
A small project written in Python- Django which performs CRUD operations on models with a decent user interface.This maintainsa friend directory with featuresl like adding , updating, deleting a friend in the directory.

## Prerequisites

- [Django](https://www.djangoproject.com/)
- [MySQL](https://www.mysql.com/)

## Installation
- Create a virtual environment
    ```bash
     virtualenv -p python3 foldername
    ```
- Activate the virtual environment
    ```bash
    source bin/activate
    ```
- Run the flask server
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    ```
- Hit the url `http://localhost:8000/`