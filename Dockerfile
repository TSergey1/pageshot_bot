FROM python:3.11-slim-buster

# RUN pip install wheel
RUN pip install \
    pyppeteer==1.0.2

RUN apt-get update \
    && apt-get install --no-install-recommends --yes \
        libpq-dev gcc libc6-dev \
        chromium libxcursor1 libxss1 libpangocairo-1.0-0 libgtk-3-0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir
COPY . .