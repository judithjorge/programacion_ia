"""Problema 2. Frecuencia de palabras en un texto. 
Escribe una función que reciba por parámetro una lista de palabras y la ruta a un fichero de texto y devuelva 
un diccionario que muestre cuantas veces aparecen las distintas palabras de la lista en el fichero de texto.
Haz un pequeño programa que la ponga a prueba. 
    Requisitos: 
    1. Eliminar signos de puntuación y convertir todo a minúsculas. 
    2. Usar un diccionario donde la clave sea la palabra y el valor su frecuencia. 
    3. Mostrar las palabras y sus frecuencias de forma ordenada por la palabra. """

import string  

def count_word_frequency(word_list, file_path):
    #Abrimos y leemos el fichero
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    #convertimos todo a minusculas
    text = text.lower()

    #Eliminamos los signos de puntuacion usando str.translate y str.maketrans
    text = text.translate(str.maketrans('', '', string.punctuation))

    #Separamos el texto en palabras
    words = text.split()

     # Creamos un diccionario para guardar las frecuencias
    word_frequency = {}

    # Contamos las apariciones de cada palabra de la lista
    for word in word_list:
        word = word.lower()
        word_frequency[word] = words.count(word)

    # Devolvemos el diccionario
    return word_frequency


word_list = ['python', 'código', 'aprender'] #lista de palabras a buscar en el fichero
result = count_word_frequency(word_list, 'texto.txt')
# Mostramos las palabras ordenadas alfabeticamente
for word in sorted(result):
    print(f"{word}: {result[word]}")
