velocidade = int(input("Velocidade do carro: "))

if velocidade > 110:
	print("Foi multado")
	multa = (velocidade - 110) * 5
	print("valor da multa: %5.2f" %multa)


minutos = int(input("valor da conta: "))

if minutos < 200:
	total = minutos * 0.2
elif minutos >= 200 and minutos <= 400:
	total = minutos * 0.18
elif minutos > 800:
	total = minutos * 0.8
else: 
	total = minutos * 0.15
print("voce gastou: %5.2f" %total)
