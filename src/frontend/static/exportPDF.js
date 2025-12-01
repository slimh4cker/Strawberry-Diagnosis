const { jsPDF } = window.jspdf;

// Convierte los síntomas a filas de tabla
function formatConditionsTable(conditions) {
    return conditions.map(c => [
        c.hecho.replace("sintoma_", "").replace(/_/g, " "),
        c.valor.replace(/_/g, " ")
    ]);
}

// Añade número de página
function addPageNumber(doc, pageNumber) {
    doc.setFontSize(10);
    doc.text(`Página ${pageNumber}`, 105, 290, { align: "center" });
}

export function exportSingleDiagnosticPDF(diag, filename = "diagnostico.pdf") {
    const doc = new jsPDF();

    // Encabezado
    doc.setFillColor(240, 240, 240);
    doc.rect(0, 0, 210, 25, "F");
    doc.setFontSize(16);
    doc.setTextColor(34, 139, 34); // verde oscuro
    doc.setFont(undefined, "bold");
    doc.text("Resultado del Diagnóstico", 105, 15, { align: "center" });

    let y = 35;
    const titulo = diag?.conclusion?.diagnostico || diag?.nombre || "Diagnóstico sin nombre";

    // Título del diagnóstico
    doc.setFontSize(14);
    doc.setTextColor(0, 0, 0);
    doc.setFont(undefined, "bold");
    doc.text(`Diagnóstico: ${titulo}`, 20, y);
    y += 10;

    // Tabla de síntomas
    const tableBody = formatConditionsTable(diag.condiciones);

    doc.autoTable({
        startY: y,
        head: [['Síntoma', 'Valor']],
        body: tableBody,
        theme: 'grid',
        styles: { fontSize: 12 },
        headStyles: { fillColor: [34, 139, 34], textColor: 255, halign: 'center' },
        columnStyles: { 0: { cellWidth: 80 }, 1: { cellWidth: 90 } }
    });

    addPageNumber(doc, 1);
    doc.save(filename);
}

export function exportAllDiagnosticsPDF(lista, filename = "diagnosticos_completos.pdf") {
    const doc = new jsPDF();
    let pageNumber = 1;
    let y = 35;

    // Encabezado general
    doc.setFillColor(240, 240, 240);
    doc.rect(0, 0, 210, 25, "F");
    doc.setFontSize(16);
    doc.setTextColor(34, 139, 34);
    doc.setFont(undefined, "bold");
    doc.text("Diagnósticos Generados", 105, 15, { align: "center" });

    lista.forEach((diag, index) => {
        if (y > 260) {
            addPageNumber(doc, pageNumber);
            doc.addPage();
            pageNumber++;
            y = 35;
        }

        // Título diagnóstico
        doc.setFontSize(13);
        doc.setFont(undefined, "bold");
        doc.text(`(${index + 1}) ${diag.conclusion?.diagnostico || diag.nombre}`, 20, y);
        y += 8;

        // Tabla de síntomas
        const tableBody = formatConditionsTable(diag.condiciones);

        doc.autoTable({
            startY: y,
            head: [['Parte', 'Sintoma']],
            body: tableBody,
            theme: 'grid',
            styles: { fontSize: 12 },
            headStyles: { fillColor: [34, 139, 34], textColor: 255, halign: 'center' },
            columnStyles: { 0: { cellWidth: 80 }, 1: { cellWidth: 90 } }
        });

        y = doc.lastAutoTable.finalY + 10;
    });

    addPageNumber(doc, pageNumber);
    doc.save(filename);
}
