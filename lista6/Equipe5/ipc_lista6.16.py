def fazerfatduplo(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fazerfatduplo(num-2)
    
   
num = int(input("Digite um numero natural impar: "))
print(fazerfatduplo(num))