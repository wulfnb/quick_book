



curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh ./get-docker.sh --dry-run

sudo sh get-docker.sh

docker run hello-world

if getting permission issues .sock file

sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
docker run hello-world


docker login -u wulfnb