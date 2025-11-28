const sintomasSeleccionadosDiv = document.getElementById("sintomas-seleccionados");
const listaSintomasDiv = document.getElementById("lista-sintomas");

window.addEventListener("load", () => {
    const img = document.getElementById("img-base");
    const svg = document.getElementById("svg-overlay");

    // Ajusta el SVG al tamaño real renderizado de la imagen
    const resizeSVG = () => {
        svg.style.width = img.clientWidth + "px";
        svg.style.height = img.clientHeight + "px";
    };

    resizeSVG();
    window.addEventListener("resize", resizeSVG);
});


// Evento: clic en una parte del SVG
document.querySelectorAll(".parte").forEach(elem => {
    elem.addEventListener("click", () => {
        const parte = elem.dataset.parte;

        // Solicita los síntomas desde Flask según la parte
        fetch(`/sintomas/${parte}`)
            .then(r => r.json())
            .then(data => {
                mostrarSintomasDe(parte, data.sintomas);
            });
    });
});

// Mostrar lista de síntomas según la parte
function mostrarSintomasDe(parte, sintomas) {
    listaSintomasDiv.innerHTML = "";

    sintomas.forEach(s => {
        const id = parte + "_" + s;

        listaSintomasDiv.innerHTML += `
            <div class="form-check">
                <input class="form-check-input sintoma-check"
                    type="checkbox"
                    value="${parte}:${s}"
                    id="${id}">
                <label class="form-check-label" for="${id}">
                    ${s.replace('_',' ')}
                </label>
            </div>`;
    });

    actualizarEventosCheckbox();
}

// Actualizar lista de síntomas seleccionados
function actualizarEventosCheckbox() {
    document.querySelectorAll(".sintoma-check").forEach(chk => {
        chk.addEventListener("change", () => {
            const seleccionados = [...document.querySelectorAll(".sintoma-check:checked")]
                .map(c => c.value.replace("sintoma_", "").replace("_", " "));

            sintomasSeleccionadosDiv.innerHTML =
                seleccionados.length
                    ? "• " + seleccionados.join("<br>• ")
                    : "<span class='text-muted'>Ninguno aún</span>";
        });
    });
}



document.querySelectorAll(".parte").forEach(elemento => {
    elemento.addEventListener("click", () => {
        const parte = elemento.getAttribute("data-parte");

        // Mostrar el nombre seleccionado (solo para pruebas)
        let box = document.getElementById("parte-seleccionada-temp");

        if (!box) {
            box = document.createElement("div");
            box.id = "parte-seleccionada-temp";
            box.className = "alert alert-info mt-3 text-center fw-bold";
            document.querySelector(".svg-container").appendChild(box);
        }

        box.textContent = "Parte seleccionada: " + parte;
    });
});
