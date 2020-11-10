FROM nginx

RUN apt-get -y update && apt-get -y upgrade && apt-get -y install software-properties-common certbot python-certbot-nginx

RUN mv /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.old

COPY headers.conf /etc/nginx/conf.d
COPY server.conf /etc/nginx/conf.d

EXPOSE 8001