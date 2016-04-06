"""Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma.
O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados.
Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor.
Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete.
O formato da saída foi dado pela empresa, e é o seguinte:
Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outro                     150    2%
-------------------     -----
Total                    8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos."""
#ipc_lista4.19
#Thiago Santos Borges - Matrícula - 1615310023
#

sistema = ["1-Windows Server             ","2-Unix                       ","3-Linux                      ","4-Netware                    ","5-Mac OS                     ","6-Outro                      "]
#sistema = ["1-Windows Server","2-Unix","3-Linux","4-Netware","5-Mac OS","6-Outro"]
nomes = ["Windows Server","Unix","Linux","Netware","Mac OS","Outro"]

cond = True
taxas = []
contvotos = [0,0,0,0,0,0]
maior = 0
soma = 0
votos = 0
nome = ""

def taxa (dado1,dado2):
   return (dado1 * 100) / dado2
    
for i in sistema:
    print(i) 

while cond:
    voto = int(input("Informe valor de 1-6(0=sair):"))
    if voto == 1:
        contvotos[0] = contvotos[0] + 1
        soma = soma + 1
    elif voto == 2:
        contvotos[1] = contvotos[1] + 1
        soma = soma + 1
    elif voto == 3:
        contvotos[2] = contvotos[2] + 1  
        soma = soma + 1
    elif voto == 4:
        contvotos[3] = contvotos[3] + 1
        soma = soma + 1
    elif voto == 5:
        contvotos[4] = contvotos[4] + 1
        soma = soma + 1
    elif voto == 6:
        contvotos[5] = contvotos[5] + 1
        soma = soma + 1
    elif voto == 0:
        cond = False
    else:
        print("Informe um valor valido!")


taxas.append(taxa(contvotos[0],soma))
taxas.append(taxa(contvotos[1],soma))
taxas.append(taxa(contvotos[2],soma))
taxas.append(taxa(contvotos[3],soma))
taxas.append(taxa(contvotos[4],soma))
taxas.append(taxa(contvotos[5],soma))


for i,k,p in zip(nomes,contvotos,taxas):
    if k >= maior:
        nome = i
        votos = k
        maior = p
print(" - Sistema Operacional     -     Votos     -     %     - ")
for i,k,p in zip(nomes,contvotos,taxas):
    print("   %s          %d             %.2f"%(i,k,p))

print("\nTotal                             %d"%soma)

print("O Sistema Operacional mais votado foi o %s, com %d votos, correspondendo a %.2f porcento dos votos."%(nome,votos,maior))







