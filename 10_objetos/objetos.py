class mascota:
	#constructor (el self hace referencia a la misma clase)
	def __init__(self, n, e, a):
		#propiedades
		self.nombre = n
		self.edad = e
		self.altura = a
		self.comida = "para gatos"

	#métodos
	def correr(self):
		return "corriendo"
	
	def getNombre(self):
		return self.nombre
	
	def getEdad(self):
		return self.edad
	
	def getComida(self, adicional):
		return self.comida + " " + adicional

#creo un objeto
gato = mascota("copérnico", 4, 20)

#llamo a sus propiedades o métodos
print(gato.getNombre())
print(gato.getEdad())
print(gato.correr())
print(gato.getComida("con carne"))

#creo otro objeto
perro = mascota("arquímedes", 3, 50)

print(perro.getNombre())

#heredo en otra clase
class salvaje(mascota):
	pass
		
animalSalvaje = salvaje("tigre", 5, 500)
print(animalSalvaje.correr())