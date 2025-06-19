distancia = float(input("Por gentileza, digite a distância da nossa loja até sua residência"))

if distancia <= 50:
    print("O valor do frete é R$5,00")
elif distancia <= 150:
    print("O valor do frete é R$15,00")

else:
    print("O valor é R$25,00")


