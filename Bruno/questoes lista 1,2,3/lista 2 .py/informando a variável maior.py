nota1 = float(input(" digite o número 1 "))
nota2 = float(input(" digite o número 2 "))
nota3 = float(input(" digite o número 3 "))

if( nota1>nota2 and nota1>nota3 ):
    print("nota1 é maior")
if( nota2>nota1 and nota2>nota3 ):
    print("nota2 é maior")
if( nota3>nota1 and nota3>nota2):
    print("nota3 é maior")
if( nota1==nota2==nota3):
    print(" todos os números são iguais ")
if( nota1==nota2 and nota1>nota3 ):
    print("nota1 e nota2 sao maiores")
if( nota1==nota3 and nota1>nota2 ):
    print(" nota1 e nota3 sao maiores ") 
if( nota2==nota3 and nota2>nota1):
    print("nota2 e nota3 sao maiores")
