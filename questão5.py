valor_hora = float(input("qual valor da hora"))
horas_trabalhadas = float(input("quantas horas trabalhadas"))

sal_bruto = valor_hora * horas_trabalhadas
ir = sal_bruto * 0.11
inss = sal_bruto * 0.08
sindicato = sal_bruto * 0.05
salario_liquido = sal_bruto - ir - inss - sindicato
print(f"""salario bruto R${sal_bruto}
    salario liquido R${sal_liquido}
    IR R${ir}
    INSS R${inss}
    sindicato R${sindicato}""")
