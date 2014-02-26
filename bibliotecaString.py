import string 

texto = 'Alice foi atrás do coelho, mas não o encontrou'
print (texto)

texto = texto.replace(',', '')
texto = texto.lower()
print (texto)

texto = texto.split()
print (texto)

dic = {}
for palavra in texto:
	if palavra not in dic:
		dic[palavra] = 1
	else: 
		dic[palavra] += 1

print(dic)

texto = 'alice caiu no buraco'
print (texto)
texto = texto.split()

for palavra in texto:
	if palavra not in dic:
		dic[palavra] = 1
	else: 
		dic[palavra] += 1

print(dic)

