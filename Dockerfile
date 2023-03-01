FROM python:3.8

WORKDIR "/usr/src/app/"

COPY . .
RUN pip install django
RUN pip install mysqlclient

CMD ["/bin/bash", "-c", "./pilotage/manage.py runserver 0.0.0.0:8000"]

# CMD ["/bin/bash", "-c", "./manage.py makemigrations; manage.py migrate; ./manage.py runsslserver 0.0.0.0:8000"]
# CMD ["/bin/bash", "-c", "./helpMeName/manage.py runserver 0.0.0.0:8000"]