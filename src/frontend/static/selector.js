const sintomasSeleccionadosDiv = document.getElementById("sintomas-seleccionados");
const listaSintomasDiv = document.getElementById("lista-sintomas");
// Array global para almacenar síntomas seleccionados
// Los sintomas se almacenan como {"hecho": "sintoma_hoja", "valor": "danada", "nombre": "dañada", parte: "hoja"}
window.sintomasSeleccionados = [];

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
        const clave = elem.dataset.clave;

        obtenerSintomasParaParte(clave).then(sintomas => {
            mostrarSintomasDe(parte, sintomas);
        });
    });
});


// Mostrar lista de síntomas según la parte
function mostrarSintomasDe(parte, sintomas) {
    listaSintomasDiv.innerHTML = "";

    sintomas.forEach(s => {
        const id = parte + "_" + s;
        const valor = s[0];
        
        // Verificar si el síntoma ya está seleccionado
        const estaSeleccionado = window.sintomasSeleccionados.some(
            sel => sel.parte === parte && sel.valor === valor
        );

        listaSintomasDiv.innerHTML += `
            <button class="btn btn-outline-primary sintoma-check my-1 ${estaSeleccionado ? 'active' : ''}"
            type="button"
            value="${parte}:${valor}"
            name="${s[1]}"
            id="${id}">
            + ${s[1]}
            </button>`;
    });

    actualizarEventosCheckbox();
}

// evento cuando se presiona el boton para agregar sintoma
function actualizarEventosCheckbox() {
    document.querySelectorAll(".sintoma-check").forEach(btn => {
        btn.addEventListener("click", () => {
            if (!btn.classList.contains("active")) {
                btn.classList.toggle("active");
                agregarSintoma(btn.value, btn.name);
            }
        });
    });
}

// Agregar síntoma seleccionado al div correspondiente
// sintoma es el valor de la caracteristica value del boton (deveria de ser parte:sintoma)
// nombre es el texto que se muestra en el boton, su forma normal de escribirlo
// ejemplo: valor = "hoja:danada", nombre = "Hoja dañada"
// lo agrega a la variable global window.sintomasSeleccionados y actauliza actualizarSintomasSeleccionadosDiv
function agregarSintoma(sintoma, nombre) {
    const parte = sintoma.split(":")[0];
    const desc = sintoma.split(":")[1];
    
    // agregar a variable global
    const sintomaObj = { "hecho": parte, "valor": desc, "nombre": nombre, "parte": parte };

    // Verificar si ya existe
    const index = window.sintomasSeleccionados.findIndex(s => s.hecho === parte && s.valor === desc);

    if (index === -1) {
        // No existe, agregar
        window.sintomasSeleccionados.push(sintomaObj);
    }

    // Actualizar el div de síntomas seleccionados
    actualizarSintamasSeleccionadosDiv();
}

// Actualizar el div de síntomas seleccionados segun lo que se encuentre dentro de window.sintomasSeleccionados
function actualizarSintamasSeleccionadosDiv() {
    console.log("Síntomas seleccionados:", window.sintomasSeleccionados);
    sintomasSeleccionadosDiv.innerHTML =
        window.sintomasSeleccionados.length
            ? `<ul class="list-unstyled">` + window.sintomasSeleccionados.map((s, idx) => `
                <li class="mb-2 d-flex align-items-center">
                    <button class="btn btn-sm btn-danger sintoma-remove" 
                            data-index="${idx}"
                            data-parte="${s.parte}"
                            data-valor="${s.valor}">
                        −
                    </button>
                    <span class="ms-2">${s.parte}: ${s.nombre}</span>
                </li>
              `).join("") + `</ul>`
            : "<span class='text-muted'>Ninguno aún</span>";
    removerSintomaEvento();
}

// Evento para remover síntoma seleccionado de la lista con el boton en sintomas seleccionados
function removerSintomaEvento() {
    document.querySelectorAll(".sintoma-remove").forEach(btn => {
        btn.addEventListener("click", () => {
            const index = btn.dataset.index;
            const parte = btn.dataset.parte;
            const valor = btn.dataset.valor;
            
            
            // Remover la clase "active" del botón correspondiente
            const sintomaBtnId = parte + "_" + valor;
            const sintomaBtnId2 = parte + "_" + parte + ":" + valor;
            const sintomaBtn = document.getElementById(sintomaBtnId) || 
                            document.getElementById(sintomaBtnId2) ||
                            document.querySelector(`.sintoma-check[value="${parte}:${valor}"]`);
            
            if (sintomaBtn) {
                sintomaBtn.classList.remove("active");
            }

            // Remover de la variable global
            console.log("Removiendo síntoma:", parte, valor);
            window.sintomasSeleccionados = window.sintomasSeleccionados.filter((sintoma) => !(sintoma.parte == parte && sintoma.valor == valor));
            
            actualizarSintamasSeleccionadosDiv();
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

// Función para obtener síntomas según la parte seleccionada
// clave es el identificador de la parte segun el json
async function obtenerSintomasParaParte(clave) {
  return fetch('/static/data/sintomas.json')
    .then(res => res.json())
    .then(data => {
    return data[clave] || data;
  });
}
