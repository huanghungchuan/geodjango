#!/bin/bash

# Createing PGAdmin4 Container
sudo docker stop geodjango_pgadmin4
sudo docker rm geodjango_pgadmin4
sudo docker create --name geodjango_pgadmin4 --network wmap_network --network-alias wmap-pgadmin4 -t -v wmap_pgadmin_data:/var/lib/pgadmin -e 'PGADMIN_DEFAULT_EMAIL=hugnchuan.huang@tudublin.ie' -e 'PGADMIN_DEFAULT_PASSWORD=mypassword' dpage/pgadm$
sudo docker start geodjango_pgadmin4

# Createing PostGIS Container
sudo docker stop geodjango_postgis
sudo docker rm geodjango_postgis
sudo docker create --name wmap_postgis --network wmap_network --network-alias wmap-postgis -t -v wmap_postgis_data:/var/lib/postgresql kartoza/postgis
sudo docker start geodjango_postgis

# Creating Project Container
sudo docker stop geodjango_container
sudo docker rm geodjango_container
sudo docker rmi geodjango
sudo docker build -t geodjango .
sudo docker create --name geodjango_container --network geodjango_network --network-alias geodjangoImage -t -p 28001:8001 geodjango
sudo docker start geodjango_container

# Creating NginX Container
sudo docker stop geodjango_nginx
sudo docker rm geodjango_nginx
sudo docker rmi nginx_image
sudo docker build -t nginx_image ./nginx
sudo docker create --name geodjango_nginx --network wmap_network --network-alias wmap-nginx-certbot -p 80:80 -p 443:443 -t -v wmap_web_data:/usr/share/nginx/html -v $HOME/wmap_nginx_certbot/conf:/etc/nginx/conf.d -v /etc/letsenc$
sudo docker start geodjango_nginx
