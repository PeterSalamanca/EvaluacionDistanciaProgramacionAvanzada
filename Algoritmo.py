class persona(): # Clase Padre

    # constructor de la clase padre con los atributos o parametros a ingresar
    def __init__(self, apePaterno, apeMaterno, nomb):
        self.apellidoPaterno = apePaterno
        self.apellidoMaterno = apePaterno
        self.nombres = nomb
    # metodo para mostrar el nombre completo
    def mostrarNombreCompleto(self):
        txt = "{0} {1}, {2}"
        return txt.format(self.apellidoPaterno, self.apellidoMaterno, self.nombres)

class Estudiante(persona): # Clase Hija

    # Metodo para heredar el constructor de la clase Padre
    def __init__(self, apePaterno, apeMaterno, nomb, var4):
        super().__init__(apePaterno, apeMaterno, nomb)
        self.profesion = var4

# Se registra los datos personales como ejemplo
est1 = Estudiante("Salamanca","Alfonso","Peter Alberto","Ingeniería en Informática")
# Se muestra en pantalla el nombre completo y la profesión
print(est1.mostrarNombreCompleto())
print(est1.profesion)