FROM python:latest
RUN mkdir /code
RUN apt-get update  \
    && apt-get install -y postgresql-client
COPY requirements.txt /code
RUN pip install --upgrade pip
RUN pip install -r /code/requirements.txt
COPY .. /code/
WORKDIR /code/expense_manager