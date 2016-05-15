# Corrosive-the-punk-rooster-

## Start the project

Really, we don't know about the reason of the project

## To start install Virtualenv
    
```bash
    $ pip install virtualenv
    $ virtualenv Corrosive
    $ source bin/activate 
    # (In windows maybe is not inside of bin directory ej. venv\Scripts\activate.bat or something)
    $ pip install -r requirements.txt
```
To add new libraries please add to the requirements.txt just like that:
    
```bash
    $ pip freeze > requirements.txt
```
## To create and run migrations
    
If you change something in the models, make migrations and run again.
```bash
    $ python manage.py makemigrations 
```
```bash
    $ python manage.py migrate
```

## To create a superuser and run

```bash
    $ python manage.py createsuperuser
    $ python manage.py runserver
```
## Gulp

Install Node
    https://nodejs.org/en/
    
 ```bash 
    $ npm init
    $ npm install gulp -g
    Agregar (node_modules/.bin/ en $Path) Windows
    $ npm i -D gulp
    $ npm install stylus -g
    $ npm i -D gulp-webserver
    $ npm i -D gulp-stylus
    $ npm i -D nib
    $ npm i -D gulp-minify-css
    $ npm i -D browserify
    $ npm i -D vinyl-source-stream
    $ npm i -D vinyl-buffer
    $ npm i -D gulp-uglify
    $ npm i -D gulp-image-optimization
    $ npm i -D gulp-smoosher

    #Run 
    $ gulp build:js
    $ gulp
``` 

## Add browserSync (to solve gulp issues)

```bash
    npm install browser-sync --save
```
```bash

    # add to gulfile.js
    $ var browserSync = require("browser-sync")

    # and
    $ browserSync.init({
    $ host: "0.0.0.0",
    $ notify: false,
    $ port: 8080,
    $ server: {
        baseDir: ['User/templates/User', 'app']
        },
    });
```
## Integrate Djago + Gulp

Add "django_gulp" to your INSTALLED_APPS

```bash
    sudo pip install django_gulp"
```