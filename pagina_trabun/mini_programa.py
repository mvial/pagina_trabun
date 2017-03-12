from os import listdir
from os.path import isfile, join

archivos = [f for f in listdir("equipo") if isfile(join("equipo", f))]

nombres = ["Beatriz Menchaca", "Diego Espinoza", "Francisco de la Lastra", 
			"Ina Gana", "Javier Castello", "Josemaria Mora", "Matias Celedon", 
			"Maria Parot", "Rosario Jimenez", "Sofia Gana", "Santiago Rios", 
			"Salvador Valdes", "Vicente Andriguetti", "Vicente Mariscal"]

cargos = ["", "", "", "", "", "", "", "", "", "", "", "", "", ""]

def armar_miembro(nombre_archivo, nombre, cargo):
	return '''<div class="miembro">
              <img src="equipo/{}" alt="Imagen no disponible" 
              	onerror="this.onerror=null;this.src='img/logo/logo.png';">
                <h6>{}</h6>
                <p>{}</p>
          	</div>
          	'''.format(nombre_archivo, nombre, cargo)

with open("equipo.txt", "w") as archivo:
	for i in range(len(archivos)):
		miembro = armar_miembro(archivos[i], nombres[i], cargos[i])
		archivo.write(miembro)
	#[archivo.write(armar_miembro(archivos[i], nombres[i], cargos[i])) for i in range(len(archivos))]
