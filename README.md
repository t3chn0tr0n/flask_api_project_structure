# flask_project_structure

## To run for the first time

### Step 0: Get folder

Clone: `git clone <link>`

Goto dir: `cd <dir>` or maybe inside project workspaces if you want individual venvs for each project!

### Step 1: Create virtual environment

`python -m virtual venv`

### Step 2: Start virtual environment

Windows: `venv\Scripts\activate`

Linux: `source\bin\activate`

### Step 3: Install Requirements

`pip install -r requirements.txt`

## Run the flask app

**Note**: Must be inside the folder where `run.py` is visible!

### Set env

Windows: `set FLASK_APP=run.py` (Powershell will not work out-of-the-box. Use cmd!)

Linux: `export FLASK_APP=run.py`

### Run

`flask run`

Optional parameters: [Use `flask run <params1> <params2> <params3>`]

- `-h 0.0.0.0` : sets host to 0.0.0.0
- `-p 9876` : sets port to 9876 (use any valid port)
- `--with-threads` : use multi-threading
- `--help` : more useful options

## Install DB Requirements

- For sql:

  - MySQl: `mysql`
  - Postgres: `psycopg2`

- For Mongo: `pymongo`

And then update `requirements.txt`

## Update requirements.txt if new packages are installed

`pip freeze > requirements.txt`

**Note**: NEVER EVER update the requirements.txt manually!F
