python -m venv venv
.\venv\Scripts\Activate.ps1
py -m pip install --upgrade pip
pip install django
django-admin startproject defaults
New-Item -Path .gitignore -ItemType File
Rename-Item -Path "defaults" -NewName "projeto"
cd projeto
py manage.py migrate
py manage.py startapp app_1
New-Item -Path app_1\urls.py -ItemType File
New-Item -Path app_1\forms.py -ItemType File
mkdir -p app_1\templates
New-Item -Path app_1\templates\index.html -ItemType File
New-Item -Path app_1\templates\base.html -ItemType File
mkdir -p static\css, static\js, static\img
New-Item -Path static\css\styles.css -ItemType File
New-Item -Path static\js\scripts.css -ItemType File
pip list
cd .. pip freeze > requirements.txt
py manage.py runserver