# Introdução ao programa
print("Bem vindo(a) à calculadora de gorjeta")
# Pedindo o valor da conta
conta = round(float(input("Quanto deu a conta?")),2)
# Pedindo o percentual da gorjeta
gorjeta = round(float(input("Quantos % de gojeta você gostaria de oferecer?")),2)
# Transformando o valor informado anterior em decimal
porcentagem_gorjeta = gorjeta / 100
# Pedindo o número de pessoas da mesa
n_pessoas = int(input("Qunatas pessoas vão dividir a conta?"))
# Realizando o cálculo para decidir quanto cada um vai pagar
valor_total = (conta / n_pessoas) * (1 + porcentagem_gorjeta)
# Informando o usuário
print(f"Cada pessoa deve pagar: {valor_total}")
