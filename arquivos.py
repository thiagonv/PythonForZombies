arquivo = open('numeros.txt', 'w')
for linha in range(1,101):
	arquivo.write('%d\n' %linha)
arquivo.close()

arquivo = open('numeros.txt', 'r')
for linha in arquivo.readlines():
	print(linha.rstrip())
arquivo.close()


texto = open('mensagem.txt')
saida = open('cripto.txt', 'w')
for linha in texto.readlines():
	for letra in linha:
		if letra in 'aeiou':
			saida.write('*')
		else:
			saida.write(letra)
texto.close()
saida.close()

def ipOk(ip):
	ip = ip.split('.')
	#print(ip)
	for byte in ip:
		#print(byte)
		#for casa in byte:
		#	print(casa)
		if int(byte) > 255:
			return False
	return True

arq = open('IPS.txt')
validos = open('Validos.txt', 'w')
invalidos = open('Invalidos', 'w')

for linha in arq.readlines():
	if ipOk(linha):
		validos.write(linha)
	else:
		invalidos.write(linha)
arq.close()
validos.close()
invalidos.close()