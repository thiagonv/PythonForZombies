n = 1
soma = 0

while n <= 10:
	x = int(input("digite o %d numero: " %n))
	soma = soma + x
	n = n + 1
	media = soma / 10
print ("Soma %d" %soma)
print ("Media: %5.2f" %media)



inp = int(input("Fatoria: "))
fat = 1
n = 1

while n <= inp:
	fat = fat * n
	n = n + 1
print ("fatorial: %d = %d" %(n, fat))