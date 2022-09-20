def anagrama(strg1, strg2):
    return sorted(strg1)==sorted(strg2)
    # retornará una nueva lista ordenada de cada cadena
    # Confirmando si la primera y segunda cadena contienen los mismos caracteres

print(anagrama("roma","amor"))
print(anagrama("hola","adios"))


