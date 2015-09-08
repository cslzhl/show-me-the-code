#!/usr/bin/env python
# -*- coding: utf-8 -*-  
def get_words(file):
    f = open(file,'rb')
    words = f.read()
    words = words.split('\n')
    return words

def check_words(input_word,words):
    result = input_word
    for word in words:
        if word == '':
            continue
        elif word in input_word:
            result = input_word.replace(word,'*'*len(word.decode('utf-8')))
    return result 
if __name__ == '__main__':
    words = get_words('filtered_words.txt')
    print check_words('程序员在上班。', words)
    print check_words('我妈妈是农民。', words)
 
