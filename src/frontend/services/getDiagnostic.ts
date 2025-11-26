

export interface Diagnostic{
    hecho: string,
    valor: string
};

function post_diagnostic(data: Array<Diagnostic> ): void{
    const url: string ="http://127.0.0.1:8000/api/diagnostico";
    console.log(data);
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            data
        })
            
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });

}

// Ejemplo de como se manda a llamar
const diagnostic: Array<Diagnostic> = [
        {"hecho": "sintoma_boton", "valor": "seco_caido"},
        {"hecho": "sintoma_boton", "valor": "perforado"},
        {"hecho": "sintoma_fruto", "valor": "escasos"},
        {"hecho": "sintoma_hoja", "valor": "mordidas_agujeros"},
        {"hecho": "sintoma_fruto", "valor": "danados"},
        {"hecho": "presencia_insecto", "valor": "gusanos_verdes_pequenos"}
];

post_diagnostic(diagnostic);

