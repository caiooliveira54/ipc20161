#Ana Jessye 1615310046
#Franklin Yuri 1615310033
#Bruno de Oliveira Freire- 1615310030
import random
nome=raw_input("digite seu nome:")
numero= random.randint(1,3)
x=0
while x !=1:

    print("\n escolha o numero\n digite 1 para pedra \n digite 2 para tesoura \n digite 3 para papel")
    
    resposta=int(input("digite sua resposta:"))
    
    if resposta==1 and numero==2:
        print(" ganhou miseravel pois pedra vence tesoura \n computador colocou tesoura")
        
    if resposta==1 and numero==3:
        print(" voce perdeu miseravel pois papel vence pedra\n computador colocou papel")
    if resposta==2 and numero==1: 
        print(" perdeu miseravel pois tesoura perde para pedra\n computador colocou pedra")
    if resposta==2 and numero==3:   
        print(" ganhou miseravel pois tesoura vence papel\n computador colocou papel")
    if resposta==3 and numero==1:
        print(" voce ganhou pois papel vence pedra\n computador colocou pedra")
    if resposta==3 and numero==2: 
        print(" perdeu miseravel pois papel perde para tesoura\n computador colocou tesoura")
    if resposta==numero:    
        print("empate miseravel pois computador jogou:",numero)
    x=int(input("digite 1 para sair e outro numero para continuar:")) 
    
    if x==1:
        print("\n-----------------Obrigado por jogar!!!!!--------------------")
    


