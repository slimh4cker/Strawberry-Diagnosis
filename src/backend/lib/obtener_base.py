
# Importamos las bibliotecas necesarias
from pathlib import Path  # Para manejo de rutas de archivos de forma portable
import json              # Para leer y parsear archivos JSON
from typing import Any, List, Dict  # Para anotaciones de tipo en Python


def flatten_dict_lists(data: Dict[Any, Any]) -> List[Any]:
    """Función recursiva para extraer listas de un diccionario anidado."""
    result = []
    for value in data.values():
        if isinstance(value, list):
            result.extend(value)
        elif isinstance(value, dict):
            # Llamada recursiva para diccionarios anidados
            result.extend(flatten_dict_lists(value))
    return result


def obtener_base() -> List[Any]:
    """Lee el archivo de base de conocimiento y lo convierte en una lista de Python."""
    base_path = Path(__file__).resolve().parents[1] / "data/base_conocimiento.json"
    print(base_path)

    try:
        text = base_path.read_text(encoding="utf-8")
        data = json.loads(text)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

    if isinstance(data, list):
        return data

    if isinstance(data, dict):
        if len(data) == 1:
            only = next(iter(data.values()))
            if isinstance(only, list):
                return only

        # Usamos la función recursiva externa
        list_values = flatten_dict_lists(data)
        if list_values:
            return list_values

        return [data]

    return [data]


if __name__ == "__main__":
    # Hacemos una pequeña prueba manual de la función
    lista = obtener_base()
    # Mostramos cuántos elementos se leyeron
    print("Leidos", len(lista), "elementos desde base_conocimiento.json")
    # Y mostramos el contenido para verificación
    print(lista)

