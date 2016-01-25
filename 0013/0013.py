#!/usr/bin/env python
# -*- coding: utf-8 -*-  
import urllib2
from bs4 import BeautifulSoup
import os

# 创建文件夹，昨天刚学会
path = os.getcwd()   				     # 获取此脚本所在目录
new_path = os.path.join(path,u'test')
if not os.path.isdir(new_path):
  os.mkdir(new_path)

def drawpic(url):
    page = urllib2.urlopen(url)
    contents = page.read()
    soup = BeautifulSoup(contents)
    pics = soup.find_all('img','BDE_Image')
    for i in pics:
        link = i.get('src')
        print link
        try:
            content2 = urllib2.urlopen(link).read()
        except urllib2.URLError, e:
            print e.reason
            continue
        with open(u'test/'+ link[-10:],'wb') as f:
            f.write(content2)


if __name__ == '__main__':
    drawpic('http://tieba.baidu.com/p/2166231880')