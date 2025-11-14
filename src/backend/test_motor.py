import motores.retornar_concordancias
import lib.obtener_base 

"""
Este módulo contiene las pruebas unitarias para el sistema de diagnóstico de
enfermedades en fresas. Verifica diferentes escenarios de búsqueda de padecimientos
basados en síntomas proporcionados.

Cada función prueba un escenario diferente:
- busqueda_valida: Un caso típico con síntomas que identifican una enfermedad específica
- busqueda_insuficiente: Caso donde los síntomas son muy pocos para un diagnóstico
- busqueda_multiples: Caso donde los síntomas coinciden con varias enfermedades
- busqueda_inexistente: Caso donde los síntomas no coinciden con ninguna enfermedad
"""

def busqueda_valida():
    """
    Prueba el caso donde se tienen suficientes síntomas específicos para identificar
    una única enfermedad (Picudo de la fresa).
    
    Verifica que:
    1. Se obtiene exactamente un resultado
    2. El resultado corresponde al "Picudo de la fresa"
    """
    # Sintomas de prueba
    sintomas_prueba = [
        {"hecho": "sintoma_boton", "valor": "seco_caido"},
        {"hecho": "sintoma_boton", "valor": "perforado"},
        {"hecho": "sintoma_fruto", "valor": "escasos"}
      ]
    
    # Obtener la base de conocimiento
    base_conocimiento = lib.obtener_base.obtener_base()
    
    
    # Iniciar la busqueda
    resultados = motores.retornar_concordancias.iniciar_busqueda(sintomas_prueba, base_conocimiento)
    print(resultados)

    assert len(resultados) == 1

    nombre = resultados[0].get("nombre", ["No hay nombre en los resultados"])

    assert nombre == "Picudo de la fresa"
    

def busqueda_insuficiente():
    """
    Prueba el caso donde los síntomas proporcionados son insuficientes para 
    realizar un diagnóstico confiable.
    
    En este caso se proporciona un solo síntoma (botón seco y caído), que
    por sí solo puede corresponder a múltiples enfermedades o condiciones.
    
    Verifica que:
    1. No se devuelve ningún resultado cuando los síntomas son muy pocos
       para hacer un diagnóstico confiable
    """
    # Sintomas insuficientes
    sintomas_insuficientes = [
        {"hecho": "sintoma_boton", "valor": "seco_caido"}
      ]
    
    # Obtener la base de conocimiento
    base_conocimiento = lib.obtener_base.obtener_base()
    
    # Iniciar la busqueda
    resultados = motores.retornar_concordancias.iniciar_busqueda(sintomas_insuficientes, base_conocimiento)
    
    assert len(resultados) == 0


def busqueda_multiples():
    """
    Prueba el caso donde los síntomas coinciden con más de una enfermedad.
    
    Este caso usa una combinación de síntomas que son comunes a varias
    enfermedades, específicamente al "Picudo de la fresa" y al
    "Gusano soldado de la remolacha".
    
    Verifica que:
    1. Se obtienen múltiples resultados (len > 1)
    2. Entre los resultados está el "Picudo de la fresa"
    3. Entre los resultados está el "Gusano soldado de la remolacha"
    """
    # Sintomas que coinciden con multiples padecimientos
    sintomas_multiples = [
        {"hecho": "sintoma_boton", "valor": "seco_caido"},
        {"hecho": "sintoma_boton", "valor": "perforado"},
        {"hecho": "sintoma_fruto", "valor": "escasos"},
        {"hecho": "sintoma_hoja", "valor": "mordidas_agujeros"},
        {"hecho": "sintoma_fruto", "valor": "danados"},
        {"hecho": "presencia_insecto", "valor": "gusanos_verdes_pequenos"}
      ]
    
    # Obtener la base de conocimiento
    base_conocimiento = lib.obtener_base.obtener_base()
    
    # Iniciar la busqueda
    resultados = motores.retornar_concordancias.iniciar_busqueda(sintomas_multiples, base_conocimiento)
    
    assert len(resultados) > 1

    assert any(p.get("nombre", "") == "Picudo de la fresa" for p in resultados)
    assert any(p.get("nombre", "") == "Gusano soldado de la remolacha" for p in resultados)

def busqueda_inexistente():
    """
    Prueba el caso donde los síntomas no coinciden con ninguna enfermedad conocida.
    
    Este caso usa una combinación de síntomas que, aunque son válidos individualmente,
    no corresponden a ningún patrón conocido de enfermedad en la base de conocimiento.
    Los síntomas incluyen:
    - Falta de ventilación (condición ambiental)
    - Hojas dañadas
    - Planta pequeña
    
    Verifica que:
    1. No se devuelve ningún resultado cuando los síntomas no coinciden
       con ningún patrón conocido de enfermedad
    """
    # Sintomas que no coinciden con ningun padecimiento
    sintomas_inexistentes = [
        {"hecho": "condicion_ambiental", "valor": "falta_ventilacion"},
        {"hecho": "sintoma_hoja", "valor": "danada"},
        {"hecho": "sintoma_planta", "valor": "chiquita"},
      ]
    
    # Obtener la base de conocimiento
    base_conocimiento = lib.obtener_base.obtener_base()
    
    # Iniciar la busqueda
    resultados = motores.retornar_concordancias.iniciar_busqueda(sintomas_inexistentes, base_conocimiento)
    
    assert len(resultados) == 0


if __name__ == "__main__":
    """
    Ejecuta todas las pruebas en secuencia cuando este archivo se ejecuta directamente.
    
    El orden de las pruebas va de casos simples a más complejos:
    1. busqueda_valida: Caso base de diagnóstico exitoso
    2. busqueda_insuficiente: Manejo de datos incompletos
    3. busqueda_multiples: Manejo de diagnósticos múltiples
    4. busqueda_inexistente: Manejo de casos no reconocidos
    
    Si todas las pruebas pasan (ninguna assertion falla), se muestra un mensaje de éxito.
    """
    tests = [
      ("busqueda_valida", busqueda_valida),
      ("busqueda_insuficiente", busqueda_insuficiente),
      ("busqueda_multiples", busqueda_multiples),
      ("busqueda_inexistente", busqueda_inexistente),
    ]

    for nombre, prueba in tests:
      print(f"Ejecutando {nombre}...")
      prueba()
      print(f"{nombre} pasada.\n")

    print("Todas las pruebas pasaron.")