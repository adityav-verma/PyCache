FROM python:3.7-buster
LABEL maintainer="aditya.verma.connect@gmail.com"


RUN apt update && apt install nginx -y

RUN rm /etc/nginx/sites-available/default

COPY infra/nginx/default /etc/nginx/sites-available/default

WORKDIR /www/app

COPY requirements.lock .

RUN pip3 install --no-cache-dir -r requirements.lock

COPY . .

EXPOSE 80

RUN chmod +x /www/app/docker-entrypoint.sh

ENTRYPOINT ["/www/app/docker-entrypoint.sh"]