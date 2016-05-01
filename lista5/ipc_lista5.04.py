#Introducao a programacao de computadores;
#Professor: Jucimar Junior;
#Felipe Henrique Bastos Costa - 1615310032;
#Bruno de Oliveira freire - 1615310030;
#Samuel Silva de França- 1615310049;
#Lista 5, questao 4;
from matriz import*

linhas = int(input("Informe quantas linhas tem a matriz: "))
colunas = int(input("Informe quantas colunas tem a matriz: "))
matrizA = gerar_matriz(linhas,colunas)
mostrar_matriz(matrizA,linhas)
print(verificar_numeros_repetidos(matrizA,linhas,colunas))