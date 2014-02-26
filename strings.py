#checar se a palavra é palindrome

palavra = input ('Palavra: ')

if palavra == palavra[::-1]:
	print("Eh palindrome")

k = 0
troca = ""
while k < len(palavra):
	if palavra[k] in 'aeiou':
		troca = troca + '*'
	else:
		troca = troca + palavra[k]
	k += 1
print("Nova palavra %s" %troca)


meses = ['janeiro', 'fevereiro', 'marco', 'abril', 'maio']

dia, mes, ano = input("Insira a data no formato dd/mm/aaaa: ").split('/')

print('%s de %s de %s' %(dia, meses[int(mes) - 1], ano))
