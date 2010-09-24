Introduction
============

Grab source:

    git clone git@github.com:gandalfar/ivotecoz.git

Create Python virtual environment and activate it:

    cd ivotecoz
    virtualenv --no-site-packages --python=/usr/bin/python2.6 .
    source bin/activate

Install dependencies:

    python setup.py develop

Copy over default settings:

    cd ivotecoz
    cp localsettings.py.example localsettings.py
    
Create the (default is Sqlite3) database:

    ./manage.py syncdb

Start the development server:

    ./manage.py runserver

