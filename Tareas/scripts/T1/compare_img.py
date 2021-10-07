import numpy as np
from PIL import Image, ImageOps
import sys
# Open the image form working directory

def get_image_array(direction):
    color_image = Image.open(direction)

    img = np.array( ImageOps.grayscale(color_image))    # Se crea matriz de tonos grises

    photo = []

    # Extendemos matriz en un arreglo
    for i in img:
        photo += list(i)

    return np.array(photo)

"""
Recibe los arreglos de pixeles de la pauta y del alumno
Retorna el porcentaje (de 0 a 100) de error. 
    0.0   -> Todo bueno
    100.0 -> Todo malo
"""
def compare_photos(pauta, alumno):
    cont_pix = 0                            # Pixeles distintos de 0 que calzan con la pauta
    cont_total = 0                          # Cantidad de pixeles de la pauta distintos de cero

    for i in range(len(pauta)):
        try:
            if pauta[i] != 0:                   # Si el pixel de la pauta es distinto de cero, se cuenta
                cont_total += 1

                if pauta[i] == alumno[i]:       # Si el pixel de la pauta es igual al del alumno, se suma un punto
                    cont_pix += 1
            elif pauta[i] != alumno[i]:         # Si el pixel de la pauta es 0, y el alumno tiene un pixel distinto de 0, se suma el pixel al total (por estar incorrecto) 
                cont_total += 1
        except:
            cont_total +=1
    return (1 - cont_pix / cont_total) * 100


def compare_raw(ground_truth, student_output):
    alumno = get_image_array(student_output)
    pauta = get_image_array(ground_truth)
    return compare_photos(pauta, alumno)

if __name__ == '__main__':
    print(compare_raw(sys.argv[1], sys.argv[2]))
