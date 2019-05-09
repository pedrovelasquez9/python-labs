a = "hola"
b = "strings"

#concatenado
c = a + " " +  b 
d = "concatenando: %s %s" %(a, b)
e = "concatenando: {0} {1}" .format(a,b)

print(c)
print(d)
print(e)

#Multiplicado 
f = a+" \n"
print(f*5)

g = a
g+=" cualquier cosa"
print(g)

#longitud
print(len(g))

#busqueda
print(g.find('cualquier'))

#Uppercase y lowercase
print(g.capitalize())
print(g.lower())
print(g.upper())

#reemplazo
print(g.replace("cualquier", "una"))

#imprimir piezas
print(g[:5])

#\n > salto de línea 
print("string con \"comillas\"")
print("string con 'comillas simples'")