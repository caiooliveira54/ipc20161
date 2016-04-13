#
# Ana Beatriz Faria Frota - 1615310027
# Mateus Mota de Souza - 1615310016
# Matheus Henrique Araujo Batista - 1615310039
# Nahan Trindade Passos - 1615310021
# Victor Hugo Souza Correia - 1615310024
#

print ("Vamos calcular o tempo aproximado de quanto demorará o seu download?")
print ("Primeiramente...")
tamanho_d = int(input("Insira o tamanho do arquivo para download (MB): "))
velocidade_d = int(input("Insira a velocidade da sua conexão (Mbps): "))

tempo_d_segundos = tamanho_d / velocidade_d
tempo_d_minutos = tempo_d_segundos / 60 #Conversão para minutos

print ("O tempo estimado para o download será %.2f minutos"%(tempo_d_minutos))
