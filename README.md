# Minimal Flask Blueprint

There are a number of Flask[^1] tutorials on the web.
I want a minimal flask project to explore web application development using blueprints.
A blueprint encapsulates routes, templates, static files, and other logic.
While Flask states it "doesn't enforce any dependencies or project layout", a good layout avoids a number of problems people experience as an application gets larger.

## Nothing But Flask

There are any number of posts about setting up a flask app.
However, they all seem to have too much of what I don't want, need, or know how to use.
I want to be mindful of what I use and how I can integrate or replace various extensions.
So, we will start simple using only the Python standard library and Flask.

## Project Directory Layout

We are going to follow best practice and use packages to organize code.
It will include:
- **venv/** the python virtual environment.
- **webapp/**, a Python package for our code.
- **wsgi.py**, a file for flask command line integration.

### Create Your Project Directory
Create a project directory. Call it anything you want.
Need a little inspiration? Try something from https://online-generator.com/name-generator/project-name-generator.php and see if you like it.
I will use `basic-blue-flask` and you will find the repository at https://github.com/jidn/basic-blue-flask .

```bash
$ mkdir basic-blue-flask
$ cd basic-blue-flask
```

### Install Python Virtual Environment

Keeping with our minimalist approach, we will create our virtual environment without other helper tools.
Actually, this is one of my favorite ways to create virtual environment.
If anything goes wrong, just delete the virtual environment directory and run these steps again.
Once created, enter the environment so we can install Flask.

```bash
$ python -m venv venv
$ source venv/bin/activate
(venv)$ printenv VIRTUAL_ENV
/home/.../basic-blue-flask/venv
```

For our friends on Windows using Powershell
```powershell
PS > python -m vnv venv
PS > .\venv\Scripts\Activate.ps1
```

With our virtual environment active, install Flask.

```bash
(venv)$ pip install flask
```

### Package: `webapp`

First, an overview of the file structure.
```
webapp
├── __init__.py
├── app.py
├── blueprints
│   ├── __init__.py
│   └── main
│       └── __init__.py
└── cli
    ├── __init__.py
    └── test_cli.py
```
The existance of the file `webapp/__init__.py` makes Python treat the directory as a package and has no content.

[//]: # (Select text between fenced code in vim with  "v/```/e" k$dk to delete.
    Place cursor at beginning of fence and read external file
    :read filename or :r filename
    Need to find you current directory? :!pwd
)
`webapp/app.py` contains a single function to create our Flask application.

```python
"""Flask app factory function."""
from flask import Flask
from webapp.cli import register_commands
from webapp.blueprints import register_blueprints

def create_app():
    """An application factory.
    """
    app = Flask(__name__, static_folder=None)

    # Hook everything up
    register_commands(app)
    register_blueprints(app)
    return app
```

The `create_app` function is commonly called an [application factory](https://flask.palletsprojects.com/en/1.1.x/patterns/appfactories/).
It's sole purpose is to create a Flask application with different possible configurations.
Different configurations aid in testing and production scenarios.

Many other examples, including the Flask documentation, import individual extensions and configure them in the method.
I recommend we create a module for each of the major application functionality and just call a register function there.
We will examine this closer in just a few paragraphs, but I wanted to point it out here.

Look at where we "Hook everything up".
Instead of importing individual cli-commands, blueprints, and eventually extensions in this function, we use a package and keep this clutter free.

Blueprints
----------

`webapp/blueprints` is our package for keeping the applications blueprints.
For the moment we will have only a main package with 'Hello World blueprint.
Looking at the below code is should look very similar to Flask's [minimal application](https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application) except we are using a `flask.Blueprint` instead of a Flask application.

`webapp/blueprints/main/__init__.py`
```python
from flask import Blueprint
blueprint = Blueprint("main", __name__)

@blueprint.route("/")
def HelloWorld():
    return "Hello World!"
```

Now, let's look at the `webapp/blueprint/__init__.py` and it is here we will hook up the blueprint.
```python
"""Import all `flask.Blueprint` modules.
"""
from . import main

def register_blueprints(app):
    """Register blueprints on application."""
    app.register_blueprint(main.blueprint)
```

## CLI Command Line Interface

The flask application has three commands by default: `routes`, `run`, and `shell`.
We will add another command to test the `main` blueprint is working and giving the correct response.
The package layout is similar to that of `blueprints`, an `register_commands` function to load all the commands.
Here is the `cli/__init__.py` file.

```python
"""Additional `flask` command-line options.
"""
from .test_cli import testing

def register_commands(app):
    """Register `Click` commands with flask app."""
    app.cli.add_command(testing)
```
And here is the contents of the `cli/test_ci.py` file.

```python
"""Add test to Flask command line
"""
import click

@click.command()
def test():
    """Run application tests."""
    from webapp.app import create_app

    client = create_app().test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b"Hello World!"
    print("Passed tests")
```

## Running the Application

For the command `flask run` to work it needs to know where the application exists.
One way is to define an environment variable `FLASK_APP`.  This is the method taught by the [Flask documentation](https://flask.palletsprojects.com/en/1.1.x/tutorial/factory/#run-the-application).
However, I want to use a different way to start Flask.
When a file named `wsgi.py` is in the directory root, Flask will look for an object named `app` and use that object.

```python
"""The webapp Flask instance."""
from webapp.app import create_app

app = create_app()
```

Now that we have all the pieces in place, let's try them out.

```
$ flask
Usage: flask [OPTIONS] COMMAND [ARGS]...

  A general utility script for Flask applications.

  Provides commands from Flask, extensions, and the application. Loads the
  application defined in the FLASK_APP environment variable, or from a
  wsgi.py file. Setting the FLASK_ENV environment variable to 'development'
  will enable debug mode.

    $ export FLASK_APP=hello.py
    $ export FLASK_ENV=development
    $ flask run

Options:
  --version  Show the flask version
  --help     Show this message and exit.

Commands:
  routes  Show the routes for the app.
  run     Run a development server.
  shell   Run a shell in the app context.
  test    Run application tests.
```

Have Flask run this application and check the output at http://localhost:5000

That is it for today.  We have a basic, blueprint Flask application using nothing but Flask and the standard library.

## Footnotes

[^1]: [Flask Documentation](https://flask.palletsprojects.com/)
