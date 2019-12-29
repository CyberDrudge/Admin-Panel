# Admin-Panel
A simple panel for admins to checkout all users.

**Setup Build Environment**

Create a virtual environment:

```virtualenv .```

Clone this repository:

```git clone <url>```

```cd Admin-Panel```

Install requirements:

```pip install -r requirements.txt```

Create Migrations:

```python manage.py makemigrations```

```python manage.py migrate```

Create a superuser or Admin:

`python manage.py createsuperuser`



**Run**

```python manage.py runserver```

Open `localhost:8000` on your browser to view.

 
