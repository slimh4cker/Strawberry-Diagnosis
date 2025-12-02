#COMANDO PARA LEVANTAR FAST API. NECESARIO EJECUTAR PARA QUE FUNCIONE EL PRPYECTO
# uvicorn api_fast:app --reload

# Este archivo es el que levanta FastApi (logica del BackEnd)

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict, Any
from fastapi.middleware.cors import CORSMiddleware
import logging # Registro de logs en terminal
from collections import Counter # Para contar sintomas repetidos

logger = logging.getLogger("uvicorn.error")
logger.setLevel(logging.DEBUG)

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
    counter = Counter((s['hecho'], s['valor']) for s in lista_sintomas) # se cuenta cada clave, valor
    if any(count > 1 for count in counter.values()): # si alguna clave, valor se repite
        return {"resultado": "Hay síntomas repetidos en la selección."}
    
    if len(lista_sintomas) < 2:
        return {"error": "⚠️ Selecciona mas sintomas."}

    base = obtener_base()
    resultados = motor.iniciar_busqueda(lista_sintomas, base)

    if resultados:
        # Para devolver todos los resultados como lista
        # limpiamos o formateamos cada resultado si quieres,
        # o solo devuelve tal cual vienen del motor
        response = []
        for r in resultados:
            item = {
                "id": r.get("id", ""),
                "nombre": r.get("nombre", ""),
                "conclusion": r.get("conclusion", {}),
                "condiciones": r.get("condiciones", [])
            }
            response.append(item)

        return response

    return {"error": "No se puede diagnosticar con los datos actuales. Posiblemente los sintomas indicados no sean sufucientes"}

