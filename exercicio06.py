hora_atual = int(input("Digite o horário que você está acessando a plataforma"))

if 9 <= hora_atual <= 21:
    print("A plataforma está funcionando perfeitamente.")
else:
    print("A plataforma está fora do horário de funcionamento.")