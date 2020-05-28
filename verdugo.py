import random

# Presentacion del juego
print('''
JUEGO DEL VERDUGO\n
\nEn este solo tendremos 6 intentos para adivinar una palabra.

''')

# Lista de palabras que se adivinaran
palabras = ['manzana', 'gato', 'silla', 'cocina', 'fotografia', 'mesa', 'lapicero', 'perro', 'durazno']

# Elegimos una palabra al azar
pal_azar = random.choice(palabras)
list_let = list(pal_azar)

# Numero de lestras de la palabra elegida
n_pal = len(pal_azar)

adiv = []
for n in range(n_pal):
    adiv.append("_")

i = 0 # Iterador de intentos

# Iteramos el numero de intentos
while i < 6:
    print(adiv)
    print('Numero de intentos:', i)
    letra = input('Escribe una letra: ')

    if letra in list_let:
        print('Letra correcta')
        ind = pal_azar.index(letra)
        adiv[ind] = letra
        
    else:
        print('Letra incorrecta')
        i += 1

print(pal_azar)