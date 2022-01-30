# python-entsoefacade

My first Django project

## Scaffolding

```bash
django-admin startproject entsoefacade .
cd entsoefacade
django-admin startapp transmission
cd ..
```

## DB migration

```bash
python manage.py makemigrations transmission
python manage.py migrate
```

## Test

```bash
python manage.py test
```

## Run

```bash
cp sample.env .env # edit as you see fit
set -a && . .env && set +a
python manage.py runserver
```

HTML:
http://localhost:8000/transmissions/

JSON:
http://localhost:8000/v1/transmissions/cross_border_flows/?from=NL&to=DE&start=20220101&end=20220201
