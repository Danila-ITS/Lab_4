#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Дано предложение. Определить, есть ли в нем буквосочетания чу или щу. В случае
# положительного ответа найти также порядковый номер первой буквы первого из них

if __name__ == '__main__':
    sentence = input("Введите предложение ").lower()
    n = len(sentence)
    for word in sentence:
        if 'чу' in sentence:
            idex = sentence.find('чу')
            print("Номер буквы, с котрой начинается чу", idex+1)
        elif 'щу' in sentence:
            idex = sentence.find('щу')
            print("Номер буквы, с котрой начинается щу", idex+1)
