num = int(input("Informe o numero inteiro que deseja analisar:\n"))

i = 1
divisores = 0

while i <= num :
    if num%i==0 :
        divisores+=1    
    i+=1
if divisores > 2 or num == 1:
    print("Nao e primo!")
else:
    print("E primo!")