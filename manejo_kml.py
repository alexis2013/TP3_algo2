from random import choice

colores = ("ff0000ff", "ff00ffff", "ffff0000", "ff00ff00", "ff800080", "ff0080ff", "ff336699", "ffff00ff")

def escribir_kml(nombre_archivo, camino, ciudades, comando):

	color = choice(colores)
	cant_ciudades = len(camino)
	with open(nombre_archivo, "a+") as archivo:
		archivo.write("\t\t<name>{}</name>\n".format(comando))
		for i in range(cant_ciudades):
			archivo.write("\t\t\t<Placemark>\n")
			archivo.write("\t\t\t\t<name>{}</name>\n".format(camino[i-1]))
			archivo.write("\t\t\t\t<Point>\n")
			archivo.write("\t\t\t\t\t<coordinates>")
			archivo.write("{}, {}".format(ciudades[camino[i]][0], ciudades[camino[i]][1]))
			archivo.write("</coordinates>\n")
			archivo.write("\t\t\t\t</Point>\n")
			archivo.write("\t\t\t</Placemark>\n")
			archivo.write("\n")
		for i in range(1, cant_ciudades):
			archivo.write("\t\t\t<Placemark>\n")
			archivo.write("\t\t\t\t<LineString>\n")
			archivo.write("\t\t\t\t\t<coordinates>")
			archivo.write("{}, {}".format(ciudades[camino[i-1]][0], ciudades[camino[i-1]][1]))
			archivo.write(" {}, {}".format(ciudades[camino[i]][0], ciudades[camino[i]][1]))
			archivo.write("</coordinates>\n ")
			archivo.write("\t\t\t\t</LineString>\n")
			archivo.write("\t\t\t\t<Style>\n")
			archivo.write("\t\t\t\t\t<LineStyle>\n")
			archivo.write("\t\t\t\t\t\t<color>#{}</color>\n".format(color))
			archivo.write("\t\t\t\t\t</LineStyle>\n")
			archivo.write("\t\t\t\t</Style>\n")
			archivo.write("\t\t\t</Placemark>\n")
			archivo.write("\n")

