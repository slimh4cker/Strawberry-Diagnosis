def contar_coincidencias(sintomas, condiciones, s_idx=0, c_idx=0, count=0):
    """Cuenta coincidencias recursivamente entre síntomas y condiciones."""
    # Caso base: ya recorrimos todos los síntomas
    if s_idx >= len(sintomas):
        return count
    
    # Si terminamos las condiciones del síntoma actual, pasamos al siguiente síntoma
    if c_idx >= len(condiciones):
        return contar_coincidencias(sintomas, condiciones, s_idx + 1, 0, count)
    
    # Obtenemos el síntoma y condición actual para comparar
    s = sintomas[s_idx]
    c = condiciones[c_idx]
    
    # Verificamos coincidencia en ambos campos
    if s.get("hecho") == c.get("hecho") and s.get("valor") == c.get("valor"):
        count += 1
    
    # Llamada recursiva para siguiente condición
    return contar_coincidencias(sintomas, condiciones, s_idx, c_idx + 1, count)


def consultar_enfermedad(lista_sintomas, padecimiento):
    """Determina si un padecimiento coincide con los síntomas."""
    condiciones = padecimiento.get("condiciones", [])
    # Requiere al menos 2 coincidencias
    return contar_coincidencias(lista_sintomas, condiciones) >= 2


def filtrar_padecimientos(sintomas, base, idx=0, resultados=None):
    """Filtra recursivamente los padecimientos que coinciden con los síntomas."""
    if resultados is None:
        resultados = []
    
    # Caso base: recorrimos toda la base de conocimiento
    if idx >= len(base):
        return resultados
    
    # Si hay coincidencia, agregamos a resultados
    if consultar_enfermedad(sintomas, base[idx]):
        resultados.append(base[idx])
    
    # Llamada recursiva para siguiente padecimiento
    return filtrar_padecimientos(sintomas, base, idx + 1, resultados)


def iniciar_busqueda(lista_sintomas, base_conocimiento):
    """Inicia la búsqueda recursiva de padecimientos."""
    # Validación mínima de síntomas requeridos
    return [] if len(lista_sintomas) < 2 else filtrar_padecimientos(lista_sintomas, base_conocimiento)