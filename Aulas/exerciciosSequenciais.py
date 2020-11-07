# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 23:30:07 2020

@author: Maximo
"""
def get_menu_choice():
    def print_menu():       ## Your menu design here
        print (30 * "-" , "Estrutura Sequencial" , 30 * "-")
        print ("1º Faça um Programa que mostre a mensagem 'Alo mundo' na tela. ")
        print ("2º Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].")
        print ("3º Faça um Programa que peça dois números e imprima a soma.")
        print ("4º Faça um Programa que peça as 4 notas bimestrais e mostre a média.")
        print ("5º Faça um Programa que converta metros para centímetros.")
        print ("6º Faça um Programa que peça o raio de um círculo, calcule e mostre sua.")
        print ("7º Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.")
        print ("8º Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês, calcule e mostre o total do seu salário no referido mês.")
        print ("9º Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius C = 5 * ((F-32) / 9).")
        print (67 * "-")
  
    loop=True
    while loop:          ## o laço só vai parar quando o loop = False
        print_menu()    ## mostra menu
        escolha = input("Escolha o nº do exercicio: ")
        if escolha == '1':
            #1º Faça um Programa que mostre a mensagem "Alo mundo" na tela.
            print("Hello Word!!!")
            loop = False
        elif escolha == '2':
            print(input("Informe um numero: "))
            loop = False
        elif escolha == '3':
            n1=int(input("Informe o primeiro numero: "))
            n2=int(input("Informe o segundo numero: "))

            print("A Soma foi "+str(n1+n2))
            loop = False
        elif escolha == '4':
            n1=int(input("Informe a primeira nota: "))
            n2=int(input("Informe a segunda nota: "))
            n3=int(input("Informe a terceira nota: "))
            n4=int(input("Informe a quarta nota: "))
            
            print("A média é ",(n1+n2+n3+n4)/4)
            loop = False
        elif escolha == '5':
            metros = float(input("Metros a ser convertidos: "))
            
            cent = metros * 1000
            
            print(str(cent)+"cm")   
            loop = False
        elif escolha == '6':
            pi = 3.14
            r = float(input("Digite a área do circulo em metros: "))
            
            a = pi * (r * r)
            
            print("A área do circulo é ",a,"m2")  
            loop = False
        elif escolha == '7':
            lado = float(input("Informe o valor do lado: "))
            area = lado * lado
            dobro = area * 2
            print("A área é: ",area," e o dobro é :",dobro)  
            loop = False
        elif escolha == '8':
            valhora = float(input("Informe o valor da hora: "))
            numhora = float(input("Informe o numeros de horas trabalhadas: "))
            
            print("Seu salário é de R$ ",numhora*valhora)  
            loop = False
        else:
            print("Opção errada.")
            loop = False
    return 


print(get_menu_choice())