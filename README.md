# flask-and-mongo
exer class for connecting to seperate containers with docker

sudo apt update

sudo apt install -y ca-certificates curl gnupg

sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt update

sudo apt-get -y install docker-ce

sudo usermod -aG docker $USER


clone reg: 

cd app

 docker build -t flask .

 now have flask image

  docker run --name flask -d -p 5000:5000 flask

 mongo: 
 docker pull mongo
 docker run --name mongo -p 27017:27017 -d mongo

 
now both containers are up.

 docker network create flask_mongo
 docker network ls
 docker network connect flask_mongo flask
 docker network connect flask_mongo mongo
 docker network inspect flask_mongo

 docker exec -it flask ping mongo
there is: good!

install in the host: sudo apt install mongodb-clients
mongo --host <ip of host> --port <same port run command>
show dbs -> use my_database -> show collections -> db.my_collection.find() -
shows all db in mongo.

here it is all!


























  
