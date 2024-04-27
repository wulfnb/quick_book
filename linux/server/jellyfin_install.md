# Install jellyfin

## Using docker

> docker run -d   --name=jellyfin   -e PUID=1000   -e PGID=1000   -e TZ=Etc/UTC   -e JELLYFIN_PublishedServerUrl=192.168.1.50 `#optional`   -p 8096:8096   -p 8920:8920 `#optional`   -p 7359:7359/udp `#optional`   -p 1900:1900/udp `#optional`   -v /home/config:/config   -v /home/wolverine/tvseries:/data/tvshows   -v /home/wolverine/movies:/data/movies   --restart unless-stopped   lscr.io/linuxserver/jellyfin:latest