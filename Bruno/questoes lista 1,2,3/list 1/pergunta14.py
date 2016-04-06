#Bruno de Olliveira Freire - 1615310030
regul_quilos = 50
peso = float(input("Informe o peso total de peixes pescados:\n"))
multa = 0.00

if( peso > regul_quilos ):
    multa = (peso - 50)*4.00
    print("Existe execesso e a multa a ser paga será de %.2f reais"%multa)

else:
    multa = 0.00
    print("Não á excesso e a multa será igual a 0.00")
