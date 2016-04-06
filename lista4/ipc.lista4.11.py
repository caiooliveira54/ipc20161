"""
Lista 4 questao 11
Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
"""
#Luiz Gustavo Rocha Melo - 1615310015
vetor1 = []
vetor2 = []
vetor3 = []
vetor4 = []
c1 = 0
c2 = 1
v = 10

while (c1 < v):
    x = (input("informe um elemento para a primeira lista: "))
    y = (input("informe um elemento para a segunda lista: "))
    z = (input("informe elementos para a terceira lista: "))
    vetor1.append(x)
    vetor2.append(y)
    vetor3.append(x)
    
    vetor4.append(x)
    vetor4.append(y)
    vetor4.append(z)
    c1 += 1
    c2 += 1

print ("A uniao dos vetores e",vetor4)
