import random

IMÁGENES_AHORCADO = ['''
     +---+
     |   |
         |
         |
         |
         |
  =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
 =========''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
  =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
  =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
 =========''']

# Esta funcion nos permite obtener los indices de la letra que se repite
def index_rep(lista):
    unico = [] # Lista de valores que no se repiten
    list_rep = [] # Lista de indices que se repiten
    rep = {} # Dict de indices como valores de la llave letra repetida

    # Iteramos para obtener el dict de valores repetidos
    for elem in lista:
        # Si no esta en la lista sin repetir lo agregamos 
        if elem not in unico:
            unico.append(elem)
        else:
            # Si no esta en las llaves de dict agregamos el primer indice
            if elem not in rep.keys():
                rep[elem] = [lista.index(elem)]
    
    # Iteramos para comparar cada valor de la lista y encontrar los valores repetidos
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if (lista[i] == lista[j]) and (i not in list_rep):
                rep[lista[i]].append(j)
                list_rep.append(i)
    
    return rep

# Presentacion del juego
print('''
JUEGO DEL VERDUGO\n
\nEn este juego solo tendremos 6 intentos para adivinar las letras de la palabra
\nelegida al azar\n.
''')
print(IMÁGENES_AHORCADO[0], "\n")

# Lista de palabras que se adivinaran
palabras = ['manzana', 'gato', 'silla', 'cocina', 'fotografia', 'mesa', 'lapicero', 'perro', 'durazno']

# Elegimos una palabra al azar
pal_azar = random.choice(palabras)
list_let = list(pal_azar) 

# Obtenemos el dict con los valores repetidos y sus indices
c_rep = index_rep(list_let)

n_pal = len(pal_azar) # Numero de letras de la palabra elegida

adiv = [] # Lista de letras a adivinar
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
        ind = list_let.index(letra)
        if letra in c_rep.keys():
            for k in c_rep[letra]:
                adiv[k] = letra
        else:
            adiv[ind] = letra
        
    else:
        i += 1
        print(IMÁGENES_AHORCADO[i])

    if adiv == list_let:
        print(pal_azar + "\n")
        print("¡FELICITACIONES! Ganaste la partida.")
        break
