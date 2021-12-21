FROM python:3.6
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
COPY models-0.1.tar.gz /app/models-0.1.tar.gz
RUN pip install -r requirements.txt
RUN pip install /app/models-0.1.tar.gz
COPY . /app

CMD python manage.py runserver 0.0.0.0:8000