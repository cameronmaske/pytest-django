FROM stackbrew/ubuntu:14.04

RUN apt-get -q update
RUN apt-get install -y python python-pip python-dev libxml2-dev libxslt-dev libpq-dev python-psycopg2 git

# Install Ruby + Foreman
RUN apt-get install -y ruby
RUN gem install foreman

# Remove unnecessary packages
RUN apt-get autoremove -y

ADD requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt

ADD requirements-dev.txt /code/requirements-dev.txt
RUN pip install -r /code/requirements-dev.txt


ADD .env /code/.env
WORKDIR /code/
EXPOSE 8000

CMD foreman run python server/manage.py runserver 0.0.0.0:8000