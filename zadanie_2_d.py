# -*- coding: utf-8 -*-
"""Zadanie 2: d

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1N-6zjUhc6Yeha8m6bYFJoCqg1FuYSB5D
"""

def wyswietl_co_drugi_element(lista_liczb):
    for i in range(0, len(lista_liczb), 2):
        print(lista_liczb[i])


lista_liczb = list(range(10, 20))
wyswietl_co_drugi_element(lista_liczb)