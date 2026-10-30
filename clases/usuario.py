class Usuario():
    def __init__(self,nombre,edad,correo,contrasena):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        self.contrasena = contrasena


    def datos_completos(self):
        if self.nombre!="" and self.edad!=0 and self.correo!="" and self.contrasena!="":
            return True
        else:
            return False

    def correo_valido(self):
        if self.correo[len(self.correo)-13: len(self.correo)] == "@pioix.edu.ar":
            return True
        else:
            return False

    def nombre_valido(self):
            for caracter in self.nombre:
                if caracter == 1 or caracter == 2 or caracter == 3 or caracter == 4 or caracter == 5 or caracter == 6 or caracter == 7 or caracter == 8 or caracter == 9 or caracter == 0:
                    return False
                else:
                    return True

