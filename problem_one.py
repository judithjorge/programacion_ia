""" Problema 1. Procesamiento de una lista de enteros. 
Crea una función que reciba una lista de enteros por parámetro y devuelva otra 
lista, de acuerdo a las siguientes acciones: 
    1. Eliminar los números negativos de la lista. 
    2. Eliminar los valores que están repetidos, quedándonos con uno de ellos. 
    3. Ordenar los números resultantes de menor a mayor. 
    Por ejemplo, si le pasara [4, -1, 2, 4, 3, -5, 2], debería retornar [2,3,4].  """

lista = [4, -1, 2, 4, 3, -5, 2]
def procesar_enteros(lista):
    #Eliminar los numeros negativos de la lista (con list comprehension)
    lista = [num for num in lista if num >= 0]
    #Eliminar los valores repetidos(set convierte la lista en un conjuunto, y los conjunto no permiten valores duplicados)
    lista = list(set(lista))
    #Ordenar los números resultantes de menor a mayor (sort() ordena la lista de menor a mayor)
    lista.sort()
    return lista

print(procesar_enteros(lista))