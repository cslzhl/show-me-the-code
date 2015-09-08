# -*- coding: utf-8 -*-
import operator

def get_count(filepath,lower=True):
    f= open(filepath,'rb')
    t= f.read()
    ignore =['\n',',', '.', ':', '!', '?', '”', '“', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    for i in ignore:
        t = t.replace(i,' ')
    if lower:
        t = t.lower()
#    t = t.strip()
    words = t.split(' ')
    dict = {}
    for word in words:
        word = word.strip()
        if word == '':
            continue
        if word in dict:
            dict[word]+=1
        else:
            dict[word] = 1
    return dict   
if __name__ == '__main__':
    result = sorted(get_count('test.txt').items(),key = operator.itemgetter(1),reverse = True)
    for item in result:
        print item[0],item[1] 
