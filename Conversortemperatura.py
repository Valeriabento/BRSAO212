# Conversor de Temperatura

# Solicita os dados do usuário
temperatura = float(input("Digite a temperatura: "))
origem = input("Digite a unidade de origem (C, F, K): ").upper()
destino = input("Digite a unidade de destino (C, F, K): ").upper()

# Função para converter
def converter_temp(valor, de, para):
    # Converte a unidade de origem para Celsius
    if de == "C":
        celsius = valor
    elif de == "F":
        celsius = (valor - 32) * 5/9
    elif de == "K":
        celsius = valor - 273.15
    else:
        return None

    # Converte de Celsius para a unidade de destino
    if para == "C":
        return celsius
    elif para == "F":
        return (celsius * 9/5) + 32
    elif para == "K":
        return celsius + 273.15
    else:
        return None

# Faz a conversão
resultado = converter_temp(temperatura, origem, destino)

# Exibe o resultado
if resultado is not None:
    print(f"\n{temperatura:.2f} {origem} = {resultado:.2f} {destino}")
else:
    print("\nUnidade inválida! Use apenas C, F ou K.")
