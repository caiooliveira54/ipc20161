#Introdução a programação de computadores
#Professor: Jucimar Junior
#Calebe Roberto Chaves da Silva Rebello - 1615310043
#Luiz Gustavo de Rocha Melo - 1615310015

def fatorial(n):                                        
    if n == 1 or n == 0:
        return 1
    else:
        return n * fatorial(n-1)

def analise_c(n,i):                                     
    ac = fatorial(n)/(fatorial(i)*fatorial(n-i))
    return ac


n = int(input("Digite um valor de n:\n"))               
vetor = []

for n in range(0,n+1):                                  
    vet = []
    for i in range(0,n+1):
        vet.append(int(analise_c(n,i)))
        vetor.append(int(analise_c(n,i)))
    print(vet)                                          
print(vetor)                                            
