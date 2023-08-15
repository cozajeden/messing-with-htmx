# Messing with htmx

This is a project to learn how to use htmx.<br>
I will be using Django as the backend.

## How to run in virtual environment

1. Clone the repo
2. Create a virtual environment
3. Install the requirements
4. Run the server

```bash
git clone
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

## How to run in Docker

1. Clone the repo
2. Build and run the image

```bash
git clone
docker-compose -f docker-compose-dev.yml up -d
```

