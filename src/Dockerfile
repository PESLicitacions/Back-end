FROM python:3.11.2-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y netcat-openbsd gcc && \
    apt-get clean

RUN mkdir static
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
RUN python3 manage.py collectstatic

EXPOSE 8080
CMD ["gunicorn","--bind", ":8080", "adjudiCat.wsgi:application"]
#CMD ["python3", "manage.py", "runserver", "0.0.0.0:8080"]
