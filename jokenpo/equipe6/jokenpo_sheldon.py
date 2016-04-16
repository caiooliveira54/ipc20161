"""
Lorene Marques 1615310013
Nadine Brito 1615310040
"""

import random

cond = True

nome = input ("Digite seu nome: ")

while cond:
       num = random.randint(1,5)

       tent = int(input("Digite 1 = pedra ou 2 = papel ou 3 = tesoura ou 4 = lagarto ou 5 = Spock: \n"))

       if tent == 1:
              if num == 1:
                     print ("Computador jogou: Pedra")
                     print (nome,"jogou: Pedra")
                     print ("Empatou")
              elif num == 2:
                     print ("Computador jogou: Papel")
                     print (nome,"jogou: Pedra")
                     print (nome,"você perdeu!")
              elif num == 3:
                     print ("Computador jogou: Tesoura")
                     print (nome,"jogou: Pedra")
                     print (nome,"você ganhou!")
              elif num == 4:
                     print ("Computador jogou: Lagarto")
                     print (nome,"jogou: Pedra")
                     print (nome,"você ganhou!")
              else:
                     print ("Computador jogou: Spock")
                     print (nome,"jogou: Pedra")
                     print (nome,"você perdeu!")

       elif tent == 2:
              if num == 1:
                     print ("Computador jogou: Pedra")
                     print (nome,"jogou: Papel")
                     print (nome,"você ganhou!")
              elif num == 2:
                     print ("Computador jogou: Papel")
                     print (nome,"jogou: Papel")
                     print ("Empatou!")
              elif num == 3:
                     print ("Computador jogou: Tesoura")
                     print (nome,"jogou: Papel")
                     print (nome,"você perdeu!")
              elif num == 4:
                     print ("Computador jogou: Lagarto")
                     print (nome,"jogou: Papel")
                     print (nome,"você perdeu!")
              else :
                     print ("computador jogou: Spock")
                     print (nome,"jogou: Papel")
                     print (nome,"você ganhou!")

       elif tent == 3:
              if num == 1:
                     print ("Computador jogou: Pedra")
                     print (nome,"jogou: Tesoura")
                     print (nome,"você perdeu!")
              elif num == 2:
                     print ("Computador jogou: Papel")
                     print (nome,"jogou: Tesoura")
                     print (nome,"você ganhou!")
              elif num == 3:
                     print ("Computador jogou: Tesoura")
                     print (nome,"jogou: Tesoura")
                     print ("Empatou!")
              elif num == 4:
                     print ("Computador jogou: Lagarto:")
                     print (nome,"jogou: Tesoura")
                     print (nome,"você ganhou!")
              else:
                     print ("Computador jogou: Spock")
                     print (nome,"jogou: Tesoura")
                     print (nome,"você perdeu!")

       elif tent == 4:
              if num == 1:
                     print ("Computador jogou: Pedra")
                     print (nome,"jogou: Lagarto")
                     print (nome,"você perdeu!")
              elif num == 2:
                     print ("Computador jogou: Papel")
                     print (nome,"jogou: Lagarto")
                     print (nome,"você ganhou!")
              elif num == 3:
                     print ("Computador jogou: Tesoura")
                     print (nome,"jogou: Lagarto")
                     print (nome,"você perdeu!")
              elif num == 4:
                     print ("Computador jogou: Lagarto:")
                     print (nome,"jogou: Lagarto")
                     print ("Empatou!")
              else:
                     print ("Computador jogou: Spock")
                     print (nome,"jogou: Lagarto")
                     print (nome,"você ganhou!")

       elif tent == 5:
              if num == 1:
                     print ("Computador jogou: Pedra")
                     print (nome,"jogou: Spock")
                     print (nome,"você ganhou!")
              elif num == 2:
                     print ("Computador jogou: Papel")
                     print (nome,"jogou: Spock")
                     print (nome,"você perdeu!")
              elif num == 3:
                     print ("Computador jogou: Tesoura")
                     print (nome,"jogou: Spock")
                     print (nome,"você ganhou!")
              elif num == 4:
                     print ("Computador jogou: Lagarto:")
                     print (nome,"jogou: Spock")
                     print (nome,"você perdeu!")
              else:
                     print ("Computador jogou: Spock")
                     print (nome,"jogou: Spock")
                     print ("Empatou!")

       else:
              print("Jogada inválida")
              cond = True
       jognov = int (input("\nJogar novamente? 1 = Sim ou 2 = Não: "))
       if jognov == 1:
              cond = True
       elif jognov == 2:
              cond = False
       else:
              print("Resposta inválida")
