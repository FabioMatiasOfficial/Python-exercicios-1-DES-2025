media01 = int(input("Digite o valor da média da avaliação"))
media02 = int(input("Digite o valor da média da avaliação"))
media03 = int(input("Digite o valor da média da avaliação"))
valor = media01 or media02 or media03
if valor >= 7 :
    print("Você foi aprovado!")
elif valor >= 5 :
    print("Você está em treinamento")
elif valor < 7 :
    print("Você está em treinamento.")
else:
    print("Você foi aprovado!")
