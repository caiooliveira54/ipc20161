# Alexander Emerson Batalha Carlos 1615310051 
A = ["a","b","c","d","e","f","g","h","i","j"]
C = 0
v = len(A)
ac = 0
while C < len(A):
    if A[C] != "a" and A[C] != "e" and A[C] != "i" and A[C] != "o" and A[C] != "u":
        ac = ac + 1
        print(A[C])
    C = C + 1
print("O numero de consoantes são: ",ac)
     
    
     
