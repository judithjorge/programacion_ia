"""Escribe una función que reciba dos listas de enteros y devuelva un diccionario 
con la siguiente información (ES OBLIGATORIO USAR CONJUNTOS PARA CALCULARLOS) 
    1. La intersección de ambos conjuntos (elementos comunes). 
    2. La unión de ambos conjuntos (todos los elementos sin duplicados). 
    3. La diferencia simétrica (elementos que están en uno u otro conjunto, 
    pero no en ambos). 
"""

def set_operations(list1, list2):
    conjunto1 = set(list1)
    conjunto2= set(list2)
    
    #Intereseccion de ambos conjuntos
    interseccion = conjunto1 & conjunto2   

    #Union de ambos conjuntos
    union = conjunto1 | conjunto2    

    #Diferencia simetrica
    diferencia_simetrica = conjunto1 ^ conjunto2

    resultado = {
        "Interseccion" : interseccion, 
        "Union" : union,
        "Diferencia simetrica": diferencia_simetrica
    }

    return resultado

lista1 = [1,2,3,4]
lista2= [3,4,5,6]

resultado = set_operations(lista1, lista2)
print(resultado)
   

    