# create_flask_structure
Creating new flask project tree with user input (project name and port number)


# Project Structure
```
my_flask_app/
│
├── app/
│   ├── __init__.py
│   ├── main/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── templates/
│   │       └── main/
│   │           └── index.html
│   │           └── other_template.html
│   │   └── static/
│   │       └── main/
│   │           └── style.css
│   │           └── script.js
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── templates/
│   │       └── auth/
│   │           └── login.html
│   │           └── register.html
│   │   └── static/
│   │       └── auth/
│   │           └── style.css
│   │           └── script.js
│   ├── models.py
│   ├── forms.py
│   ├── config.py
│   └── extensions.py
│
├── migrations/
│
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   └── test_auth.py
│
├── venv/
│
├── .flaskenv
│
├── .gitignore
│
├── README.md
│
└── run.py
```


You can change Project Name from create file.

# .flaskenv inside 
```
FLASK_APP=run.py
FLASK_ENV=development
```

# .gitignore inside 
```
  venv/
  *.pyc
  __pycache__/
  instance/
  .webassets-cache
```
