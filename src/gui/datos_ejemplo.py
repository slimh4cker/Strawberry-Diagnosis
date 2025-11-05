EJEMPLOS_DETALLADOS = {
    "sintoma_boton": {
        "valores": ["seco_caido", "perforado"],
        "descripcion": "Síntomas en botones florales"
    },
    "sintoma_fruto": {
        "valores": ["manchas_cafe", "zonas_acuosas", "podrido", "lesiones", "opacos", "mordidas", "deformes", "agarre_flojo", "manchas_circulares_marron", "centros_necroticos_rosada", "pudricion", "lesiones_blandas", "goteo_liquido_rojo", "cubierta_blanca_negra", "manchas_blandas", "moho_negro", "descomposicion_rapida_tejido", "perdida_total_firmeza", "masas_largas_micelio", "perdida_agua", "escasos", "danados", "mordidos", "pequenos_deformes", "pudricion_negro", "morado_oscuro", "moho_blanco_humedo"],
        "descripcion": "Síntomas en los frutos"
    },
    "sintoma_hoja": {
        "valores": ["danada", "cubierta_gris", "marchita", "manchas_purpura", "amarillentas", "secas", "enrolladas_torcidas", "centros_grisaceos_blanquecinos", "bordes_oscuros_definidos", "manchas_negras", "lesiones_negras", "halo_amarillo", "arrugadas", "pegajosas", "telaranas_muy_pequenas", "enrollamiento_limites", "manchas_blancas_micelio", "puntos_negros", "manchas_marron", "manchas_circulares_purpura", "centro_blanco"],
        "descripcion": "Síntomas en las hojas"
    },
    "sintoma_tallo": {
        "valores": ["marchito"],
        "descripcion": "Síntomas en los tallos"
    },
    "presencia_insecto": {
        "valores": ["gusanos_verdes_pequenos", "moscas_blancas_pequenas_alrededor", "gusanos_gordos_tierra", "larvas_movimiento_u", "chinches_verde_rojo_naranja", "oruga_pelos_verde_marron_negro", "pequenos_insectos_tallo", "polilla_color_cafe", "gusanos_cabeza_dura_cafe", "tijerillas_dentro_fruto", "ciempes_en_cerca_planta", "larvas_verdes_amarillas_cabeza_marron_fruta", "insecto_debajo_plantas_dia"],
        "descripcion": "Insectos o plagas visibles"
    },
    "sintoma_raiz": {
        "valores": ["podrida_negra", "podrida", "estela_central_roja", "blanca", "dano", "corteza_desprendible"],
        "descripcion": "Síntomas en las raíces"
    },
    "sintoma_planta": {
        "valores": ["chiquita", "marchitez_general", "muerte", "debilitada", "cortadas_ras_suelo", "crecimiento_lento", "baja_normal", "hormigas_alrededor", "debil_seca", "marchitamiento"],
        "descripcion": "Síntomas generales de la planta"
    },
    "condicion_ambiental": {
        "valores": ["falta_ventilacion", "falta_luz", "alta_humedad"],
        "descripcion": "Condiciones ambientales"
    },
    "sintoma_corona": {
        "valores": ["manchas_oscuras", "podrida", "descolorida", "lesiones"],
        "descripcion": "Síntomas en la corona"
    },
    "sintoma_general": {
        "valores": ["olor_feo", "baba_brillante", "manchas_pardas", "olor_agrio", "olor_fermentacion_moho"],
        "descripcion": "Síntomas generales"
    },
    "sintoma_hoja_vieja": {
        "valores": ["marchita", "color_amarillo_rojizo"],
        "descripcion": "Síntomas en hojas viejas"
    },
    "sintoma_hoja_nueva": {
        "valores": ["mordidas", "deformadas_arrugadas"],
        "descripcion": "Síntomas en hojas nuevas"
    },
    "sintoma_raiz_joven": {
        "valores": ["podrida"],
        "descripcion": "Síntomas en raíces jóvenes"
    },
    "sintoma_raiz_principal": {
        "valores": ["estela_central_roja"],
        "descripcion": "Síntomas en raíz principal"
    },
    "sintoma_fruto_joven": {
        "valores": ["rayas_plateadas"],
        "descripcion": "Síntomas en frutos jóvenes"
    },
    "sintoma_fruto_maduro": {
        "valores": ["deformados_piel_fea"],
        "descripcion": "Síntomas en frutos maduros"
    },
    "sintoma_fruto_cerca_suelo": {
        "valores": ["mordidas_redondas_pequenas"],
        "descripcion": "Síntomas en frutos cerca del suelo"
    },
    "sintoma_planta_joven": {
        "valores": ["muerte"],
        "descripcion": "Síntomas en plantas jóvenes"
    },
    "sintoma_petalo_pedunculo": {
        "valores": ["color_cafe"],
        "descripcion": "Síntomas en pétalos y pedúnculos"
    },
    "sintoma_peciolo": {
        "valores": ["lesiones_oscuras", "marchito"],
        "descripcion": "Síntomas en peciolos"
    },
    "sintoma_base_hoja": {
        "valores": ["lesiones"],
        "descripcion": "Síntomas en la base de las hojas"
    },
    "sintoma_estolon": {
        "valores": ["muerto"],
        "descripcion": "Síntomas en estolones"
    },
    "sintoma_lesion": {
        "valores": ["pequenas"],
        "descripcion": "Características de lesiones"
    },
    "sintoma_caliz": {
        "valores": ["marron"],
        "descripcion": "Síntomas en el cáliz"
    },
    "sintoma_fresa": {
        "valores": ["malformada"],
        "descripcion": "Síntomas en la fresa completa"
    },
    "sintoma_interno": {
        "valores": ["decoloracion_interna"],
        "descripcion": "Síntomas internos"
    },
    "sintoma_flor": {
        "valores": ["danos_base"],
        "descripcion": "Síntomas en las flores"
    },
    "sintoma_superficie": {
        "valores": ["blanco"],
        "descripcion": "Síntomas en la superficie"
    },
    "sintoma_pudricion": {
        "valores": ["empapada"],
        "descripcion": "Características de pudrición"
    }
}

CATEGORIAS = list(EJEMPLOS_DETALLADOS.keys())

def obtener_valores_por_categoria(categoria):
    """Retorna los valores disponibles para una categoría específica"""
    return EJEMPLOS_DETALLADOS.get(categoria, {}).get("valores", [])