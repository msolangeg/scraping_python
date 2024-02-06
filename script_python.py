import re
from colorama import Fore
import requests

website = "https://www.vulnhub.com/"
resultado = requests.get(website)

# Se guarda el resultado total de la peticion http
content = resultado.text

# Detectar patron que acompañe la variable que quiero extraer en este caso los titulos.
patron = r"/entry/[\w-]*"

maquinas_repetidas = re.findall(patron, str(content))
#  eliminar elementos repetidos
sin_duplicados = list(set(maquinas_repetidas))

# Crear lista vacía con bucle for sacar lo que no me interesa
maquinas_final = []

for i in sin_duplicados:
    # va recorrer cada entry lo va a quitar y no va a poner nada.
    nombre_maquinas = i.replace("/entry/", "")
    # quiero almacernarlo
    maquinas_final.append(nombre_maquinas) 
    print(nombre_maquinas)
 
 
########################################
# Voy a tomar de referencia la ultima maquina que aparece en la primer pagina para poder saber si agregan alguna nueva y guardare en una variable
maquina_noob = "noob-1"
# Voy a preguntar si existe noob
existe_noob = False

# Recorro la lista de nombres y creo una condicional preguntando si existe noob, si existe la sentencia pasa a true
for a in maquinas_final:
    if a == maquina_noob:
        existe_noob = True
        break
    
#   Usar colorama  
color_verde = Fore.GREEN
color_amarillo = Fore.YELLOW


if existe_noob == True:
     print("\n" + Fore.GREEN + "No hay ninguna maquina nueva")
else:
     print("\n" + color_amarillo + "Máquina nueva")