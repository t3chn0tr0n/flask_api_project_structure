# flask_project_structure

My take on writing flask APIs and micro-services.
This repo is a boilerplate for writing flask restful APIs.
Includes:

1. A proper way to separate configs in Production, Development and Testing
2. SQL Alchemy build-in, with CRUD operations
3. Email service configured
4. Password and Token Authentication handled using Argon2 and PyJWT
5. Pymongo functions written to do basic CRUD operations

i.e. most of the boring stuff done in one place!

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

**Note**: NEVER EVER update the requirements.txt manually!

## Understating the Project structure

### A few Topics that should be cleared out before hand

This things are sometimes called advanced topics in Python/Flask/Web-dev in general, so people usually don't include them in
beginner courses and tutorials. But going thought these helped me understand a lot!

(Btw, if you are new to python, heres a book: [Python for you and me](https://pymbook.readthedocs.io/en/latest/)

#### Modules, Packages and Imports in Python

- Absolute vs Relative Imports in Python
  [Realpython article](https://realpython.com/absolute-vs-relative-python-imports/)
- Python Modules and Packages [Realpython article](https://realpython.com/python-modules-packages/)

#### Password hashing and Argon 2

Argon2 is a password hashing algorithm. I used `argon2-cffi` - a python library that implements that
algorithm with a simple way to use it!

- Why Hash Passwords and technologies involved!
  [Auth0 Blog](https://auth0.com/blog/hashing-passwords-one-way-road-to-security/)
- Basic Knowledge: [argon2-cffi docs](https://argon2-cffi.readthedocs.io/en/stable/)
- Detailed Algorithm [here](https://github.com/P-H-C/phc-winner-argon2/blob/master/argon2-specs.pdf)

#### Authentication and JWT Tokens

- Most Used Rest-api Authentication Types and where to use what
  [Restcase article](https://blog.restcase.com/4-most-used-rest-api-authentication-methods/)
- JWT Introduction: [JWT.io](https://jwt.io/introduction/)
- JWT Detail Read: [Auth0 docs](https://auth0.com/docs/tokens/json-web-tokens)
- [PyJWT docs](https://pyjwt.readthedocs.io/en/latest/)

#### Python and concurrency/parallelism

Python is different from most other languages, we all agree, but when it comes to concurrency, well,
let's say its most different!

Although this repo has not implemented any async methods, since you learned all those above topics,
why leave this!

- Thread vs Process: [GeeksForGeeks](https://www.geeksforgeeks.org/difference-between-process-and-thread/)
- Python's GIL: [Realpython article](https://realpython.com/python-gil/) and/or
  [Python wiki](https://wiki.python.org/moin/GlobalInterpreterLock)
- Thread vs Process in python: [medium @bfortuner's blog](https://medium.com/@bfortuner/python-multithreading-vs-multiprocessing-73072ce5600b)
- Also look in python [threading module](https://docs.python.org/3.8/library/threading.html) and
  [multiprocessing module](https://docs.python.org/3.8/library/multiprocessing.html)

### A few general things

- Functions solving 1 problem are grouped in a File.

- Files solving similar problem are in a folder.

- `project_root` is a placeholder. It can be safely renamed to anything. To achieve this flexibility,
  most of the code inside uses relative imports. Therefore **_Do Not move folders around blindly_**.

- Once copied for your project, make sure to edit this `README.md`. Always write a detailed README,
  it is useful for newcomers to the project!

more doc will be added...
