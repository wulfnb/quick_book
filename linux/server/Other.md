docker run -d \
  --name=heimdall \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Etc/UTC \
  -p 8082:80 \
  -p 4443:443 \
  -v /home/config:/config \
  --restart unless-stopped \
  lscr.io/linuxserver/heimdall:latest


docker run -p 8083:8080 -p 50000:50000 -v /home/wolverine/jenkins:/var/jenkins_home -d jenkins/jenkins

(password will be in console)


docker run -d --tmpfs /tmp --tmpfs /run --tmpfs /run/lock -v /sys/fs/cgroup:/sys/fs/cgroup:ro -p 8880:8880 plesk/plesk

admin / changeme1Q**


docker run --name prometheus -d -p 9090:9090 prom/prometheus


docker run --name nagios4 -p 0.0.0.0:8084:80 jasonrivers/nagios:latest

nagiosadmin / nagios