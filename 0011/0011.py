#!/usr/bin/env python
# -*- coding: utf-8 -*-  

def get_words(file):
    f = open(file,'rb')
    words = f.read()
    words = words.split('\n')
    return words

def check_words(input_word,words):
    for word in words:
        if word == '':
            continue
        elif word in input_word:
            return 'Freedom'
    return 'Human Rights'
if __name__ == '__main__':
    words = get_words('filtered_words.txt')
#    print check_words('程序员在上班。', words)
#    print check_words('我妈妈是农民。', words)
    while True:
        string = raw_input('输入句子:')
        print check_words(string,words)
'''
def word_check(input_word, filtered_words):
    for word in filtered_words:
        if word in input_word:
            return 'Freedom'
    return 'Human Rights'

file = open('filtered_words.txt')
filtered_words=[line.replace('\n','') for line in file]
print word_check('程序员在上班。', filtered_words)
print word_check('我妈妈是农民。', filtered_words)
'''
