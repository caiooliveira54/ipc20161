def verificar(cont, numero, escolha):
    while numero%10 != 0:
        resto = numero%10
        if resto == escolha:
            cont +=1
            return verificar(cont, numero//10, escolha)
        else:
            return verificar(cont, numero//10, escolha)
    return cont

cont = 0
print ("Programa que calcula repetição de número")
numero = int(input("Qual o numero que deseja verificar repetição? "))
escolha = int(input("Qual a sua escolha? "))
print ("\nO número %d repete-se %d vez em %d"%(escolha, verificar(cont, numero, escolha), numero))
