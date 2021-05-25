import numpy as np
import matplotlib.pyplot as plt

def convertirAListaNums(listaDeStrings):
    return np.float_(list(listaDeStrings.split(" ")))

# Datos de la funcion f y g
nf = int(input("Ingrese el valor de n donde comienza f[n]: "))
imagenF = input("Ingrese la primera secuencia de valores: ")
imagenF = convertirAListaNums(imagenF)
dominioF = np.arange(nf, len(imagenF) + nf, 1)

ng = int(input("Ingrese el valor de n donde comienza g[n]: "))
imagenG = input("Ingrese la segunda secuencia de valores: ")
imagenG = convertirAListaNums(imagenG)
dominioG = np.arange(ng, len(imagenG) + ng, 1)

# Configuración de figura y axes
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7.5, 7))

# Configuracion de ploteo
ax1.stem(dominioF, imagenF, '.', label='f[n]', markerfmt='C0o')
ax1.stem(dominioG, imagenG, '.', label='g[n]', markerfmt='C1o', linefmt='C1--')
ax1.set_title('Grafica de f[n] y g[n]')
ax1.set_xticks(dominioF[ : : 1])
ax1.grid(color='#0066cc', ls='--', lw=0.1)
ax1.ticklabel_format(style='plain', axis='y')
ax1.legend()
ax1.axhline(y=0, color='k')
ax1.axvline(x=0, color='k')

# Convolucion
imagenConvolucion = np.convolve(imagenF,imagenG)
anchoPulso = len(imagenF) + len(imagenG) - 1
primerN = nf + ng
dominioConvolucion = np.arange(primerN, anchoPulso + primerN, 1)

# Configuracion de ploteo
ax2.stem(dominioConvolucion, imagenConvolucion, '.', label='f*g[n]', markerfmt='ro', linefmt='r-')
ax2.set_title('Convolucion entre las dos funciones')
ax2.set_xticks(dominioConvolucion[ : : 1])
ax2.grid(which='major', axis='both', color='#0066cc', ls='--', lw=0.1)
ax2.ticklabel_format(style='plain', axis='y')
ax2.legend()
ax2.axhline(y=0, color='k')
ax2.axvline(x=0, color='k')

plt.tight_layout()
plt.show()
