# Corrosive-the-punk-rooster-

## Start the project

Really, we don't know about the reason of the project

## To start install Virtualenvv
    
    pip install virtualenv
    virtualenv Corrosive
    source bin/activate (In windows maybe is not inside of bin directory 
        ej. venv\Scripts\activate.bat or something)
    pip install -r requirements.txt

To add new libraries please add to the requirements.txt just like that:
    
    pip freeze > requirements.txt

## To run migrations
    
    python manage.py migrate

If you change something in the models, make migrations and run again.

    python manage.py makemigrations 
