#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Дано слово. Переставить его последнюю букву на место первой.
# При этом первую, вторую,..., предпоследнюю буквы сдвинуть
# вправо на одну позицию.

if __name__ == '__main__':
    word = input("Введите слово ")
    word = word.replace(word[0], word[-1])
    word = word[:-1]
    word = '..' + word
    print(word)
