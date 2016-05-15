def chamar_numero():
    numero = int(input("digite um numero: "))
    return numero

def fatorar_numero(numero):
    if (numero == 1) or (numero == 0):
        return 1
    else:
        n = numero - 1
        return numero * fatorar_numero(n)
    
def analisar_combinacao(numero,acm):
    resultado = fatorar_numero(numero) / (fatorar_numero(acm) * fatorar_numero(numero - acm))
    return resultado

def fazer_triangulo(numero):
    for numero in range(0,numero + 1):
        triangulo = []
        for acm in range(0,numero + 1):
            triangulo.append(int(analisar_combinacao(numero, acm)))
        print (triangulo)

numero = chamar_numero()
fazer_triangulo(numero)

