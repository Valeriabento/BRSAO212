# Calculadora de IMC (com valores fixos)

# Dados da pessoa
peso = 70.0      # em kg
altura = 1.65    # em metros

# Calcula o IMC
imc = peso / (altura ** 2)

# Classifica o IMC
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"

# Exibe os resultados
print(f"Peso: {peso} kg")
print(f"Altura: {altura} m")
print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")
