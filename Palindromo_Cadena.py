Cadena = "dabale arroz a la zorra el abad"
Cadena_lower = Cadena.casefold()
# Se indica que no tome ni mayusculas ni minusculas para el proceso
Cadena_split = Cadena_lower.split(' ')
# Se separa en partes la frase, reemplazando el espacio
Cadena_join = ''.join(Cadena_split)
# Se une cada una de las palabras de la cadena sin espacios

Cadena_Inversa = Cadena_join[::-1]
# Se confirma si la Cadena sin espacios es igual a la cadena normal

# print(Cadena_Inversa)

if (Cadena_join == Cadena_Inversa):
  print("Si, la cadena '{}' es un palindromo".format(Cadena))
else:
  print("No, la cadena '{}' no es un palindromo".format(Cadena))