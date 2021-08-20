# dandi-api

## Develop with Docker (recommended quickstart)
This is the simplest configuration for developers to start with.

### Initial Setup
1. Run `docker-compose run --rm django ./manage.py migrate`
2. Run `docker-compose run --rm django ./manage.py createsuperuser`
   and follow the prompts to create your own user.
   Set your username to your email to ensure parity with how GitHub logins work.
3. Run `docker-compose run --rm django ./manage.py create_dev_dandiset --owner your.email@email.com`
   to create a dummy dandiset to start working with.

### Run Application
1. Run `docker-compose up`
2. Access the site, starting at http://localhost:8000/admin/
3. When finished, use `Ctrl+C`

### Application Maintenance
Occasionally, new package dependencies or schema changes will necessitate
maintenance. To non-destructively update your development stack at any time:
1. Run `docker-compose pull`
2. Run `docker-compose build --pull --no-cache`
3. Run `docker-compose run --rm django ./manage.py migrate`

## Develop Natively (advanced)
This configuration still uses Docker to run attached services in the background,
but allows developers to run Python code on their native system.

### Initial Setup
1. Install [Docker](https://docs.docker.com/engine/install/) and [Docker Compose](https://docs.docker.com/compose/install/)
2. Run `docker-compose -f ./docker-compose.yml up -d`
3. Install Python 3.8
4. Install
  [`psycopg2` build prerequisites](https://www.psycopg.org/docs/install.html#build-prerequisites).
  Example `psycopg2` installation on Ubuntu 20.04:
  ```
  sudo apt install libpq-dev
  export PATH=/usr/lib/postgresql/X.Y/bin/:$PATH
  pip install psycopg2
  ```
5. Create and activate a new Python virtualenv
6. Run `pip install -e .[dev]`
7. Run `source ./dev/export-env.sh`
8. Run `./manage.py migrate`
9. Run `./manage.py createsuperuser` and follow the prompts to create your own user
3. Run `./manage.py create_dev_dandiset --owner your.email@email.com`
   to create a dummy dandiset to start working with.

### Run Application
1.  Ensure `docker-compose -f ./docker-compose.yml up -d` is still active
2. Run:
   1. `source ./dev/export-env.sh`
   2. `./manage.py runserver`
3. Run in a separate terminal:
   1. `source ./dev/export-env.sh`
   2. `celery --app dandiapi.celery worker --loglevel INFO --without-heartbeat`
4. When finished, run `docker-compose stop`

## Remap Service Ports (optional)
Attached services may be exposed to the host system via alternative ports. Developers who work
on multiple software projects concurrently may find this helpful to avoid port conflicts.

To do so, before running any `docker-compose` commands, set any of the environment variables:
* `DOCKER_POSTGRES_PORT`
* `DOCKER_RABBITMQ_PORT`
* `DOCKER_MINIO_PORT`

The Django server must be informed about the changes:
* When running the "Develop with Docker" configuration, override the environment variables:
  * `DJANGO_MINIO_STORAGE_MEDIA_URL`, using the port from `DOCKER_MINIO_PORT`.
* When running the "Develop Natively" configuration, override the environment variables:
  * `DJANGO_DATABASE_URL`, using the port from `DOCKER_POSTGRES_PORT`
  * `DJANGO_CELERY_BROKER_URL`, using the port from `DOCKER_RABBITMQ_PORT`
  * `DJANGO_MINIO_STORAGE_ENDPOINT`, using the port from `DOCKER_MINIO_PORT`

Since most of Django's environment variables contain additional content, use the values from
the appropriate `dev/.env.docker-compose*` file as a baseline for overrides.

## Testing
### Initial Setup
tox is used to execute all tests.
tox is installed automatically with the `dev` package extra.
To install the tox pytest dependencies into your environment, run `pip install -e .[test]`.
These are useful for IDE autocompletion or if you want to run `pytest` directly (not recommended).

When running the "Develop with Docker" configuration, all tox commands must be run as
`docker-compose run --rm django tox`; extra arguments may also be appended to this form.

### Running Tests
Run `tox` to launch the full test suite.

Individual test environments may be selectively run.
This also allows additional options to be be added.
Useful sub-commands include:
* `tox -e lint`: Run only the style checks
* `tox -e type`: Run only the type checks
* `tox -e test`: Run only the pytest-driven tests
* `tox -e test -- -k test_file`: Run the pytest-driven tests that match the regular expression `test_file`
* `tox -e test -- --cov=dandiapi`: Generate a test coverage report
* `tox -e test -- --cov=dandiapi --cov-report=html`: Generate an HTML test coverage report in the `htmlcov` directory

To automatically reformat all code to comply with
some (but not all) of the style checks, run `tox -e format`.

## API Authentication
Read-only API endpoints (i.e. `GET`, `HEAD`) do not require any
authentication. All other endpoints require token authentication
to call.

### Creating a Token
Visit the URL `/admin` with a web browser, logging
in with the credentials entered during the `createsuperuser` setup step..
Then go to `/swagger` and use `GET /auth/token` end-point.

### Supplying the Token
In API endpoint calls, add the `Authorization` HTTP header with a value of
`Token <token_value>`. For example, for a token `1234`, include the header:
`Authorization: Token 1234`.
