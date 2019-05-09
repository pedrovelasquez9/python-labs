def crearArchivo():
	#open abre un archivo o lo crea si no existe
	#w escritura, si tiene algo, lo sobreescribe
	#a no sobreescribe, concatena
	#r solo lectura
	#lo crea en el mismo directorio que el .py
	archivo = open("prueba.txt", 'w')
	archivo.write("Pedro Plasencia \n")
	archivo.write("Instagram: @pedrovelasquez9 \n")
	archivo.write("Full Stack Web Developer")
	archivo.close()

#leer el archivo
def leer():
	archivo = open('prueba.txt', 'r')
	row = archivo.readline()
	
	while row != "" :
		print(row)
		row = archivo.readline()
	archivo.close()

crearArchivo() 
leer()
