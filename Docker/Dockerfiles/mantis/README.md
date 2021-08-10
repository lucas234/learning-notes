1. docker-compose  运行

   ```sh
   # Start the container
   docker-compose up -d
   # Confirm container is running
   docker ps
   # stop container 
   docker-compose down
   ```
   
2. 打开安装`http://localhost:8989/admin/install.php`

   按照如下填写
   
   ```
================================================================================
   Installation Options
   ================================================================================
   Type of Database                                        MySQL/MySQLi
   Hostname (for Database Server)                          mysql
   Username (for Database)                                 mantisbt
   Password (for Database)                                 mantisbt
   Database name (for Database)                            bugtracker
   Admin Username (to create Database if required)         root
   Admin Password (to create Database if required)         root
   Print SQL Queries instead of Writing to the Database    [ ]
   Attempt Installation                                    [Install/Upgrade Database]
   ================================================================================
   ```

3. 输入用户名密码登录

   ```
   username: administrator
   password: root
   ```

4. 问题

   如果遇到错误：Does administrative user have access to the database? ( No such file or directory ) 

   ![error](C:\diy\Dockerfiles\mantis\error.png)

   

   则需要将`Hostname`中的`localhost` 替换成`mysql`（即`docker-compose.yml`中定义的`service`名字）![update](C:\diy\Dockerfiles\mantis\update.png)

5. 参考

   部署教程：[https://hub.docker.com/r/xlrl/mantisbt](https://hub.docker.com/r/xlrl/mantisbt)
   
   使用教程：[https://www.guru99.com/mantis-bug-tracker-tutorial.html](https://www.guru99.com/mantis-bug-tracker-tutorial.html)