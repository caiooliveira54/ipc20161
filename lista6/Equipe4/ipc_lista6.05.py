def somar(numero):
    if numero == 1:
        return 1
    else:
        return numero + somar(numero-1)

print ("Somatório de 1 até o N-ésimo termo (1 + 2 + 3 + ... + N-ésimo = ?)")
numero = int(input("Qual o N-ésimo termo? "))
print ("\nO somatório de 1 até %d é:"%(numero), somar(numero))
