distancia = float(input("Digite a distância percorrida"))
tempo = float(input("Digite o tempo gasto "))
v_media = distancia / tempo
if v_media < 5 :
    print("A velocidade foi lenta")
elif v_media >=5 <= 10 :
    print("A velocidade foi moderada")
else:
    print("A velocidade foi rápida")