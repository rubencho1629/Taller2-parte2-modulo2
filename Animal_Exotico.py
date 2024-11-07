from Animal import Animal

class Animal_Exotico(Animal):
    def __init__(self, nombre: str, edad: int, peso: float, pais_origen: str, impuestos: float) -> None:
        super().__init__(nombre, edad, peso)
        self.pais_origen = pais_origen
        self.impuestos = impuestos

    def calcular_flete(self) -> float:
        return self.peso * self.impuestos