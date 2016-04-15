"""
Lorene Marques 1615310013
Nadine Brito 1615310040
"""

import random

cond = True

nome = input("Digite seu nome: ")

while cond :
       num = random.randint(1,3)              
       tent = int(input("Digite 1 = pedra ou 2 = papel ou 3 = tesoura: \n"))

       if tent == 1:
              if num == 3:
                     print ("Computador jogou: Tesoura")
                     print (nome,"jogou: Pedra")
                     print ("Você ganhou!")
              elif num == 2:
                     print ("Computador jogou: Papel")
                     print (nome,"jogou: Pedra")
                     print ("Você perdeu!")
              else:
                     print ("Computador jogou: Pedra")
                     print (nome,"jogou: Pedra")
                     print ("Empatou!")
                     

       elif tent == 2:
              if num == 1:
                     print ("Computador jogou: Pedra")
                     print (nome,"jogou: Papel")
                     print ("Você ganhou!")
              elif num == 3:
                     print ("Computador jogou: Tesoura")
                     print (nome,"jogou: Papel")
                     print ("Você perdeu!")
              else:
                     print ("Computador jogou: Papel")
                     print (nome,"jogou: Papel")
                     print ("Empatou!")

       elif tent == 3:
              if num == 2:
                     print ("Computador jogou: Papel")
                     print (nome,"jogou: Tesoura")
                     print ("Você ganhou!")
              elif num == 1:
                     print ("Computador jogou: Pedra")
                     print (nome,"jogou: Tesoura")
                     print ("Você perdeu!")
              else:
                     print ("Computador jogou: Tesoura")
                     print (nome,"jogou: Tesoura")
                     print ("Empatou!")

       else:
              print ("Jogada inválida.")
              cond = True

       jognov = int(input("\nJogar novamente? 1 = Sim // 2 = Não: "))
       if jognov == 1:
              cond = True
       elif jognov == 2:
              cond = False     
