
# Install qbittorrent

## install qbittorrent

> docker run -d   --name=qbittorrent   -e PUID=1000   -e PGID=1000   -e TZ=Etc/UTC   -e WEBUI_PORT=8081   -e TORRENTING_PORT=6881   -p 8081:8081   -p 6881:6881   -p 6881:6881/udp   -v /home/config:/config   -v /home/downloads:/downloads   --restart unless-stopped   lscr.io/linuxserver/qbittorrent:latest