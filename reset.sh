#!/bin/sh

rm db.sqlite
rm -rf stache/migrations
python manage.py schemamigration stache --initial
python manage.py syncdb --noinput
python manage.py migrate stache
python manage.py loaddata stache/fixtures/admin.yaml
#python manage.py loaddata stache/fixtures/arch.yaml
