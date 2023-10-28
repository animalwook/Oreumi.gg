FROM python 3.10.12

WORKDIR /app/

COPY . /app/

RUN python3 -m venv ggvenv && . ggvenv/bin/activate
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]