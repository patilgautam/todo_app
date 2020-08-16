# TODO APP

**_A Basic TODO app using Python,Django and JavaScript._**
Using this we can create ToDO list,mark it as complete,Delete completed items and Delete all list items.

**_Home Page_**
![Index Page](https://github.com/gautamp25/todo_app/blob/master/index.png)


## Getting Started - Local Development

*Clone the project*

`git clone https://github.com/gautamp25/todo_app.git`

---

**How to Create Virtual Environment in Windows**

*1. Create virtual environment*

`virtualenv myenv`

*2. Activate virtual environment*

`myenv\Scripts\activate.bat`

*3. Insatll Django*

`pip install django`

*4. Create project*

`django-admin startproject django-pro`

`cd django-pro`

*5. Run project*

`python manage.py runserver`

---

**How to Create Virtual Environment in Ubuntu**

*1. Make new folder*

`mkdir python-project`

`cd python-project`

*2. Create virtual environment*

`virtualenv -p python3`

*3. Activate virtual environment*

`source bin/activate`

*4. Create project*

`django-admin startproject django-pro`

`cd name-pro`

*5. Run project*

`python manage.py runserver`

---

**CREATE SUPERUSER**

`python manage.py createsuperuser`

*CREATE APP*

`python manage.py startapp app_name`

*MIGRATIONS*

`python manage.py makemigrations`

`python manage.py migrate`
