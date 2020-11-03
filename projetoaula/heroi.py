# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 15:14:15 2020

@author: Maximo
"""
class Heroi:
    
    def __init__(self, voa, possui_arma,lanca_teia, frase_comum):
        print("Executando o init.")
        self.voa = voa
        self.possui_arma = possui_arma
        self.lanca_teia = lanca_teia
        self.frase_comum = frase_comum
    
        
    def falar(self):
        print(self.frase_comum)
        
        
    def detalhar(self):
       if self.voa:
           print("O herói voa.")
       if self.possui_arma:
           print("O herói possui arma.")
       if self.lanca_teia:
           print("O herói lança teia.")    
        
