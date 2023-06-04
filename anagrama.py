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


