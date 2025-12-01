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

    const recomendacion =
        diag?.conclusion?.recomendacion ||
        "No hay recomendaciones disponibles.";

    const listaCondiciones = diag.condiciones
        .map(c => {
            const hecho = c.hecho.replace("sintoma_", "").replace("_", " ");
            const valor = c.valor.replace("_", " ");
            return `<li><strong>${hecho}:</strong> ${valor}</li>`;
        })
        .join("");

    const html = `
        <div class="diagnostic-header">
            <span>${titulo}</span>
            <span class="status-icon">✔</span>
        </div>

        <p class="diagnostic-description">
            <strong>Síntomas característicos:</strong>
        </p>

        <ul class="diagnostic-description">
            ${listaCondiciones}
        </ul>

        <div class="diagnostic-recommendation">
            <strong>Recomendación:</strong><br>
            ${recomendacion}
        </div>
    `;

    updateContainer(html);

    // Mostrar con animación
    document.getElementById("diagnostic-result").classList.add("show");
}



export function renderMessage(message) {
    const html = `
        <div class="diagnostic-header">
            <span>Mensaje</span>
            <span class="status-icon warning">⚠</span>
        </div>

        <p class="diagnostic-description text-center">
            ${message}
        </p>
    `;
    updateContainer(html);
    document.getElementById("diagnostic-result").classList.add("show");
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
            <div style="margin-bottom: 1.5rem; padding: 1rem; border-radius: 12px; background: #f8f9fa; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
                <div class="diagnostic-header">
                    <span>${titulo}</span>
                    <span class="status-icon">✔</span>
                </div>

                <p class="diagnostic-description"><strong>Síntomas característicos:</strong></p>

                <ul class="diagnostic-description">${listaCondiciones}</ul>
            </div>
        `;
    }

    updateContainer(html);
    document.getElementById("diagnostic-result").classList.add("show");
    return;
}


    // Caso 3: API real regresa objeto diagnóstico
    if (typeof data === "object" && data !== null) {
        return renderDiagnosticCard(data);
    }

    // Caso 4: Nada útil
    return renderMessage("No se pudo generar diagnóstico.");
}