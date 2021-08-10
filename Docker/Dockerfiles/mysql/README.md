1. docker-compose  运行

```sh
# Start the container
docker-compose up -d
# Confirm container is running
docker ps
# stop container 
docker-compose down
```

2. 命令

   ```mysql
   #进入容器
   docker exec -it mysql bash
   
   #登录mysql
   mysql -u root -p
   ALTER USER 'root'@'localhost' IDENTIFIED BY 'Lzslov123!';
   
   #添加远程登录用户
   CREATE USER 'test'@'%' IDENTIFIED WITH mysql_native_password BY 'test';
   GRANT ALL PRIVILEGES ON *.* TO 'test'@'%';
   ```

   

3. 参考

   [https://hub.docker.com/_/mysql](https://hub.docker.com/_/mysql)

