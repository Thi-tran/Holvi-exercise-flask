
## Tips to get started

Install python in your system.

Install virtualenv for python https://pypi.python.org/pypi/virtualenv. This
step is optional but recommended, since it won't make available globally Flask
to your system, but only for this project. If not using virtualenv you can just
run:

    easy_install Flask

or

    pip install Flask

If using virtualenv, create a virtual environment in the cloned project folder.
Call it `env`:

    virtualenv env

Activate the virtual environment you will have to do this every time you get
back to the project:

    source env/bin/activate

Install the dependencies for the project:

    pip install -r requirements.txt

to run the app just do

    python app.py

the Flask server (in debug mode) will be running in port 5000. It loads in
its root the base HTML file to build on.

Install bower dependencies

    bower install

All yours, have fun!

