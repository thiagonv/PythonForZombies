'''edificil = ["familia a", "familia b", "familia c"] 
print (edificil[0]) 
print (edificil[1])

print(edificil)

edificil.append("familia d")

print(edificil)

notas = [4, 5, 6, 7]

contador = 0
media = 0 

while contador != 4:
	media = media + notas[contador]
	contador = contador + 1

media = media / contador
print(media)


contador = 0
vetInt = []

while contador !=5:
	n = int(input("Insira o valor %d: " %contador))
	vetInt.append(n)
	contador += 1
print(vetInt)



contador = 0
vetInt = []

while contador !=5:
	n = int(input("Insira o valor %d: " %contador))
	vetInt.append(n)
	contador += 1

vetIntInv = []
while contador !=0:
	n = vetInt[contador - 1]
	print(n)
	vetIntInv.append(n)
	contador -= 1	
print(vetIntInv)

contador = 0 
notas = []
media = 0
while contador !=4: 
	n = float(input("Insira a nota: "))
	notas.append(n)
	media = media + n
	contador += 1
media = media / contador

print("Notas: ", notas)
print("Media ", media)'''

contador = 0
letras = []
vogais = ["a", "e", "i", "o", "u"]
consoantes = 0
while contador < 5:
	n = input("Insira a letra: ")
	letras.append(n)
	contador += 1
	if n not in 'aeiou' : 
		consoantes += 1
print(letras)
print(consoantes)
