import { processDiagnosticSource } from "./DiagnosticoCard.js";
import { get_dummy } from "./getDiagnostic.js";
// Si luego quieren usar la API real:
// import { post_diagnostic } from "./getDiagnostic.js";

document.getElementById("btn-diagnosticar").addEventListener("click", async () => {

    const data = await get_dummy();   // usa lo que ya existía
    // luego se cambiara por const data = await post_diagnostic(seleccionados);
    processDiagnosticSource(data);    // muestra la tarjeta
});
