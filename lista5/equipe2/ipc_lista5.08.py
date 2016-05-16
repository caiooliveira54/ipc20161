#
#Introdução a Programação de Computadores
#Prof. Dr. :Jucimar Jr.
#
#Kid Mendes de Oliveira Neto - 1615310011
#Eduardo Maia Freire - 1615310003
#Igor Menezes Sales Vieira - 1615310007
#

def fatorial(n):
    if(n == 1 or n == 0):
        return 1
    else:
        return (n * fatorial(n-1))
def analise_c(n,i):
    analise_combinatoria = fatorial(n)/(fatorial(i)*fatorial(n-i))
    return analise_combinatoria

def triangulo_pascal(n):
    triangulo_vetor = []
    for n in range(0,n+1):                                  
        triangulo_escala = []
        for i in range(0,n+1):
            triangulo_escala.append(int(analise_c(n,i)))
            triangulo_vetor.append(int(analise_c(n,i)))
        print(triangulo_escala)                                          
    print(triangulo_vetor)   

linha = int(input("Numero de linhas do Triangulo de Pascal:\n"))
triangulo_pascal(linha)

