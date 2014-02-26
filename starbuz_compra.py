import urllib.request
import time

def pegaPreco():
	pagina = urllib.request.urlopen(
		'http://beans.itcarlow.ie/prices-loyalty.html')
	texto = pagina.read().decode("utf-8")
	onde = texto.find('>$')
	inicio = onde + 2
	fim = inicio + 4
	return float(texto[inicio:fim])

opcao = input("Comprar agora? S/N ")

if opcao == 'S':
	preco = pegaPreco()
	print ('Comprar! Preco: %5.2f' %preco)
else:
	preco = pegaPreco()
	while preco >= 4.74:
		if preco >= 4.74:
			print(
				'Esperando para comprar. %5.2f' %preco)
			time.sleep(6)
	print('Comprar! Preco: %5.2f' %preco)