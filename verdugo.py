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

# Numero de lestras de la palabra elegida
n_pal = len(pal_azar)

adiv = '_ ' * n_pal # Para visualizar el numero de letras

i = 0 # Iterador de intentos

# Iteramos el numero de intentos
while i < 6:
    print(adiv)
    print('Numero de intentos:', i)
    letra = input('Escribe una letra: ')

    if letra in list(pal_azar):
        print('Letra correcta')
        ind = pal_azar.index(letra)
        pos = 2 * ind - 1
        adiv = str((list(pal_azar)).pop(pos))
    else:
        print('Letra incorrecta')
        i += 1

print(pal_azar)