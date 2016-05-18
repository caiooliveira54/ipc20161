def inverter (n):
    ac = 0
    if len (str(n)) == 1:
        return n
    else:
        return str(n % 10) + str(inverter(n // 10))
        

num = int(input("Digite um numero: "))
print(inverter(num))
