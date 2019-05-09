a = "string"

try:
	print(b)
except NameError:
	print("ha ocurrido un error")
else:
	print("no hay error")
finally:
	print("siempre se ejecuta")