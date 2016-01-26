#!/usr/bin/env python
# -*- coding: utf-8 -*-  
import xlwt
import re

def txt_to_exl(file):
    book = xlwt.Workbook(encoding='utf-8',style_compression=0)
    sheet = book.add_sheet('sheet1')
    with open(file,'r') as f:
        count = 0
        for line in f:
            cols = re.split('[":\[\],]',line.strip())
            while '' in cols:
                cols.remove('')
            for i in xrange(len(cols)):
                sheet.write(count,i,cols[i])
            count += 1
    book.save('test.xls')

if __name__ == '__main__':
    txt_to_exl('test.txt')
