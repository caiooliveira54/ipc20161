#
#Programa Lista 4, questão 15;
#Felipe Henrique Bastos Costa - 1615310032;
#
lista = [] # Vetor que vai receber as notas inseridas pelo usuário
listainv = [] # Vetor que vai receber as notas inseridas da forma inversa
cond = True # Condição para tornar o 'while' um loop até ser quebrado com o -1
cont1 = 0 
cont2 = 0
cont3 = 0
cont4 = 0
soma = 0 # Receberá todos os valores e somará-los

while(cond): # Enquanto for verdade 
    nota = float(input("Informe uma nota(para encerrar o programa, informe -1):\n")) # Solicitará notas
    if(nota == -1): # Se for -1, encerrará o programa
        soma = soma
        cont1 = cont1
        cond = False
    else: # Caso não, adicionará nota ao vetor lista e somará os valores e o contador será incrementado 
        lista.append(nota)
        soma += nota
        cont1 += 1
media_notas = (soma)/cont1 # 
v = cont1 - 1 # Último elemento do vetor lista

while(cont2 <= v): # Enquanto for verdadeira
    x = lista[v] # Adicionará os últimos números do vetor lista ao vetor listainv
    listainv.append(x)
    v -= 1 # Decrementando o contador
    
for i in range(cont1): # Verificará no vetor...
    if(lista[i] > media_notas):  # Quantos números estão acima da média
        cont3 += 1
    if(lista[i] < 7): # Quantos números são menores que sete
        cont4 += 1
print("A quantidade de valores lidos foi de %d"%cont1)
print("Os valores informados foram:\n%s"%lista)
print("A lista inversa, com os elementos um abaixo do outro e:")
for i in range(cont1):
    print(listainv[i])
print("A soma dos valores dentro da lista e: %.2f"%soma)
print("A media geral das notas e: %.2f"%media_notas)
print("A quantidade de notas acima da media geral e(sao): %d"%cont3)
print("A quantidade de notas abaixo de sete e(sao): %d"%cont4)
print("Obrigado por usar nossos serviços!")
