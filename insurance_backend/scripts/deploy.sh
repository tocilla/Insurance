#!/bin/bash
python manage.py collectstatic --noinput
zappa update production
zappa manage production migrate