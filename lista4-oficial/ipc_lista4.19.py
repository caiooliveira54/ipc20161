lista_sis_opera = ["Windows Server","Unix          ","Linux         ","Netware       ","Mac OS        ","Outro         "]#apenas para a melhorar a estetica da tabela que sera formada;
lista_sis_opera2 = ["Windows Server","Unix","Linux","Netware","Mac OS","Outro"]#para ser usada no final do programa, para dizer qual é o S.O. mais votado;
lista_opcoes = [1,2,3,4,5,6]
lista_votos = [0,0,0,0,0,0]
lista_percentual = []
total = 0
soma = 0
cont = 1
por_cento = "%"

print("Qual o melhor Sistema Operacional para uso em servidores?")
print("Vote usando o numero de uma das opções dadas a seguir:")
print("1- Windows Server\n2- Unix\n3- Linux\n4- Netware\n5- Mac OS\n6- Outro")
cond = True
while cond:
    voto = int(input("Vote aqui: "))
    if voto > 0 and voto <= 6:
        for i in range(6):
            if lista_opcoes[i] == voto:
                lista_votos[i] += 1
        total += 1
    if voto < 0 or voto > 6:
        print("Voto inválido! Por favor, escolha uma das opções a seguir:")
        print("1- Windows Server\n2- Unix\n3- Linux\n4- Netware\n5- Mac OS\n6- Outro")
    if voto == 0:
        total = total
        cond = False
maior = lista_votos[0]
maior_nome = ""
maior_porcentagem = 0

for i in range(6):
    percentual = (lista_votos[i]*100)/(total)
    lista_percentual.append(percentual)
    if maior < lista_votos[i]:
        maior = lista_votos[i]
        maior_nome = lista_sis_opera2[i]
        maior_porcentagem = lista_percentual[i]
print("    Sistema operacional    |   Votos      |    %")
print("___________________________|______________|________")
for i in range(6):
    print("%d - %s         |     %d        |   %.2f%s"%(cont,lista_sis_opera[i],lista_votos[i],lista_percentual[i],por_cento))
    cont += 1
print("___________________________|______________|________")
print("Total                      |     %d        |  100%s  "%(total,por_cento))
print("___________________________|______________|________")
print("O Sistema Operacional mais votado foi %s, com %d voto(s), correspondendo a %.2f%s dos votos"%(maior_nome,maior,maior_porcentagem,por_cento))