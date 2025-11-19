from flask import Flask, render_template, request, jsonify
from lib.obtener_base import obtener_base
import motores.retornar_concordancias as motor
import traceback
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "frontend", "templates"),
    static_folder=os.path.join(BASE_DIR, "frontend", "static")
)

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
           #("sintoma_hoja") como clave en  la plantilla
            if hecho not in sintomas_ag:
                sintomas_ag[hecho] = set()
            sintomas_ag[hecho].add(valor)
    # convertir a listas ordenadas
    return {k: sorted(list(v)) for k, v in sintomas_ag.items()}

@app.route("/")
def index():
    base = obtener_base()
    sintomas = agrupar_sintomas(base)
    print(f"[DEBUG] Base cargada: {len(base)} reglas. Categorías de síntomas: {list(sintomas.keys())[:10]}")
    return render_template("index.html", sintomas=sintomas)

@app.route("/diagnosticar", methods=["POST"])
def diagnosticar():
    try:
        payload = request.get_json(force=True)
        sintomas_recibidos = payload.get("sintomas", [])

        if not sintomas_recibidos:
            return jsonify({"resultado": "⚠️ No seleccionaste síntomas."})

        # Convertir a lista de diccionarios {"hecho": "...", "valor": "..."}
        lista_sintomas = []
        for s in sintomas_recibidos:
            if ":" in s:
                hecho, valor = s.split(":", 1)
                lista_sintomas.append({"hecho": hecho, "valor": valor})

        base = obtener_base()
        resultados = motor.iniciar_busqueda(lista_sintomas, base)

        # Si el motor devuelve coincidencias
        if resultados:
            mejor = resultados[0]  
            diagnostico = mejor.get("conclusion", {}).get("diagnostico", mejor.get("nombre", "Desconocido"))

            descripcion = mejor.get("descripcion", "")
            condiciones = [f"{c['hecho'].replace('sintoma_', '').capitalize()}: {c['valor'].replace('_', ' ')}"
                           for c in mejor.get("condiciones", [])]

            texto_condiciones = "<br>".join(f"• {c}" for c in condiciones)

            resultado_html = f"""
                <h4 class='text-success'>🩺 {diagnostico}</h4>
                {'<p class="text-muted">' + descripcion + '</p>' if descripcion else ''}
                <div class='text-start mx-auto mt-2' style='max-width:600px'>
                    <p class='fw-semibold'>Síntomas característicos:</p>
                    <p>{texto_condiciones}</p>
                </div>
            """

            return jsonify({"resultado": resultado_html})

        # Si no hubo coincidencias
        return jsonify({"resultado": "No se puede diagnosticar en este momento."})

    except Exception as e:
        traceback.print_exc()
        return jsonify({"resultado": f"Error interno: {str(e)}"})


if __name__ == "__main__":
    app.run(debug=True)