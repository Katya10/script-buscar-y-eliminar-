import os

ruta="/home/katya/Documentos/borrar"
lstFiles = []


# primer for que hace la busque en la ruta del directorio con la extencion dada
for root, dirs, files in os.walk(ruta):
    for fichero in files:
        (nombreFichero, extension) = os.path.splitext(fichero)
        if(extension == ".txt"):
            lstFiles.append(nombreFichero+extension)
            print 'Los archivos encontrados son: ',(nombreFichero+extension)

numero = int(input('quieres eliminar los archivos encontrados? 1 es si, 2 es no: '))
borrar=1
no=2


# vamos hacer una sentencia para confirmar si queremos borrar los archivos
if (numero==borrar):
	print 'archivos se eliminaran'
	# este for eliminara los archivos
	for parent, dirnames, files in os.walk(ruta):
		for fn in files:
			if fn.lower().endswith('.txt'):
				os.remove(os.path.join(parent, fn))
	print 'se eliminaron los archivos'

if (numero==no):
	print 'archivos no se borraran'