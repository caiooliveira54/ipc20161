#Introduçao a Programação de Computadores
#Professor: Jucimar Junior
#Bruno de Oliveira Freire - 1615310030
#Igor Menezes Sales Vieira - 1615310007
#Matheus Mota de Souza - 1615310016
#Nadine da Cunha Brito - 1615310040
#Nickso Patrick Façanha Calheiros - 1615310059
#Thiago Santos Borges - 1615310023
#

alto = 0
baixo = 99999999999999999999999999
gordo = 0
magro = 99999999999999999999999999
cond = True
soma1 = 0
soma2 = 0
numero_loops = 0


while cond :
    n = int(input("Informe 1 para continuar ou 0 para parar o programa:\n"))
    if n == 1:
        codigo = float(input("Informe o codigo do cliente: "))
        peso = float(input("Informe o peso do cliente: "))
        altura = float(input("Informe a altura do cliente: "))
        if peso >= gordo :
            gordo = peso
            codigo_peso_g = codigo
        if peso <= magro :
            magro = peso
            codigo_peso_m = codigo
        if altura >= alto :
            codigo_altura_a = codigo
            alto = altura
        if altura <= baixo :
            codigo_altura_b = codigo
            baixo = altura
        soma1+=altura
        soma2+=peso
        numero_loops+=1
        
    if n == 0 :
        cond = False
media_altura = soma1/numero_loops
media_peso = soma2/numero_loops
print("O codigo do mais gordo e %.0f, com peso %.2f"%(codigo_peso_g,gordo))
print("O codigo do mais magro e %.0f, com peso %.2f"%(codigo_peso_m,magro))
print("O codigo do mais baixo e %.0f, com altura %.2f"%(codigo_altura_b,baixo))
print("O codigo do mais alto e %.0f, com altura %.2f"%(codigo_altura_a,alto))
print("A media das alturas e %.2f"%media_altura)
print("A media dos pesos e %.2f"%media_peso)
