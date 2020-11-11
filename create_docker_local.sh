
docker network create awm2021

docker stop geodjango_postgis
docker rm geodjango_postgis
docker create --name geodjango_postgis --network awm2021 --network-alias geodjango_network_alias -t -p 25432:5432 -v my_first_spatialdb_data:/var/lib/postgresql kartoza/postgis
docker start geodjango_postgis