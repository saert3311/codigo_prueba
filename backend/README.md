# Servidor Backend django
La BD esta en sqlite asi que no hace falta mas nada.

Si no tienes virtualenv puedes instalarlo usando 

    pip install virtualenv

En la carpeta principal del proyecto se crea el entorno virtual

    py -m venv env

Se debe activar el entorno virtual

    .\env\Scripts\activate

Se instalan dependencias

    pip install requirements.txt

Se inicia el servidor django con 

    python manage.py runserver

