#### :monkey: Git
![](https://img.shields.io/badge/Git-red.svg) ![](https://img.shields.io/badge/版本控制-red.svg)

##### 1.拉取、推送、切换分支
```
# dev为远程仓库的分支名
git fetch origin dev
# 查看分支
git branch
git branch -a
# 切换分支
git checkout 分支名
# 创建并切换到本地分支
git checkout -b newBranch 
# 拉取远程分支代码
git pull origin dev 
# 添加修改
git add .
# 提交修改
git commit -m "修改信息"
# 推送本地分支到远程仓库
git push origin 本地分支
# 重命名
git branch -m oldName  newName

```
##### 2.删除远程分支
- `git push origin --delete searchPublication`
- `git push origin:searchPublication`
-  `git push -f origin:my_remote_branch`(强制删除)

##### 3.撤销操作
- 撤销add的操作(已add未commit)
    ```
    # 撤销当前所有的修改
    git checkout .
    # 撤销单个文件的修改
    git checkout 文件名

    git reset HEAD . (或者文件名)
    # 查看状态
	git status 
    # 对上次的所有add的文件进行撤销 
	git reset HEAD 
    # 对单个文件进行撤销
	git reset HEAD XXX/XXX/XXX.java 
    ```

- 撤销commit的操作(已经commit)	
	```
    git rm .  (或者文件名)
	git rm  XXX/XXX/XXX.java
    ```

##### 4.解除/关联 远程仓库
```
git remote add origin https://XXXXXXX.git
git remote remove origin
```
	
##### 5.验证是否成功安装ssh key
 `ssh -T git@github.com`
	
##### 6.git cherry-pick 的使用
`git cherry-pick` 能够把另一个分支的一个或多个提交复制到当前分支，具体使用如下：
- 首先`git checkout`切换到另一个分支
- 然后使用`git log`找到想要复制的`commit id`,记录下来
- 切换到自己分支，使用`git cherry-pick  [上面记录的commit id]`  回车即可
- 如果想要复制多个, 使用`git cherry-pick [commitid1..commitid100]`，`commitid1`为想复制的最老提交(不包括),`commitid100`为想复制的最新提交(包括)
- 如果想要包括`commitid1`,那么在`commitid1`后加^即可，即 `git cherry-pick [commitid1^..commitid100]`

##### 7.fatal: refusing to merge unrelated histories
`git pull --allow-unrelated-histories`

##### 8.想切换分支，又不想删除当前分支的改动
```
# 首先 缓存当前改动，执行存储时，添加备注，方便查找，只有git stash 也要可以的，但查找时不方便识别
git stash 
git stash save "save message"
# 然后切换分支
git checkout 其他分支名
# after doing something, 切回到原分支
git checkout 原分支
# 恢复之前缓存的工作目录
git stash pop
```

