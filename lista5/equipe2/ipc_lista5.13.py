#
#Introdução a Programação de Computadores
#Prof. Dr. :Jucimar Jr.
#
#Kid Mendes de Oliveira Neto - 1615310011
#Eduardo Maia Freire - 1615310003
#Igor Menezes Sales Vieira - 1615310007
#

def tabela(time1,time2):
    print("\n----------------Tabela------------------------")
    print("%s|PG    |GM    |GS    |S     |V    |GA    |"%(time))
    print("%s|%s    |%s    |%s    |%s    |%s   |%s    |"%(time1,vet[0],vet[1],vet[2],vet[3],vet[4],vet[5]))
    print("%s|%s    |%s    |%s    |%s    |%s   |%s    |"%(time2,vet1[0],vet1[1],vet1[2],vet1[3],vet1[4],vet1[5]))
    print("-----------------------------------------------\n")
def classificar_time(jogos,numero_times):
    for i in range(numero_times):
        time = input("Nome do time:\n")
        times.append(time)
    cont = 0
    while cont < jogos:
        time1 = input("Nome do time de casa:\n")
        time2 =  input("Nome do time de fora:\n")
        gol_time1 = int(input("Gols time de casa:\n"))
        gol_time2 = int(input("Gols time de fora:\n"))
        gs1 = gol_time2
        gs2 = gol_time1
        s1 = gol_time1 - gs1
        s2 = gol_time2 - gs2
        print("%s,%s,%s,%s"%(time1,time2,gol_time1,gol_time2))
        if(gol_time1 > gol_time2):
            vet[0] = 3
            vet1[0] = 0
            vet[4] = 1
            vet1[4] = 0
        elif(gol_time1 < gol_time2):
            vet[0] = 0
            vet1[0] = 3
            vet1[4] = 1
            vet[4] = 0
        elif(gol_time1 == gol_time2):
            vet[0] = 1
            vet1[0] = 1
            vet[4] = 0
            vet1[4] = 0
        
        vet[1] = gol_time1
        vet1[1] = gol_time2
        vet[2] = gs1
        vet1[2] = gs2
        vet[3] = s1
        vet1[3] = s2
        if(gs1 != 0):
            vet[5] = gol_time1 / gs1
        elif(gs1 == 0):
            vet[5] = gol_time1
        if(gs2 != 0):
            vet1[5] = gol_time2 / gs2
        elif(gs2 == 0):
            vet1[5] = gol_time2
        tabela(time1,time2)
        cont+=1
    
time = "Times"
times = []
vet = [" "," "," "," "," "," "]
vet1 = [" "," "," "," "," "," "]
numero_times = int(input("Quantidade de times:\n"))
jogos = int(input("Quantidade de jogos:\n"))
classificar_time(jogos,numero_times)
        
    
