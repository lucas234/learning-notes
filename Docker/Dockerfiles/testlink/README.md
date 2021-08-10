1. docker-compose  运行

```sh
# Start the container
docker-compose up -d
# Confirm container is running
docker ps
# stop container 
docker-compose down
```

2. 浏览器打开`http://localhost:83`，输入用户名密码：`username：admin，password：123456`

3. 语言更改，在`docker-compose.yml`中修改参数`TESTLINK_LANGUAGE`，中文：`zh_CN`，英文：`en_US`

4. 参考

   部署教程：[https://hub.docker.com/r/bitnami/testlink](https://hub.docker.com/r/bitnami/testlink)

   使用教程：[https://www.guru99.com/testlink-tutorial-complete-guide.html](https://www.guru99.com/testlink-tutorial-complete-guide.html)

