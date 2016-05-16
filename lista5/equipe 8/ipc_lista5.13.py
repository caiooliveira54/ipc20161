#
#Introdução a Programação de Computadores
#Prof. Dr. :Jucimar Jr.
#
#Matheus Palheta Barbosa - 1615310019
#Any Mendes Carvalho - 1615310044
#Victor Rafael da Silva e Silva - 1615310025
#

from matriz import*

resultados_jogos = [("Time1", "Time2", 0, 1),
                     ("Time1", "Time3", 1, 3),
                     ("Time2", "Time3", 4, 1)]

times = {}
times["Time1"] = {"PG":0, "GM":0, "GS":0, "SG":0, "V":0, "GA": 0}
times["Time2"] = {"PG":0, "GM":0, "GS":0, "SG":0, "V":0, "GA": 0}
times["Time3"] = {"PG":0, "GM":0, "GS":0, "SG":0, "V":0, "GA": 0}

classificacao = [{"PG":-1}] * len(times)

def atribuir_valores_times(resultados):
    for i in resultados:
        times[i[0]]["GM"] += i[2]
        times[i[0]]["GS"] += i[3]
        times[i[1]]["GM"] += i[3]
        times[i[1]]["GS"] += i[2]
        
        if(i[2] > i[3]):
            times[i[0]]["V"] += 1
            times[i[0]]["PG"] += 2
        elif(i[2] < i[3]):
            times[i[1]]["V"] += 1
            times[i[1]]["PG"] += 2
        else:
            times[i[0]]["PG"] += 1
            times[i[1]]["PG"] += 1
    
    for i in times:
        times[i]["SG"] = times[i]["GM"] - times[i]["GS"]
        if(times[i]["GS"] == 0):
            times[i]["GA"] = times[i]["GM"]
        else:
            times[i]["GA"] = times[i]["GM"]/times[i]["GS"]
            

def imprimir_tabela_jogos(resultados):
    for res in resultados:
        print("%s %d x %d %s" %(res[0], res[2], res[3], res[1]))
        
def definir_classificacao(dados_times):
    for i in dados_times:  
        print("-")
        for c in range(len(classificacao)):
            if(dados_times[i]["PG"] > classificacao[c]["PG"]):
                classificacao[c] = dados_times[i]
                break
        
            
        
atribuir_valores_times(resultados_jogos)

imprimir_tabela_jogos(resultados_jogos)

definir_classificacao(times)

print(classificacao)

#print(times)
        

        
    