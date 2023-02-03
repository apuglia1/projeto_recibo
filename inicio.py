import geocoder

nome1 = input("Insira o seu nome completo: ")
nome2 = input("Insira o nome da pessoa que realizou o pagamento: ")
valor = input("Insira o valor que foi recebido: ")
servico = input("Informe por gentileza qual foi o serviço realizado: ")
local = input("Informe em qual cidade e estado foi realizado o serviço: ")
dia_data = input("Informe a data em que ocorreu o serviço (dia, mês e ano): ")

local_recibo = geocoder.ip('me')

print(f"{'RECIBO' : ^150}")

print("")
print("")
print("")
print("")
print("")
print("")

print(f"Informo para todos os fins que recebi de {nome2} a quantia de R$ {valor}, correspondente a {servico}, serviço este realizado em {local}, em {dia_data}")

print("")
print("")
print("")
print("")
print("")
print("")

print(local_recibo.city, ",")

print("")
print("")
print("")


print(f"{'___________________________________' : ^150}")






