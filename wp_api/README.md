# Welcome!

## I'd like to welcome you in my WebApp API project.

It's an easy web application made with Django Framework. 
Main functionality is to collect personal information from a user with forms, store it to the database and serialize it with Django Rest Framework just to create an API.
Everyone can submit their information but only authorized users can see them. 
What is more, **JSON Web Token** is also used here (what you can see in the settings or using Postman/Thunder Client).

#### Authorized users can be added in the admin panel only by the superuser. 

## Turning on this app:
- clone this repository
- go to wp_api folder (on the same level as *.gitignore*), which is the main project folder
- type in the terminal **python manage.py runserver**
- enjoy!


If you want to see collected data in the API use **login**: personel and the **password**: working1234.


##### P.S
This app is made with db.sqlite3 database, but was tested on PostgreSQL database (what you can see in the settings) also.


