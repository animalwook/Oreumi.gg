FROM python:3.10

ENV PYTHONUNBUFFERED = 1


RUN mkdir /app

WORKDIR /app

COPY requirements.txt /app/

RUN python3 -m venv ggvenv
RUN source ggvenv/bin/activate

RUN pip install -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]