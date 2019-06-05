#!/bin/bash
zappa update production
zappa manage production migrate
zappa manage production "collectstatic --noinput"