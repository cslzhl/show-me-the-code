#!/usr/bin/env python
# -*- coding: utf-8 -*-  
import os 

def get_files(path):
    filepath = os.listdir(path)
    files = []
    for fp in filepath:
        fppath = path + '/' + fp
        if os.path.isfile(fppath):
            files.append(fppath)
        elif os.path.isdir(fppath):
            files += get_files(fppath)
    return files
def count_line(files):
    line,blank,note = 0,0,0
    for file in files:
        f = open(file,'r')
        for l in f.readline():
            l = l.strip()
            line +=1
            if l[0] =='#' or l[0] == '/':
                note+=1
            elif l== '':
                blank+=1
        f.close()
    return line,blank,note

if __name__ == '__main__':
    files = get_files('.')
    print files
    lines = count_line(files)
    print "lines:%d, blanks:%d, notes:%d" %lines
    
