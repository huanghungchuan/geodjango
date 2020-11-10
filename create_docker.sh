docker stop geodjango_nginx
docker stop geodjango_container
docker rm geodjango_container
docker rmi geodjango
docker build -t geodjango .
docker create --name geodjango_container --network geodjango_network --network-alias geodjangoImage -t -p 28001:8001 geodjango
docker start geodjango_container
docker create --name geodjango_nginx --network geodjango_network --network-alias geodjangoNginx -t -p 20080:80 -v volume_Name:/usr/share/nginx/html nginx
docker start geodjango_nginx