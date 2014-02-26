from random import randint
print ('ola!')
sorteado = randint (1, 100)
chute = 0
while chute != sorteado:
	g = input ('chute um numero: ')
	chute = int(g)
	if chute == sorteado:
		print ('Venceu')
	else:
		if chute > sorteado:
			print ('alto')
		else:
			print ('baixo')
print ('fim do jogo')