
from pathlib import Path
import json
from typing import Any, List


def obtener_base() -> List[Any]:
	"""Lee `src/base_conocimiento.json` y devuelve su contenido como lista.

	Comportamiento:
	- Si el JSON es una lista, se devuelve tal cual.
	- Si el JSON es un dict con una sola clave cuyo valor es una lista, se devuelve esa lista.
	- Si el JSON es un dict con múltiples valores que son listas, se concatenan y se devuelven.
	- En cualquier otro caso se devuelve una lista con el objeto JSON como único elemento.

	En caso de error (archivo no encontrado o JSON inválido) se devuelve lista vacía.
	"""
	# base_conocimiento.json se encuentra en el directorio padre de este archivo (src/)
	base_path = Path(__file__).resolve().parents[1] / "base_conocimiento.json"

	try:
		text = base_path.read_text(encoding="utf-8")
		data = json.loads(text)
	except FileNotFoundError:
		# Archivo no encontrado
		return []
	except json.JSONDecodeError:
		# JSON inválido
		return []

	# Si ya es una lista, devolverla
	if isinstance(data, list):
		return data

	# Si es un dict, tratar de convertirlo en lista de forma razonable
	if isinstance(data, dict):
		# Caso común: dict con una sola clave cuyo valor es una lista
		if len(data) == 1:
			only = next(iter(data.values()))
			if isinstance(only, list):
				return only

		# Si hay varias claves y alguna contiene listas, concatenarlas
		list_values = [v for v in data.values() if isinstance(v, list)]
		if list_values:
			result: List[Any] = []
			for l in list_values:
				result.extend(l)
			if result:
				return result

		# En último caso, devolver el dict como único elemento de una lista
		return [data]

	# Para otros tipos (números, strings, etc.) devolverlos envueltos en lista
	return [data]


if __name__ == "__main__":
	# Pequeña prueba manual cuando se ejecuta el módulo directamente
	lista = obtener_base()
	print("Leidos", len(lista), "elementos desde base_conocimiento.json")
	print(lista)

