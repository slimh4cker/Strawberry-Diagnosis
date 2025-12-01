import { processDiagnosticSource } from "./DiagnosticoCard.js";
import { post_diagnostic } from "./getDiagnostic.js";
// Si luego quieren usar la API real:
// import { post_diagnostic } from "./getDiagnostic.js";

// TODO alert si se seleccionan 1 o menos sintomas
document.getElementById("btn-diagnosticar").addEventListener("click", async () => {
    // Los sintomas seleccionados están en la variable global window.sintomasSeleccionados

    // se eliminan los datos no necesarios para el backend
    // Los sintomas se almacenan como {"hecho": "sintoma_hoja", "valor": "danada", "nombre": "dañada", parte: "hoja"}
    // solo nos quedamos con hehco y valor
    const seleccionados = window.sintomasSeleccionados.map(s => {
        return {"hecho": s.hecho, "valor": s.valor};
    });

    const data = await post_diagnostic(seleccionados);   // usa lo que ya existía
    // luego se cambiara por const data = await post_diagnostic(seleccionados);

    processDiagnosticSource(data);    // muestra la tarjeta
});
