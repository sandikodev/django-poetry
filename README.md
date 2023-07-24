# OPINIONATE DJANGO AS YOU GO

## caution
this boilerplate is'nt designated as frontend yet, just REST API [backend]!!

## how to start this project
1. clone project\
    `git clone git@github.com:sandikodev/django-poetry.git`
2. install the requirement\
    a. pyenv (optional): is python version manager\
        `https://github.com/pyenv/pyenv`\
    b. poetry (required): is python dependence manager\
        `https://github.com/python-poetry/install.python-poetry.org`
3. change to project directory\
    `cd django-poetry`
4. install dependence with poetry\
    `poetry install --no-root`
5. activate virtual environment\
    `poetry shell`
6. start django web services\
    `python manage.py runserver`
7. init app (example)\
    a. `python manage.py startapp hello_example_app`\
    b. dont forget register your app to Django ASGI Webservices right after!

## how to deploy this project to fly.io
1. [first follow how to start development with this project](#how-to-start-this-project)
2. install fly.io cli as requirement\
    `https://fly.io/docs/hands-on/install-flyctl`
3. login fly.io cli\
    `fly auth login`
4. init `Dockerfile` and `fly.toml`\
    `fly launch`
5. push `Image` based on created `Dockerfile` to cloud `fly.io`\
    `fly deploy`
6. visit app with command below\
    `fly open`

## what's going on behind this project
1. install python\
    `pyenv install 3.11.4`
2. initiate python version for specific dir project\
    `pyenv local 3.11.4`
3. initiate package dependence manager with poetry\
    `poetry init`
4. after `poetry add <package name>`. update dependences package as you go\
    `poetry update`
5. initiate django project based on `src` dir\
    `poetry run django-admin startproject src`
6. initiate superuser\
    `poetry run python manage.py createsuperuser`
7. migrate django based on specific python shell project\
    `poetry run python manage.py migrate`
8. run every single command on top of python shell environment without `poetry run`\
    `poetry shell`\
    `which python`
9. run server\
    `poetry run python manage.py runserver`
10. export `requirements.txt` (optional)\
    `poetry export -f requirements.txt --output requirements.txt`

## roadmap
1. container\
   a. IAAS: fly.io compatible\
   b. docker-compose

## reference
https://proxyroot.com/django-poetry/

