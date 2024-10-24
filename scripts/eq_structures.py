def print_menu():
    """
    Esta funcion nos permite mostrar las opciones de modelos
    """
    print("Cual de los siguientes modelos deseas trabajar?")
    print("1.-Isomerizacion")
    print("2.-Dimerizacion")
    print("3.-Lotka-Volterra")
    print("4.-Modelo SIR")

def define_the_structure_function():
    print_menu()
    ID_reaction = int(input("Escribe el n'umero identificador del sistema que deseas trabajar:"))
    while ID_reaction < 5 & ID_reaction > 0:
            print('El valor proporcionado es erroneo')
            ID_reaction = int(input("Escribe el n'umero identificador del sistema que deseas trabajar:"))
    reaction = reaction_dynamics(ID_reaction)
    print(reaction)
    input()


class reaction_dynamics():
    def __init__(self,id:int):
        self.define_reaction(id)

    def define_reaction(self, id: int):
        reactions = {
            1: 'Isomerizacion',
            2: 'Dimerizacion',
            3: 'Lotka-Volterra',
            4: 'ISR'
        }
        self.id = reactions.get(id, 'Desconocido')

    def show_equation(self):
        if self.id == 1:
            self.equation = ''
        elif self.id == 2:
            self.equation = ''
        elif self.id == 3:
            self.equation = ''
        elif self.id == 4:
            self.equation = ''

    def __str__(self):
        return f'Modelo: {self.id}'
