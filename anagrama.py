def anagrama(strg1, strg2):
    return sorted(strg1)==sorted(strg2)
    # retornará una nueva lista ordenada de cada cadena
    # Confirmando si la primera y segunda cadena contienen los mismos caracteres

print(anagrama("roma", "amor"))  # True
print(anagrama("hola", "adios"))  # False


# Código corregido

def anagrama_2(strg1, strg2):
    strg1 = strg1.lower()
    strg2 = strg2.lower()
    return sorted(strg1) == sorted(strg2)

print(anagrama_2("saco", "cosa"))  # True
print(anagrama_2("mora", "ramo"))  # True
print(anagrama_2("casa", "saca"))  # True
print(anagrama_2("Cazar", "raza"))  # False

# Código corregido para analizar una frase y encontrar los anagramas 

from collections import Counter

def es_anagrama(palabra1, palabra2):
    # Convierte las palabras en contadores de caracteres
    contador1 = Counter(palabra1.lower())
    contador2 = Counter(palabra2.lower())

    # Compara los contadores para determinar si son anagramas
    if contador1 == contador2:
        return True
    else:
        return False

def encontrar_anagramas(frase):
    palabras = frase.split()
    anagramas = []

    # Compara cada par de palabras en la frase para encontrar anagramas
    for i in range(len(palabras)):
        for j in range(i + 1, len(palabras)):
            if es_anagrama(palabras[i], palabras[j]):
                anagramas.append((palabras[i], palabras[j]))

    return anagramas

# Ejemplo de uso
frase = "Una persona se desea casar en roma sin importar su dinero, solo busca un gran amor y propone a sacar el anillo de matrimonio"
resultado = encontrar_anagramas(frase)
print("Anagramas encontrados:")
for par in resultado:
    print(f"{par[0]} - {par[1]}")


