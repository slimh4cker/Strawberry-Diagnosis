from gui.app import create_integrated_app

'''
Prueba de multiples enfermedades:

sintomas = [
    {"hecho": "sintoma_hoja", "valor": "marchita"},
    {"hecho": "sintoma_fruto", "valor": "podrido"}, 
    {"hecho": "sintoma_raiz", "valor": "podrida"},
    {"hecho": "sintoma_planta", "valor": "muerte"}
]


'''

if __name__ == "__main__":
    app = create_integrated_app()
    app.run()