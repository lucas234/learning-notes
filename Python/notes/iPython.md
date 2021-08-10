#### :snowman: iPython
![](https://img.shields.io/badge/编程语言-purple.svg) ![](https://img.shields.io/badge/iPython-green.svg) ![](https://img.shields.io/badge/模块学习-yellow.svg)

##### Ipython shell命令
- Ctrl-P    或上箭头键 后向搜索命令历史中以当前输入的文本开头的命令
- Ctrl-N   或下箭头键 前向搜索命令历史中以当前输入的文本开头的命令
- Ctrl-R   按行读取的反向历史搜索（部分匹配）
- Ctrl-Shift-v   从剪贴板粘贴文本
- Ctrl-C   中止当前正在执行的代码
- Ctrl-A   将光标移动到行首
- Ctrl-E   将光标移动到行尾
- Ctrl-K   删除从光标开始至行尾的文本
- Ctrl-U   清除当前行的所有文本译注12
- Ctrl-F   将光标向前移动一个字符
- Ctrl-b   将光标向后移动一个字符
- Ctrl-L   清屏

##### Ipython 魔术命令
- `%quickref` 显示IPython的快速参考
- `%magic` 显示所有魔术命令的详细文档
- `%debug` 从最新的异常跟踪的底部进入交互式调试器
- `%hist` 打印命令的输入（可选输出）历史
- `%pdb` 在异常发生后自动进入调试器
- `%paste` 执行剪贴板中的Python代码
- `%cpaste` 打开一个特殊提示符以便手工粘贴待执行的Python代码
- `%reset` 删除interactive命名空间中的全部变量/名称
- `%page OBJECT` 通过分页器打印输出OBJECT
- `%run script.py` 在IPython中执行一个Python脚本文件
- `%prun statement` 通过cProfile执行statement，并打印分析器的输出结果
- `%time statement` 报告statement的执行时间
- `%timeit statement` 多次执行statement以计算系综平均执行时间。对那些执行时 间非常小的代码很有用
- `%who、%who_ls、%whos` 显示interactive命名空间中定义的变量，信息级别/冗余度可变
- `%xdel variable` 删除variable，并尝试清除其在IPython中的对象上的一切引用

##### Ipython系统交互命令
- `%alias ll ls -l` 将ll作为ls -l的别名暂时保存
- `%!cmd` 在系统shell中执行cmd
- `%output  = !cmd args` 执行cmd，并将stdout存放在output中
- `%alias alias_name cmd` 为系统shell命令定义别名
- `%bookmark` 使用IPython的目录书签系统
- `%cd directory` 将系统工作目录更改为directory
- `%pwd` 返回系统的当前工作目录
- `%pushd directory` 将目前目录入栈，并转向目标目录
- `%popd` 弹出栈顶目录，并转向该目录
- `%dirs` 返回一个含有当前目录栈的列表
- `%dhist` 打印目录访问历史`%env` 以dict形式返回系统环境变量
