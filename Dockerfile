FROM python:3.11-slim-buster
RUN apt-get update && apt-get install -y \
    software-properties-common \
    unzip \
    curl \
    xvfb 

RUN apt -f install -y
RUN apt-get install -y wget
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install ./google-chrome-stable_current_amd64.deb -y

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir
COPY . .