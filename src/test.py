import motores.retornar_concordancias
import lib.obtener_base 

def busqueda_valida():
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

    assert len(resultados) == 1

    nombre = resultados[0].get("nombre", ["No hay nombre en los resultados"])

    assert nombre == "Picudo de la fresa"
    


def busqueda_insuficiente():
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

if __name__ == "__main__":
    busqueda_valida()
    busqueda_insuficiente()
    busqueda_multiples()
    print("Todas las pruebas pasaron.")