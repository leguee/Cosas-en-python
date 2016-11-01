archivo = open("palabras","r")
"""for linea in archivo.readlines():
    print linea"""

contenido = archivo.read()
print contenido
print archivo.mode
print archivo.name
print archivo.encoding

archivo.close()

if archivo.closed: 
	print "El archivo se ha cerrado correctamente"
else: 
	print "El archivo permanece abierto"