To run:

Create a virtual environment using my detailed requirements.txt (created with pip freeze -l > requirements.txt)
or environment.yml.  For instance:

conda env create -f environment.yml
source activate adam_django_celery
celery -A DNA_form worker -l info          (starts celery worker)

in a new console run:
source activate adam_django_celery
brew install rabbitmq
export PATH=$PATH:/usr/local/sbin
brew services start rabbitmq

python manage.py runserver localhost:8000

Now the Web app should be available at localhost:8000 


jamieleecho Notes:
To run:
docker-compose build
docker-compose up

Currently the app, worker and broker all start up. The app seems to be getting blocked somewhere
