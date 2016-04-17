tamanho = float(input("Tamanho do arquivo em mb:\n"))
velocidade = float(input("Velocidade do link:\n"))

tempo = (tamanho)/(velocidade/60)

print("Tempo estimado:",tempo)