#
# Questao 7 da lista 6 de "Recursão";
# Professor: Jucimar Junior;
#
# Alunos;
# Caio de Oliveira Martins - 1615310031;
# Lorene da Silva Marques - 1615310013;
# Nadine da Cunha Brito - 1615310040;
#

#coding: utf-8
def inverter_lista(lista, limite, lista_i):
    if limite == 0:
        return lista_i
    else:
        inv = lista[limite-1]
        lista_i.append(inv)
        return inverter_lista(lista, limite-1, lista_i)

lista = []
lista_i = []
limite = 10
print("Inversão de lista de até 100 números reais.")
for i in range(limite):
    print("Número %d" % (i+1))
    n = float(input("Digite um termo real: "))
    lista.append(n)

lista_i_final = inverter_lista(lista, limite, lista_i)

print("A ordem inversa da lista\n%s\né:\n%s" % (lista, lista_i_final))
print("\nObrigado por usar este programa! :D")