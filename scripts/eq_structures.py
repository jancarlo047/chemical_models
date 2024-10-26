def print_menu() -> None:
    """
    Esta funcion nos permite mostrar las opciones de modelos
    """
    print("Cual de los siguientes modelos deseas trabajar?")
    print("1.-Isomerizacion")
    print("2.-Dimerizacion")
    print("3.-Muerte-Nacimiento")
    print("4.-Modelo SIR")

def obtain_id() -> int:

    while True:
        ID_reaction = input("Escribe el número identificador del sistema que deseas trabajar: ")
        try:
            ID_reaction = int(ID_reaction)
            print(f"El número identificador es: {ID_reaction}")
            break  # Salir del bucle si la conversión es exitosa
        except ValueError:
            print("Error: Por favor, ingresa un número entero válido.")
    
    while ID_reaction < 5 & ID_reaction > 0:
            print('El valor proporcionado es erroneo')
            ID_reaction = int(input("Escribe el n'umero identificador del sistema que deseas trabajar:"))
    
    return ID_reaction

def define_the_structure_function():
    
    print_menu()
    
    ID_reaction = obtain_id()

    reaction = reaction_dynamics(ID_reaction)

    print(reaction)

class reaction_dynamics():
    def __init__(self,id:int):
        self.define_reaction(id)

    def define_reaction(self, id: int):
        reactions = {
            1: 'Isomerizacion',
            2: 'Dimerizacion',
            3: 'Lotka-Volterra',
            4: 'SIR'
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
