1. 直接运行

```sh
docker run --name zentao-server -p 81:80 -v C:\diy\Dockerfiles\delete_something\zentao:/app/zentaopms -v C:\diy\Dockerfiles\delete_something\data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=123456 -d idoop/zentao:latest
```

2. docker-compose  运行

```sh
# Start the container
docker-compose up -d
# Confirm container is running
docker ps
# stop container 
docker-compose down
```

3. 浏览器打开`http://localhost:81`，输入用户名密码：`username：admin，password：123456`