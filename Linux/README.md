#### :snowman: Linux
![](https://img.shields.io/badge/Linux-black.svg) ![](https://img.shields.io/badge/操作系统-black.svg) 

##### 1. 查找大文件
```shell
du -sh /usr/* | grep G 
du -h 统计文件大小
```
##### 2. 显示当前路径下，大于50M的文件（包含子文件夹内的文件）
`find ./ -size +50M` 

##### 3. 删除当前路径下文件，大于50M的文件。（包含子文件夹内的文件）
```shell
# 删除当前路径下大于50M的文件。（包含子文件夹内的文件）
find ./ -size +50M -exec rm {} \; 

# 删除当前路径下1天前名字包括Screenshot的文件
find ./ -type f -mtime +1 -name "Screenshot*" -exec rm "{}" +  

# 或者用：
find . -mtime +5 -type f | xargs rm -rf

# /email/v1_bak --设置查找的目录；
# -mtime +92 --设置时间为91天前；
# -type f --设置查找的类型为文件；
# -name *.mail[12] --设置文件名称中包含mail1或者mail2；
# -exec rm -f --查找完毕后执行删除操作；
find /email/v2_bak -mtime +92 -type f -name *.mail[12] -exec rm -rf {} \;
	
# 删除大于1G的文件
find . -type f -size +1GB -delete   

# 打印出删除大于1G的文件
find . -type f -size +1GB -print -delete   
```
##### 4. 连接远程服务器
`ssh username@10.212.38.116`  

##### 5. 定时任务
```shell
# 定时任务 
crontab -e | -r | -l
# -e : 进入编辑模式
# -r : 删除目前的时程表
# -l : 列出目前的时程表
59 16 * * 1-5 cd /Users/lexisnexis/checkScripts && sh check-agent.sh

service crond start    # 启动服务
service crond stop     # 关闭服务
service crond restart  # 重启服务
service crond reload   # 重新载入配置
service crond status   # 查看服务状
```

##### 6. 远程服务器拷贝文件
```shell
scp -r local_folder remote_username@remote_ip:remote_folder
scp -r C:\work\issues.docx LexisNexis@10.212.38.116:/Users/lexisnexis
```

##### 7. 获取进程ID
```shell
ps -ef | grep "name" | grep -v grep | awk '{print $2}'
pgrep -f name
ps -ef | awk '/[n]ame/{print $2}'
ps x | awk '/[n]ame/{print $1}'
```
##### 8. 按名字杀掉进程
`pkill -f name`
   
##### 9. 判断端口有没有被占用（有输出就是被占用）
```shell
netstat -an|grep 4723
lsof -i | grep 4723 
# 等于 
lsof -i tcp:4723
```

##### 10. 判断进程是否存在，不存在则启动
```shell
#!/bin/sh
#第一种
if [ ! -f "/Users/test/checkScripts/log.txt" ];then
echo "file is not exist."
else
rm -f /Users/lexisnexis/checkScripts/log.txt
echo "delete log.txt successfully."
fi

ps -fe|grep jenkins |grep -v grep
if [ $? -ne 0 ]
then
echo "start process....."
cd /Users/test/jenkinsAgent&&open slave-agent.jnlp
else
echo "runing....."
fi
```

```shell
# 第二种，通过端口判断
# ps -fe | grep 'main.js -a 127.0.0.1 -p 4723' | grep -v grep
netstat -an|grep 4723
if [ $? -ne 0 ]
then
echo "start process....."
cd /usr/local/lib/node_modules/appium/build/lib && node main.js -a 127.0.0.1 -p 4723
else
echo "runing....."
fi
# pkill -f 'main.js -a 127.0.0.1 -p 4723'
```
    
##### 11. 批量删除文件（文件太多时）

这句解释为：输出所有的文件名(用空格分割)，xargs就是将ls的输出，每10个为一组(以空格为分隔符)，作为rm -rf的参数也就是说将所有文件名10个为一组，由rm -rf删除，这样就不会超过命令行的长度了.

`ls | xargs -n 10 rm -fr ls`

   
##### 12. 批量授权文件（文件太多时）

`find ./ -type f  -exec chmod -R 777 "{}" +`
    
##### 13. 获取文件4-5行的第三项文字
```shell
awk 'NR == 4,NR == 5 { print $3 } ' debian.cnf
awk 'NR == 5 { print "mysql -udebian-sys-maint -p" $3 } ' debian.cnf
```
   