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
    if len(lista_sintomas) < 3:
        return []
    
    resultados = []
    print(lista_sintomas)
    
    # si no, iniciar la busqueda por cada elemento de la base de conocimiento
    for padecimiento in base_conocimiento:
        # encontrar enfermedades que tengan esta enfermedad
        if cantidad_coincidencias(lista_sintomas, padecimiento) >= 3:
            resultados.append(padecimiento)
            
    return resultados

def cantidad_coincidencias(lista_sintomas, padecimiento):
    contador = 0
    
    for sintoma_usuario in lista_sintomas:
        for sintoma_padecimiento in padecimiento.get("condiciones", []):
            if (sintoma_usuario == sintoma_padecimiento):
                contador += 1
                
    return contador

