FROM node:18-bullseye-slim

WORKDIR /app/

COPY ./frontend/package*.json ./

RUN npm install

COPY ./frontend .

EXPOSE 3000

ENV CI=true
