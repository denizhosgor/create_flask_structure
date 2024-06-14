import os

def create_flask_project_structure(project_name):
    # Define the directory structure
    dirs = [
        f"{project_name}/app",
        f"{project_name}/app/main",
        f"{project_name}/app/main/templates/main",
        f"{project_name}/app/main/static/main",
        f"{project_name}/app/auth",
        f"{project_name}/app/auth/templates/auth",
        f"{project_name}/app/auth/static/auth",
        f"{project_name}/migrations",
        f"{project_name}/tests",
        f"{project_name}/venv"
    ]

    # Create the directories
    for dir in dirs:
        os.makedirs(dir, exist_ok=True)
    
    # Define the files to be created with their initial content
    files = {
        f"{project_name}/app/__init__.py": "# app/__init__.py\nfrom flask import Flask\n\napp = Flask(__name__)\n\nfrom app.main import routes\nfrom app.auth import routes",
        f"{project_name}/app/main/__init__.py": "# app/main/__init__.py\nfrom flask import Blueprint\n\nmain = Blueprint('main', __name__)\n\nfrom app.main import routes",
        f"{project_name}/app/main/routes.py": "# app/main/routes.py\nfrom app.main import main\n\n@main.route('/')\ndef index():\n    return 'Hello, World!'",
        f"{project_name}/app/main/templates/main/index.html": "<!-- app/main/templates/main/index.html -->\n<h1>Hello, World!</h1>",
        f"{project_name}/app/main/static/main/style.css": "/* app/main/static/main/style.css */\nbody { font-family: Arial, sans-serif; }",
        f"{project_name}/app/auth/__init__.py": "# app/auth/__init__.py\nfrom flask import Blueprint\n\nauth = Blueprint('auth', __name__)\n\nfrom app.auth import routes",
        f"{project_name}/app/auth/routes.py": "# app/auth/routes.py\nfrom app.auth import auth\n\n@auth.route('/login')\ndef login():\n    return 'Login Page'",
        f"{project_name}/app/auth/templates/auth/login.html": "<!-- app/auth/templates/auth/login.html -->\n<h1>Login Page</h1>",
        f"{project_name}/app/models.py": "# app/models.py\n# Define your database models here",
        f"{project_name}/app/forms.py": "# app/forms.py\n# Define your forms here",
        f"{project_name}/app/config.py": "# app/config.py\n# Define your configuration settings here",
        f"{project_name}/app/extensions.py": "# app/extensions.py\n# Initialize your extensions here",
        f"{project_name}/tests/__init__.py": "# tests/__init__.py\n",
        f"{project_name}/tests/test_main.py": "# tests/test_main.py\n# Write tests for main blueprint",
        f"{project_name}/tests/test_auth.py": "# tests/test_auth.py\n# Write tests for auth blueprint",
        f"{project_name}/.flaskenv": "FLASK_APP=run.py\nFLASK_ENV=development",
        f"{project_name}/.gitignore": "venv/\n*.pyc\n__pycache__/\ninstance/\n.webassets-cache\n",
        f"{project_name}/README.md": f"# {project_name.capitalize()}\n\nThis is a Flask web application.",
        f"{project_name}/run.py": "# run.py\nfrom app import app\n\nif __name__ == '__main__':\n    port = int(input('Enter the port number to run the Flask app (default is 5000): ') or 5000)\n    app.run(port=port)"
    }

    # Create the files with their initial content
    for file_path, content in files.items():
        with open(file_path, 'w') as file:
            file.write(content)
    
    print(f"Flask project '{project_name}' structure created successfully!")
# Ask for project name input
project_name = input("Enter the name for your Flask project: ").strip()

# Create the project structure if it doesn't exist
create_flask_project_structure(project_name)
