class Person():
    def __init__(self, _name, _date, _dni):  ## self --> puntero que apunta a la clase creada
        print("se crea el objeto")
        self.name = _name
        self.birthdate = _date
        self.dni = _dni
        self.address = ""

    def setDNI(self, _dni):
        self.dni = _dni

    def getDNI(self):
        return self.dni

    def __del__(self):
        print("se destruye el objeto al final de la ejecución del programa.")


class URJCstudent(Person):
    def __init__(self, _name, _date_, _dni, _tuition):
        super().__init__(_name, _date_, _dni)
        self.tuition = _tuition

    def __del__(self):
        super().__del__()
        print("Sobrecarga del hijo")


person1 = Person("Carlos", "17/01/2001", "11897218P")
print(f"El DNI de la persona es {person1.getDNI()}")
person1.setDNI("11897218N")
print(f"El DNI de la persona modificado es {person1.getDNI()}")
print("--------------------ALUMNO--------------------")
student1 = URJCstudent("Carlos", "17/01/2001", "11897218P", "88897J")

## EN PYTHON TODO ES UN OBJETO --> NO RECOMENDABLE IMPLEMENTAR METODOS CON LA CLASE GENERAL DE PYTHON



