# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 16:47:16 2020

@author: Maximo
"""

from heroi import Heroi

super_man = Heroi()

homem_aranha = Heroi(False, False, True, "")
print(homem_aranha.voa)
print(homem_aranha.lanca_teia)

he_man = Heroi(False, True, False, "Eu tenho a força")
he_man.falar()

