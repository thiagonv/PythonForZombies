import random

print(random.choice(['minhoca', 'petito', 'neguinho']))

def embaralha(palavra):
	lista = list(palavra)
	random.shuffle(lista)
	return ''.join(lista)

print(embaralha('thiago'))

listaInt = []
i = 0
while len(listaInt) < 15:
	temp = random.randint(10,100)
	if temp not in listaInt:
		listaInt.append(temp)
		
print(listaInt)