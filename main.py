from Boa_Constrictor import Boa_Constrictor
from Huron import Huron
from Guarderia import Guarderia  # Importa la clase Guarderia

# Crear una instancia de la clase Boa_Constrictor
boa = Boa_Constrictor("Boa", 5, 30.0, "Brasil", 0.3)
print(boa.hacer_sonido())  # Debería imprimir "¡Tsss!"
boa.comer_ratones()
print(boa.ratones_comidos)  # Debería imprimir 1

# Crear una instancia de la clase Huron
huron = Huron("Hurón", 2, 5.0, "España", 0.2)
print(huron.hacer_sonido())  # Debería imprimir "¡Eek Eek!"

# Crear una instancia de la clase Guarderia
guarderia = Guarderia()

# Probar alimentar a boa1 en la guardería
resultado_boa1 = guarderia.alimentar_boa(guarderia.boa1)
print("Resultado al alimentar Boa1 en la guardería:", resultado_boa1)  # Esperado: "Éxito" o "La boa está llena"

# Alimentar a boa1 en la guardería hasta que esté llena (simulamos esto al repetir la alimentación)
for _ in range(10):
    guarderia.alimentar_boa(guarderia.boa1)

# Intentar alimentar a boa1 nuevamente después de alcanzar el límite
resultado_boa1_llena = guarderia.alimentar_boa(guarderia.boa1)
print("Resultado al intentar alimentar Boa1 después del límite:", resultado_boa1_llena)  # Esperado: "La boa está llena"

# Probar alimentar una boa inexistente
resultado_boa_none = guarderia.alimentar_boa(None)
print("Resultado al alimentar una boa inexistente:", resultado_boa_none)  # Esperado: "Esta Boa no existe!"
