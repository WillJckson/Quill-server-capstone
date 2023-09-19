#!/bin/bash

rm db.sqlite3
rm -rf ./Quillapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations Quillapi
python3 manage.py migrate Quillapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python3 manage.py loaddata profiles
python3 manage.py loaddata quote_categories
python3 manage.py loaddata quotes