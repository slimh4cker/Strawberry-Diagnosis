## Este codigo resuelve la pregunta "Tengo una lista de sintomas, cuales padecimientos tiene mi arbusto de fresas?"
# esta funcion es recursivay no utiliza variables globales

# pasos
# 1. Recibir la lista de sintomas


# Funcion con la que realizar la busqueda
# lista_sintomas: lista de sintomas proporcionada por el usuario 
#       Formato: {[
#        {"hecho": "sintoma_hoja_vieja", "valor": "marchita"},
#        {"hecho": "sintoma_raiz", "valor": "blanca"},
#        {"hecho": "sintoma_raiz", "valor": "podrida"},
#        {"hecho": "sintoma_corona", "valor": "descolorida"},
#        {"hecho": "sintoma_planta", "valor": "muerte"}
#      ]}

# base_conocimiento: lista de padecimientos obtenida de la base de conocimiento, desde el metodo obtener_base()

def iniciar_busqueda(lista_sintomas, base_conocimiento):
    # filtrado en caso de que sean menos de 3 sintomas
    if len(lista_sintomas) < 2:
        return []
    
    resultados = []
    
    # si no, iniciar la busqueda por cada elemento de la base de conocimiento
    for padecimiento in base_conocimiento:
        # consultar cada regla
        if consultar_enfermedad(lista_sintomas, padecimiento):
            resultados.append(padecimiento)
            
    return resultados

# Funcion para consultar si un padecimiento coincide con los sintomas del usuario
# Devuelve True si el padecimiento coincide con al menos 3 sintomas del usuario
# Devuelve False en caso contrario
def consultar_enfermedad(lista_sintomas, padecimiento):
    contador = 0
    
    for sintoma_usuario in lista_sintomas:
        for sintoma_padecimiento in padecimiento.get("condiciones", []):
            # Comparar explícitamente cada campo
            if (sintoma_usuario.get("hecho") == sintoma_padecimiento.get("hecho") and
                sintoma_usuario.get("valor") == sintoma_padecimiento.get("valor")):
                contador += 1
                
    return contador >= 2

