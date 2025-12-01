import { processDiagnosticSource } from "./DiagnosticoCard.js";
import { post_diagnostic } from "./getDiagnostic.js";

// Si luego quieren usar la API real:
// import { post_diagnostic } from "./getDiagnostic.js";

// TODO alert si se seleccionan 1 o menos sintomas
document.getElementById("btn-diagnosticar").addEventListener("click", async () => {
    // Los sintomas seleccionados están en la variable global window.sintomasSeleccionados

    // Validar que haya al menos 2 sintomas
    if (window.sintomasSeleccionados.length < 2) {
        mostrarModal("Ha seleccionado muy pocos síntomas. Por favor selecciona al menos 2.");
        return;
    }

    // se eliminan los datos no necesarios para el backend
    // Los sintomas se almacenan como {"hecho": "sintoma_hoja", "valor": "danada", "nombre": "dañada", parte: "hoja"}
    // solo nos quedamos con hehco y valor
    const seleccionados = window.sintomasSeleccionados.map(s => {
        return {"hecho": s.hecho, "valor": s.valor};
    });

    const data = await post_diagnostic(seleccionados);   // usa lo que ya existía
    // luego se cambiara por const data = await post_diagnostic(seleccionados);

    processDiagnosticSource(data);    // muestra la tarjeta
    const resultContainer = document.getElementById("diagnostic-result");
    resultContainer.classList.add("show");
    resultContainer.scrollIntoView({ behavior: "smooth", block: "start" });
});

function mostrarModal(mensaje) {
    const modalEl = document.getElementById('modalAlerta');
    const modalBody = document.getElementById('modalAlertaMensaje');
    modalBody.textContent = mensaje;

    const modalBootstrap = new bootstrap.Modal(modalEl); // Inicializa el modal
    modalBootstrap.show();
}