// 1. Agregamos 'async' a la función para poder usar 'await' dentro
async function post_diagnostic(data) {
    const url = "http://127.0.0.1:8000/api/diagnostico";
    
    try {
        // 2. Usamos 'await' para esperar la respuesta
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ data }) 
        });

        // 3. Esperamos a que se convierta a JSON
        const responseData = await response.json();
        
        return responseData.resultado; // Ahora sí retorna el valor

    } catch (error) {
        console.error('Error:', error);
        return "Error al conectar con el servidor";
    }
}

// Ejemplo de uso
const diagnostic = [
    {"hecho": "sintoma_boton", "valor": "seco_caido"},
    {"hecho": "sintoma_boton", "valor": "perforado"},
    {"hecho": "sintoma_fruto", "valor": "escasos"},
    {"hecho": "sintoma_hoja", "valor": "mordidas_agujeros"},
    {"hecho": "sintoma_fruto", "valor": "danados"},
    {"hecho": "presencia_insecto", "valor": "gusanos_verdes_pequen"}

];

// 4. IMPORTANTE: Como post_diagnostic es asíncrona, devuelve una Promesa.
// Tienes que usar .then() o estar dentro de otra función async para ver el resultado.

// Opción A: Usando .then (estilo clásico)
post_diagnostic(diagnostic).then(resultado => {
    console.log("Resultado final:", resultado);
});
