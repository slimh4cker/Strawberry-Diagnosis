from flask import Flask, render_template, request, jsonify
from lib.obtener_base import obtener_base
import motores.retornar_concordancias as motor
import traceback

app = Flask(__name__)

def agrupar_sintomas(base_conocimiento):
    sintomas_ag = {}
    if not base_conocimiento:
        return sintomas_ag
    for regla in base_conocimiento:
        for cond in regla.get("condiciones", []):
            hecho = cond.get("hecho")
            valor = cond.get("valor")
            if hecho is None or valor is None:
                continue
            # mantenemos la forma completa (ej. "sintoma_hoja") como clave en  la plantilla
            if hecho not in sintomas_ag:
                sintomas_ag[hecho] = set()
            sintomas_ag[hecho].add(valor)
    # convertir a listas ordenadas
    return {k: sorted(list(v)) for k, v in sintomas_ag.items()}

@app.route("/")
def index():
    base = obtener_base()
    sintomas = agrupar_sintomas(base)
    # imprime cantidad de reglas y algunas claves
    print(f"[DEBUG] Base cargada: {len(base)} reglas. Categorías de síntomas: {list(sintomas.keys())[:10]}")
    return render_template("index.html", sintomas=sintomas)

@app.route("/diagnosticar", methods=["POST"])
def diagnosticar():
    try:
        payload = request.get_json(force=True)
        print(f"[DEBUG] /diagnosticar payload raw: {payload}")
        sintomas_recibidos = payload.get("sintomas", [])
        print(f"[DEBUG] Síntomas recibidos (strings): {sintomas_recibidos}")

        # Convertir a lista de dicts {"hecho": "...", "valor": "..."}
        lista_sintomas = []
        for s in sintomas_recibidos:
            if ":" in s:
                hecho, valor = s.split(":", 1)
                lista_sintomas.append({"hecho": hecho, "valor": valor})
            else:
                parts = s.split("_", 1)
                if len(parts) == 2:
                    hecho, valor = parts
                    lista_sintomas.append({"hecho": hecho, "valor": valor})
        print(f"[DEBUG] Síntomas convertidos para motor: {lista_sintomas}")

        base = obtener_base()
        # tamaño base y ejemplo
        print(f"[DEBUG] Base de conocimiento cargada. Reglas: {len(base)}")

        # Llamada al motor 
        resultados = motor.iniciar_busqueda(lista_sintomas, base)
        print(f"[DEBUG] Resultados crudos del motor (len={len(resultados)}):")
        for r in resultados:
            print("  -", r.get("id"), r.get("nombre"))

        # nombre + condiciones que coincidieron y los sintomas
        respuesta_detallada = []
        for padecimiento in resultados:
            condiciones_padecimiento = padecimiento.get("condiciones", [])
            coincidencias = []
            for cond in condiciones_padecimiento:
                for s in lista_sintomas:
                    if s.get("hecho") == cond.get("hecho") and s.get("valor") == cond.get("valor"):
                        coincidencias.append(cond)
            respuesta_detallada.append({
                "id": padecimiento.get("id"),
                "nombre": padecimiento.get("nombre"),
                "coincidencias": coincidencias,
                "conclusion": padecimiento.get("conclusion", {})
            })

        if not respuesta_detallada:
            mensaje = "No es posible diagnosticar con los síntomas proporcionados."
        else:
            mensaje = f"Se encontraron {len(respuesta_detallada)} coincidencia(s)."

        return jsonify({
            "ok": True,
            "mensaje": mensaje,
            "resultados": respuesta_detallada
        })
    except Exception as e:
        traceback.print_exc()
        return jsonify({"ok": False, "error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
