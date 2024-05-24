#!/bin/bash
sudo apt update -y
sudo apt install docker.io -y
sudo apt install docker-compose -y
newgrp docker
sudo usermod -aG docker ${USER}
cat <<EOF > docker-compose.yaml
version: "3"
services:
  mysqldb:
    container_name: mysqldb
    image: mysql:latest
    ports:
      - "3307:3306"
    environment:
      MYSQL_DATABASE: elearningsystem
      MYSQL_ROOT_PASSWORD: root
      MYSQL_PASSWORD: root
    volumes:
      - mysqldb-data:/var/lib/mysql
    healthcheck:
      test: ["CMD-SHELL", "mysqladmin ping -h localhost -u root -proot"]
      interval: 30s
      timeout: 10s
      retries: 10

  springboot-app:
    container_name: springboot-app
    image: hesoyam999/backendok
    ports:
      - "8080:8080"
    environment:
      MYSQL_HOST: mysqldb
      MYSQL_USER: root
      MYSQL_PASSWORD: root
      MYSQL_PORT: 3306
    depends_on:
      mysqldb:
        condition: service_healthy

  angular-app:
    container_name: angular-app
    image: hesoyam999/frontendok
    ports:
      - "4200:80"
    depends_on:
      - springboot-app

volumes:
  mysqldb-data:
EOF
docker-compose up 
