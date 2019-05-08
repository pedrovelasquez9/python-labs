def miFuncion():
	print('mi primera función en python')

#llamado a la función 
miFuncion()

def conParam(i):
	print('recibe', i)

conParam(10)

#con return y parámetro con valor por defecto
def retorno(a, b=0):
	resul = a + b
	return resul 

print(retorno(1,2))

#tupla (una especie de lista que no se puede editar)
tupla = (1, 2, 3, "string")

#imprimir tupla completa
print(tupla)

#imprimir posición
print(tupla[0])

#imprimir x posiciones
print(tupla[0:2])

#recorrer tupla
for i in tupla :
	print(i)

i = 0
while i < len(tupla) :
	print(tupla[i])
	i = i + 1