Dia01 = int(input("Digite o tempo necessário para entregar a atividade X"))
Dia02 = int(input("Digite o tempo necessário para entregar a atividade Y"))
Dia03 = int(input("Digite o tempo necessário para entregar a atividade Z"))

if Dia01 < 0 or Dia02 < 0 or Dia03 < 0:
    print("erro número negativo.")
else:
    soma = Dia01 + Dia02 + Dia03
    print(f"tempo total da atividade: {soma} dias")