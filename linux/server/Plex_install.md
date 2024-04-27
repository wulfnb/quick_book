# Install Plex

## Using docker

docker run -d \
  --name=plex \
  --net=host \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Etc/UTC \
  -e VERSION=docker \
  -e PLEX_CLAIM= `#optional` \
  -v /home/config:/config \
  -v /home/wolverine/tvseries:/tv \
  -v /home/wolverine/movies:/movies \
  --restart unless-stopped \
  lscr.io/linuxserver/plex:latest