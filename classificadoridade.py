# Classificador de Idade (com idade fixa)

idade = 33  # sua idade atual

# Classificação de acordo com a faixa etária
if 0 <= idade <= 12:
    categoria = "Criança"
elif 13 <= idade <= 17:
    categoria = "Adolescente"
elif 18 <= idade <= 59:
    categoria = "Adulto"
elif idade >= 60:
    categoria = "Idoso"
else:
    categoria = "Idade inválida"

# Exibe o resultado
print(f"Idade: {idade} anos")
print(f"Categoria: {categoria}")
33
