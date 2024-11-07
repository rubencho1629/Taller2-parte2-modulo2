from Boa_Constrictor import Boa_Constrictor
from Huron import Huron

class Guarderia:
    def __init__(self):
        # Instancias de 2 Boas y 2 Hurones
        self.boa1 = Boa_Constrictor("Boa1", 3, 25.0, "Brasil", 0.3)
        self.boa2 = Boa_Constrictor("Boa2", 4, 28.0, "Colombia", 0.35)
        self.huron1 = Huron("Huron1", 2, 5.0, "España", 0.2)
        self.huron2 = Huron("Huron2", 1, 4.5, "Portugal", 0.25)

    def alimentar_boa(self, boa: Boa_Constrictor) -> str:
        # Verifica si la instancia de boa es None
        if boa is None:
            return "Esta Boa no existe!"

        try:
            # Intentamos alimentar a la boa
            boa.comer_ratones()
            return "Éxito"
        except ValueError as e:
            # Si la boa ha alcanzado el límite de ratones, captura el error
            if str(e) == "Demasiados Ratones!":
                return "La boa está llena"
            else:
                raise e  # Re-lanzar cualquier otro error inesperado

# Ejemplo de uso:
guarderia = Guarderia()
print(guarderia.alimentar_boa(guarderia.boa1))  # Esperado: "Éxito" o "La boa está llena"
print(guarderia.alimentar_boa(None))  # Esperado: "Esta Boa no existe!"
