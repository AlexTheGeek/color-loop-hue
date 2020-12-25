FROM python:3.8.6-buster

WORKDIR /code

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY /code .

CMD ["python", "main.py"]