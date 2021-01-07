#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Дано слово. Добавить к нему в начале и конце
# столько звездочек, сколько букв в этом слове
if __name__ == '__main__':
    Word = input("Введите слово ")
    N = len(Word)
    stared = '*' * N + Word + ('*' * N)
    print(stared)
