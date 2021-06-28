#### :monkey: Docker
![](https://img.shields.io/badge/Docker-cyan.svg) 

##### 1.停止、删除多个容器
- 停止多个容器`docker stop $(docker ps -a -q)`
- 删除多个容器`docker rm $(docker ps -a -q)`
- 强制删除某个镜像`docker image rm -f 容器id`
- 删除所有状态为`exited`的容器`docker rm $(docker ps -a -q -f status=exited)`和命令类似：`docker container prune`

##### 2.查看容器的端口、IP
- 查看端口 `docker port static-site`
- 查看容器IP`docker exec -it 8bc945592f31 ip addr`

##### 3. --rm 参数
`--rm` 参数是指当容器结束时，会清理掉该容器，不会显示在`docker ps -a` 列表中，例如：`docker run -it --rm prakhar1989/foodtrucks-web bash`

##### 4. 网络相关
- 查看运行容器的网络信息`docker network inspect bridge`
- 创建网络`docker network create foodtrucks-net`
- 删除网络`docker network rm foodtrucks-net`
- 查看网络`docker network ls`

##### 5. 容器启动之后查看日志
`docker container [-f] logs 容器ID或者名字`

##### 6. 容器拷贝文件
- 容器拷贝到本地`docker cp 容器id:路径/文件 本地路径`
- 本地拷贝到容器`docker cp 本地路径 容器长ID:容器路径`

##### 7. 动态提交到images
- `docker build -t thirsty_darwin_base /path/to/Dockerfile`
- `docker run -it --name=thirsty_darwin_changes thirsty_darwin_base /bin/bash`
- 在交互窗口安装或者其他的操作
- 提交修改到镜像`docker commit thirsty_darwin_changes thirsty_darwin`

##### 8.导出、导入镜像
- 导出`docker image save helloworld > helloworld.tar`
- `docker save -o kafka.tar wurstmeister/kafka `
- 导入`docker image load -i helloworld.tar`

##### 9. 删除所有无用的数据卷
`docker volume rm $(docker volume ls -qf dangling=true)`

##### 10. 杀掉所有运行的容器
`docker kill $(docker ps -a -q)`

##### 11. 删除所有停止的容器
`docker rm $(docker ps -a -q)　`

##### 12。 删除所有dangling=true的镜像
`docker rmi $(docker images -q -f dangling=true)`

##### 13. 删除所有镜像
`docker rmi $(docker images -q)`

##### 14. 镜像常用命令
```shell
# build 镜像
docker image build --rm=true .
# 安装镜像
docker image pull ${IMAGE}
# 查看所有镜像
docker image ls
# 查看所有镜像详情
docker image ls --no-trunc
# 删除镜像
docker image rm ${IMAGE_ID}
# 删除无用的镜像
docker image prune
# 删除所有镜像
docker image rm $(docker image ls -aq)
```
##### 15. 容器常用命令
```shell
# 运行容器
docker container run

# 查看容器
docker container ls

# 查看所有容器
docker container ls -a

# 停止容器
docker container stop ${CID}

# 停止所有运行的容器
docker container stop $(docker container ls -q)

# 列出所有exited=1的容器
docker container ls -a --filter "exited=1"

# 删除容器
docker container rm ${CID}

# 通过正则表达式删除
docker container ls -a | grep wildfly | awk '{print $1}' | xargs docker container rm -f

# 删除所有exited的容器
docker container rm -f $(docker container ls -a | grep Exit | awk '{ print $1 }')

# 删除所有容器
docker container rm $(docker container ls -aq)

# 查看容器的IP
docker container inspect --format '{{ .NetworkSettings.IPAddress }}' ${CID}

# 进入容器，该容器必须已运行
docker container attach ${CID}

# 打开容器的命令行模式
docker container exec -it ${CID} bash | sh

# Get container id for an image by a regular expression
docker container ls | grep wildfly | awk '{print $1}'
```

##### 16. 实例
- build 镜像
	```shell
    docker build -t ubuntu-jdk8 .
	docker build -t myredis .
    ```

- 运行docker
    ```shell
	docker run -it ubuntu-jdk8
	docker run -d -p 6380:6379 --name myredis  myredis
    ```
- 查看java的安装路径
    ```shell
	update-alternatives --list java
	update-java-alternatives -l | awk '{print $3}'
    ```
- `docker attach <container>` 要attach上去的容器必须正在运行。
- `docker exec -it <container> bash|sh`直接访问容器内的bash shell。
- 容器中运行`py`文件`docker run  -v  C:\work\test:/usr/src/app -it -w /usr/src/app  test python test.py`
	
- docker-rdis
    ```
    docker pull redis:latest
    docker run -itd --name redis-test -p 6379:6379 redis
    docker exec -it redis-test /bin/bash
    redis-cli
    ```

##### 17. 问题
1.遇见这种错误时：`Error response from daemon: conflict: unable to delete 2da6c8b45647 (cannot be forced) - image has dependent child images`
- 先查看依赖：`docker image inspect --format='{{.RepoTags}} {{.Id}} {{.Parent}}' $(docker image ls -q --filter since=XXX) `(XXX指镜像ID),然后删掉依赖后再删除即可
- 可能是因为你创建的时候用了`cache`导致的，重新build的时候加上参数`--no-cache`(类似`docker build -t your docker name . --no-cache`)

2.alpine apk update 时报错：`ERROR: http://dl-cdn.alpinelinux.org/alpine/v3.11/main: network error (check Internet connection and firewall)`
- 在build时加上`--network=host`即可：
- 即`docker build -t your docker name . --no-cache --network=host`
