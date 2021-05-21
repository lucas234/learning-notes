# @Time    : 2021/5/21 11:23
# @Author  : lucas
# @File    : generate_resources_file.py
# @Project : pyqt
# @Software: PyCharm
from pathlib import Path
import os

path = Path(__file__).parent.joinpath("assets")


def generate_resources_file(path_):
    path_ = Path(path_)
    resources = [f"           <file alias='{i.name}'>assets/{i.name}</file>\n" for i in path_.iterdir()]
    with open("resources.qrc", "w") as f:
        f.write("<!DOCTYPE RCC>\n")
        f.write('   <RCC version="1.0">\n')
        f.write('       <qresource>\n')
        f.writelines(resources)
        f.write('       </qresource>\n')
        f.write('   </RCC>\n')
    os.system("pyrcc5 resources.qrc -o resources.py")

generate_resources_file(path)