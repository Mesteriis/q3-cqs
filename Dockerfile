FROM python:3.11-slim

WORKDIR /code

COPY requirements.txt .
RUN pip install --no-cache -r requirements.txt

COPY . .