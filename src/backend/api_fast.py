#Este archivo es el que levanta FastApi (logica del BackEnd)

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict, Any
from fastapi.middleware.cors import CORSMiddleware

# Importamos tus funciones del proyecto
from lib.obtener_base import obtener_base
import motores.retornar_concordancias as motor

# ------------------- CONFIG FASTAPI -------------------
app = FastAPI()

# Permitir llamadas desde flask (localhost)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # Puedes restringir después
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------- MODELO DE ENTRADA -------------------
class Symptom(BaseModel):
    hecho: str
    valor: str

class Payload(BaseModel):
    data: List[Symptom]


# ------------------- ENDPOINT PRINCIPAL -------------------
@app.post("/api/diagnostico")
def diagnostico(payload: Payload):

    lista_sintomas = [s.model_dump() for s in payload.data]

    if len(lista_sintomas) < 2:
        return {"resultado": "⚠️ Selecciona mas síntomas."}

    base = obtener_base()
    resultados = motor.iniciar_busqueda(lista_sintomas, base)

    if resultados:
        mejor = resultados[0]

        diagnostico = (
            mejor.get("conclusion", {}).get("diagnostico")
            or mejor.get("nombre")
            or "Desconocido"
        )

        descripcion = mejor.get("descripcion", "")
        condiciones = [
            f"{c['hecho'].replace('sintoma_', '').capitalize()}: "
            f"{c['valor'].replace('_', ' ')}"
            for c in mejor.get("condiciones", [])
        ]

        condiciones_html = "<br>".join(f"• {c}" for c in condiciones)

        html = f"""
            <h4 class='text-success'>🩺 {diagnostico}</h4>
            {'<p class="text-muted">' + descripcion + '</p>' if descripcion else ''}
            <div class='text-start mx-auto mt-2' style='max-width:600px'>
                <p class='fw-semibold'>Sintomas característicos:</p>
                <p>{condiciones_html}</p>
            </div>
        """

        return {"resultado": html}

    return {"resultado": "No se puede diagnosticar con los datos actuales."}
