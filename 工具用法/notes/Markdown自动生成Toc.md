#### Markdown自动生成Toc

1.保存以下代码到`auto2toc.py`:
```python
# @Time    : 2021/5/8 11:23
# @Author  : lucas
# @File    : autoGenToc.py

import sys
import codecs


toc=[]
# sign = "\t"
# 两个空格
sign = "  "


def replace(line:str)->str:
    return line.replace(" ","-").replace(".","").replace("/","").replace("、","").replace("（","").replace("）","").replace("(","").replace(")","").lower()


def run():
    # 自动生成md的toc目录
    # 要处理的文件的路径
    path = sys.argv[1]
    descpath =  path[:path.rindex("."):] + ".withtoc."+path[path.rindex(".")+1:]

    flag=False
    print(path)
    with codecs.open(path,"r") as file_object:
        lines = file_object.readlines()
    
    for line in lines:
        if(line.startswith("```")):
            flag = not flag
        if(flag):
            continue
        if line.startswith("#####"):
            line = line.replace("##### ","").strip()
            toc.append(sign*4+"* ["+line+"](#"+replace(line)+")")
        elif(line.startswith("####")):
            line = line.replace("#### ","").strip()
            toc.append(sign*3+"* ["+line+"](#"+replace(line)+")")
        elif(line.startswith("###")):
            line = line.replace("### ","").strip()
            toc.append(sign*2+"* ["+line+"](#"+replace(line)+")")
        elif(line.startswith("##")):
            line = line.replace("## ","").strip()
            toc.append(sign*1+"* ["+line+"](#"+replace(line)+")")
        elif(line.startswith("#")):
            line = line.replace("# ","").strip()
            toc.append(sign*0+"* ["+line+"](#"+replace(line)+")")
        else:
            pass

    with codecs.open(descpath,"w") as file_object:
        for line in toc:
            file_object.write("\n")
            file_object.write(line)
            file_object.write("\n")
        for line in lines:
            file_object.write(line)


if __name__=="__main__":
	run()
```


2.然后终端运行：`python auto2toc.py  your_file.md`