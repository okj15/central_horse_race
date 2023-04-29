FROM python:3.9-slim

ENV APPDIR=/work \
    PYTHONIOENCODING=UTF-8

EXPOSE 8080
WORKDIR ${APPDIR}

COPY ./ ./

RUN apt-get update && apt-get install -y \
  gcc \
  git \
  sqlite3 \
  procps

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
