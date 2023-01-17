FROM python:3.8
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1
RUN mkdir /appdjango
WORKDIR /appdjango

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .

