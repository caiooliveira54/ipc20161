vet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
c = 0
v = len (vet)
ac = 0
while c < v:
    if vet[c] != "a" and vet[c]!= "e" and vet[c] != "i" and vet[c] != "o" and vet[c] != "u":
        ac = ac + 1
        print (vet[c])
    c = c + 1
print ("Numero total de consoantes %d" %ac)
