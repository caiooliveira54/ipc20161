print("Codigo de erro:\n1 - necessita de esfera\n2 - necessita de limpeza\n3 - necessita troce de cabo\n4 - quebrado ou inutilizado\n0 - sair")
codigo_erro = int(input("Digite o codigo de erro: "))
erros = [0] * 4
total_erros = 0
while codigo_erro != 0:
    if(codigo_erro < 5):
        erros[codigo_erro - 1] = erros[codigo_erro - 1] + 1
        total_erros = total_erros + 1
    else:
        print("Codigo invalido")
    codigo_erro = int(input("Digite o codigo de erro: "))
    
print("Situacao                    Quantidade   Percentual")
print("1- Necessita de esfera              %d          %d%%" % (erros[0], (erros[0]/total_erros)*100))
print("2- Necessita de limpeza             %d          %d%%" % (erros[1], (erros[1]/total_erros)*100))
print("3- Necessita troca de cabo          %d          %d%%" % (erros[2], (erros[2]/total_erros)*100))
print("4- quebrado ou inutlizado           %d          %d%%" % (erros[3], (erros[3]/total_erros)*100))