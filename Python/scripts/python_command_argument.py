# @Time    : 2021/5/8 11:23
# @Author  : lucas
# @File    : autoGenToc.py
# @Project : pyqt
# @Software: PyCharm

import sys
import argparse

def get_argument():
    parser = argparse.ArgumentParser(description="This is a description of %(prog)s")
    parser.add_argument("-f","--file", required=True, help="The Markdown file need to be added toc")
    parser.add_argument("-o","--output",help="The Markdown file with toc")
    args = parser.parse_args()
    print(args.file)
    return args

get_argument()

# path = sys.argv[1:]
# print(path)

