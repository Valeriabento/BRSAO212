# Verificador de Ano Bissexto

# Solicita o ano ao usuário
ano = int(input("Digite um ano: "))

# Verifica se é bissexto
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    resultado = "Bissexto"
else:
    resultado = "Não é bissexto"

# Exibe o resultado
print(f"O ano {ano} é {resultado}.")
