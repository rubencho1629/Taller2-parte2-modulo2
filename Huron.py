from Animal_Exotico import Animal_Exotico

class Huron(Animal_Exotico):
    def __init__(self, nombre: str, edad: int, peso: float, pais_origen: str, impuestos: float) -> None:
        super().__init__(nombre, edad, peso, pais_origen, impuestos)

    def hacer_sonido(self) -> str:
        return "¡Eek Eek!"