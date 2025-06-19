salario = float(input("Digite o salário mensal de Renata: R$ "))
parcela = float(input("Digite o valor da parcela do financiamento: R$ "))

if salario <= 3000:
    print("Financiamento negado, salário abaixo do minímo exigido.")
elif parcela > salario * 0.35:
    print("Financiamento negado, parcela acima de 35% do salário.")
else:
    print("Financiamento aprovado!")
