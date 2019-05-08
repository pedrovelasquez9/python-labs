a = 10
b = 5

#No hay switch así que podemos poner tantos elif como necesitemos
#condicional if

if(a<b) :
	print("a es menor que b")
elif(a==b):
	print("a es igual a b")
else:
	print("a es mayor que b")

if(a<b and b>2):
	print('comparación con and')
else:
	print('else de comparación con and')

if(a<b or b<a):
	print('comparación con or')

if not a==b:
	print('no son iguales')

#Búsqueda con if in

lista = ['lunes', 'martes', 'miercoles']
if "martes" in lista : 
	print('si está el martes')
else:
	print("No está el martes")

# operadores
# !=
# ==
# <
# >
# >=
# <=

