
# Importamos las bibliotecas necesarias
from pathlib import Path  # Para manejo de rutas de archivos de forma portable
import json              # Para leer y parsear archivos JSON
from typing import Any, List  # Para anotaciones de tipo en Python


def obtener_base() -> List[Any]:
    """Lee el archivo de base de conocimiento y lo convierte en una lista de Python.
    
    El archivo `src/base_conocimiento.json` contiene la base de conocimiento del sistema
    experto para diagnóstico de enfermedades en fresas. Esta función se encarga de leer
    ese archivo y convertir su contenido en una estructura de datos de Python (lista).

    Comportamiento según el tipo de contenido en el JSON:
    - Si el JSON contiene una lista: se devuelve directamente
    - Si es un diccionario con una sola clave que contiene una lista: se extrae esa lista
    - Si es un diccionario con varias listas: se concatenan todas las listas encontradas
    - Para cualquier otro caso: se envuelve el contenido en una lista de un elemento

    Returns:
        List[Any]: Lista con el contenido de la base de conocimiento
                  Lista vacía en caso de error (archivo no encontrado o JSON inválido)
    """
	# base_conocimiento.json se encuentra en el directorio padre de este archivo (src/)
    # Construimos la ruta al archivo base_conocimiento.json
    # __file__ es la ruta al archivo actual (obtener_base.py)
    # parents[1] nos da el directorio padre del padre (src/)
    base_path = Path(__file__).resolve().parents[1] / "base_conocimiento.json"

    try:
        # Intentamos leer el archivo como texto UTF-8
        text = base_path.read_text(encoding="utf-8")
        # Convertimos el texto JSON en un objeto Python
        data = json.loads(text)
    except FileNotFoundError:
        # Si el archivo no existe, retornamos lista vacía
        return []
    except json.JSONDecodeError:
        # Si el JSON es inválido, retornamos lista vacía
        return []

    # Primer caso: si el JSON ya es una lista, la retornamos directamente
    if isinstance(data, list):
        return data

	# Si es un dict, tratar de convertirlo en lista de forma razonable
    # Segundo caso: si es un diccionario, intentamos extraer listas de él
    if isinstance(data, dict):
        # Caso más común: diccionario con una sola clave que contiene una lista
        # Por ejemplo: {"reglas": [...]} -> extraemos solo la lista
        if len(data) == 1:
            only = next(iter(data.values()))  # Obtenemos el único valor
            if isinstance(only, list):
                return only

        # Si el diccionario tiene varias claves, buscamos todas las que contengan listas
        # Por ejemplo: {"reglas": [...], "hechos": [...]} -> concatenamos las listas
        list_values = [v for v in data.values() if isinstance(v, list)]
        if list_values:
            result: List[Any] = []
            for l in list_values:
                result.extend(l)  # Concatenamos todas las listas encontradas
            if result:
                return result

        # Si no encontramos listas útiles, devolvemos el diccionario como un elemento
        return [data]

    # Tercer caso: para cualquier otro tipo de dato (str, int, float, etc.)
    # lo envolvemos en una lista para mantener la consistencia del retorno
    return [data]


if __name__ == "__main__":
    # Hacemos una pequeña prueba manual de la función
    lista = obtener_base()
    # Mostramos cuántos elementos se leyeron
    print("Leidos", len(lista), "elementos desde base_conocimiento.json")
    # Y mostramos el contenido para verificación
    print(lista)

