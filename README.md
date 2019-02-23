**_A Basic TODO app using Python,Django and JavaScript._**
Using this we can create ToDO list,mark it as complete,Delete completed items and Delete all list items.

**_Home Page_**
![Index Page](https://github.com/gautamp25/todo_app/blob/master/index.png)



**Create Virtual Environment in Windows**
1.virtualenv name-env 
2.name-env\Scripts\activate.bat
3.pip install django
4.django-admin startproject name-pro
5.cd name-pro
6.python manage.py runserver

------------------
**Create Virtual Environment in Ubuntu**
1.Make new folder
2.change directory cd folder_name
3.virtualenv -p python3 .
4.source bin/activate
5.django-admin startproject name-pro
6.cd name-pro
7.python manage.py runserver

**CREATE SUPERUSER**
1.python manage.py createsuperuser

**CREATE APP**
1.python manage.py startapp app_name

**MIGRATIONS**
1.python manage.py makemigrations
2.python manage.py migrate
