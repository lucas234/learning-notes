`ubuntu` 安装 `MySQL 5.7`

一、前置条件

- 已安装`wget`
- 未安装执行：`apt-get update && apt-get install -y wget `

二、 安装

1. 下载`mysql`配置

   `wget https://dev.mysql.com/get/mysql-apt-config_0.8.16-1_all.deb`

2. 运行该文件，并选择要安装的版本，（5.7版本的选择 1，1，4）

   `sudo dpkg -i mysql-apt-config_0.8.16-1_all.deb`

3. 安装`MySQL`，如果有提示输入密码，则设置密码；未设置密码则需继续执行第`4`步

   `sudo apt-get install -y mysql-server`

4. 查看`MySQL`的账户和密码, 默认用户为debian-sys-maint，获取到密码

   `cat /etc/mysql/debian.cnf`

   类似输出如下：

   >  [client]
   >  host     = localhost
   >  user     = debian-sys-maint
   >  password = km73KpVuSNg2UDHK
   >  socket   = /var/run/mysqld/mysqld.sock
   >  [mysql_upgrade]
   >  host     = localhost
   >  user     = debian-sys-maint
   >  password = km73KpVuSNg2UDHK
   >  socket   = /var/run/mysqld/mysqld.sock

5. 重启并更改`root`用户的密码

   ```bash
   # 要先重启一下，不然无法连接
   /etc/init.d/mysql restart
   # 步骤4获取到的用户名密码
   mysql -udebian-sys-maint -p3tD9c0pngxtlocpA
   # 更改root账户的密码
   update mysql.user set authentication_string=PASSWORD("123456") where user='root';
   flush privileges;
   # 重新启动
   service mysql start
   ```

6. 用`root`账户登录

   ```mysql
   # 查看user表
   SELECT user,authentication_string,plugin,host FROM mysql.user;
   # 创建数据库
   create database bugs;
   # 创建用户
   CREATE USER 'bugs'@'localhost' IDENTIFIED BY '1234_Qwer';
   GRANT ALL ON bugs.* TO 'bugs'@'localhost';
   flush privileges;
   ```

三、其他方式设置`root` 账户密码（未设置密码的）

1. 停止`MySQL`服务

   `sudo service mysql stop`

2. `mysqld_safe` 运行

   `sudo mysqld_safe --skip-grant-tables --skip-networking &`

3. 另起一个`terminal`，运行

   `sudo mysql -u root`

4. 更改`root`用户密码

   ```mysql
   update mysql.user set authentication_string=PASSWORD("123456") where user='root';
   flush privileges;
   ```

5. 关闭`mysql_safe` 模式

   `sudo mysqladmin -S /var/run/mysqld/mysqld.sock shutdown`

   或者直接杀掉进程 `sudo  pkill mysql`  or `sudo killall mysql`

6. 正常启动

   `sudo service mysql start`

7. `root`用户登录

   `mysql -u root -p`

   