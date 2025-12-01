/**
 * Es un modulo para mostrar tarjetas de el diagnostico en 
 * el frontend
 * Funciona tanto con datos que vengan de 
 * get_dummy() (para pruebas)
 * post_diagnostic()
 */


function updateContainer(html) {
    const cont = document.getElementById("diagnostic-result");
    if (!cont) {
        console.error("ERROR: Falta el contenedor #diagnostic-result en el HTML.");
        return;
    }
    cont.innerHTML = html;
}

//Renderiza la tarjeta del dignostico basado en el JSON

export function renderDiagnosticCard(diag) {

    const titulo =
        diag?.conclusion?.diagnostico ||
        diag?.nombre ||
        "Diagnóstico sin nombre";

    const listaCondiciones = diag.condiciones
        .map(c => {
            const hecho = c.hecho.replace("sintoma_", "").replace("_", " ");
            const valor = c.valor.replace("_", " ");
            return `<li><strong>${hecho}:</strong> ${valor}</li>`;
        })
        .join("");

    //Construir tarjeta
    const html = `
        <div class="card shadow-sm p-3" style="max-width: 600px; margin: auto;">
            <h4 class="text-success mb-2">🩺 ${titulo}</h4>

            <p class="fw-semibold mt-3 mb-1">Síntomas característicos:</p>
            <ul>
                ${listaCondiciones}
            </ul>
        </div>
    `;

    updateContainer(html);
}


export function renderMessage(message) {
    const html = `
        <div class="card shadow-sm p-3 bg-light" style="max-width: 600px; margin: auto;">
            <p class="text-center fw-semibold">${message}</p>
        </div>
    `;
    updateContainer(html);
}

export function processDiagnosticSource(data) {

    // Caso 1: API regresa error 
    if (data.error) {
        return renderMessage(data.error);
    }

    // Caso 2: API dummy regresa lista de diagnósticos
if (Array.isArray(data) && data.length > 0) {
    let html = "";

    for (const diag of data) {
        const titulo =
            diag?.conclusion?.diagnostico ||
            diag?.nombre ||
            "Diagnóstico sin nombre";

        const listaCondiciones = diag.condiciones
            .map(c => {
                const hecho = c.hecho.replace("sintoma_", "").replace("_", " ");
                const valor = c.valor.replace("_", " ");
                return `<li><strong>${hecho}:</strong> ${valor}</li>`;
            })
            .join("");

        html += `
            <div class="card shadow-sm p-3 mb-3" style="max-width: 600px; margin: auto;">
                <h4 class="text-success mb-2">🩺 ${titulo}</h4>
                <p class="fw-semibold mt-3 mb-1">Síntomas característicos:</p>
                <ul>${listaCondiciones}</ul>
            </div>
        `;
    }

    updateContainer(html);
    return;
}


    // Caso 3: API real regresa objeto diagnóstico
    if (typeof data === "object" && data !== null) {
        return renderDiagnosticCard(data);
    }

    // Caso 4: Nada útil
    return renderMessage("No se pudo generar diagnóstico.");
}