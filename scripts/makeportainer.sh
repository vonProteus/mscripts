#!/bin/bash

docker stop portainer portainer_agent 
docker rm portainer portainer_agent
docker image rm portainer/portainer portainer/agent

docker volume create portainer_data
docker run -d -p 9000:9000 -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data --name portainer --restart always portainer/portainer
docker run -d -p 9001:9001 -v /var/run/docker.sock:/var/run/docker.sock -v /var/lib/docker/volumes:/var/lib/docker/volumes --name portainer_agent --restart always portainer/agent

