import tkinter as tk
from tkinter import ttk, messagebox
from gui.datos_ejemplo import EJEMPLOS_DETALLADOS

class SymptomSelector:
    def __init__(self, parent, search_callback=None):
        self.parent = parent
        self.symptoms = []
        self.search_callback = search_callback
        self.setup_ui()
        
    def setup_ui(self):
        # Frame principal
        self.main_frame = ttk.Frame(self.parent)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Título
        title_label = tk.Label(
            self.main_frame,
            text="🔍 SISTEMA EXPERTO - IDENTIFICACIÓN DE ENFERMEDADES EN FRESAS",
            font=("Arial", 14, "bold"),
            fg="#2C3E50"
        )
        title_label.pack(pady=(0, 20))
        
        # Frame de selección
        selection_frame = ttk.LabelFrame(self.main_frame, text="Seleccionar Síntomas", padding=15)
        selection_frame.pack(fill=tk.BOTH, expand=True)
        
        # Categoría
        ttk.Label(selection_frame, text="Categoría:").grid(row=0, column=0, sticky="w", pady=5)
        self.category_var = tk.StringVar()
        self.category_combo = ttk.Combobox(
            selection_frame,
            textvariable=self.category_var,
            values=list(EJEMPLOS_DETALLADOS.keys()),
            state="readonly",
            width=30
        )
        self.category_combo.grid(row=0, column=1, padx=10, pady=5, sticky="ew")
        self.category_combo.bind('<<ComboboxSelected>>', self.on_category_selected)
        
        # Síntoma
        ttk.Label(selection_frame, text="Síntoma:").grid(row=1, column=0, sticky="w", pady=5)
        self.symptom_var = tk.StringVar()
        self.symptom_combo = ttk.Combobox(
            selection_frame,
            textvariable=self.symptom_var,
            state="readonly",
            width=30
        )
        self.symptom_combo.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
        
        # Botones
        button_frame = ttk.Frame(selection_frame)
        button_frame.grid(row=2, column=0, columnspan=2, pady=15)
        
        ttk.Button(
            button_frame,
            text="➕ Agregar Síntoma",
            command=self.add_symptom
        ).pack(side=tk.LEFT, padx=5)
        
        # Guardar referencia al botón de búsqueda
        self.search_button = ttk.Button(
            button_frame,
            text="🔍 Realizar Búsqueda",
            command=self.perform_search
        )
        self.search_button.pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            button_frame,
            text="🗑️ Limpiar Lista",
            command=self.clear_symptoms
        ).pack(side=tk.LEFT, padx=5)
        
        # Lista de síntomas agregados
        list_frame = ttk.LabelFrame(self.main_frame, text="Síntomas Seleccionados", padding=10)
        list_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.symptoms_listbox = tk.Listbox(
            list_frame,
            font=("Arial", 10),
            height=8
        )
        self.symptoms_listbox.pack(fill=tk.BOTH, expand=True)
        
        # Scrollbar para la lista
        scrollbar = ttk.Scrollbar(self.symptoms_listbox)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.symptoms_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.symptoms_listbox.yview)
        
        # Configurar grid weights
        selection_frame.columnconfigure(1, weight=1)
        
    def on_category_selected(self, event):
        category = self.category_var.get()
        if category in EJEMPLOS_DETALLADOS:
            symptoms = EJEMPLOS_DETALLADOS[category]["valores"]
            self.symptom_combo['values'] = symptoms
            if symptoms:
                self.symptom_combo.set(symptoms[0])
    
    def add_symptom(self):
        category = self.category_var.get()
        symptom = self.symptom_var.get()
        
        if not category or not symptom:
            messagebox.showwarning("Advertencia", "Por favor seleccione una categoría y un síntoma")
            return
        
        symptom_data = {"hecho": category, "valor": symptom}
        
        # Verificar si ya existe
        for existing in self.symptoms:
            if existing["hecho"] == category and existing["valor"] == symptom:
                messagebox.showinfo("Información", "Este síntoma ya fue agregado")
                return
        
        self.symptoms.append(symptom_data)
        self.update_symptoms_list()
        
        # Limpiar selección
        self.symptom_var.set("")
    
    def clear_symptoms(self):
        self.symptoms.clear()
        self.update_symptoms_list()
    
    def update_symptoms_list(self):
        self.symptoms_listbox.delete(0, tk.END)
        for symptom in self.symptoms:
            display_text = f"{symptom['hecho']}: {symptom['valor']}"
            self.symptoms_listbox.insert(tk.END, display_text)
    
    def perform_search(self):
        if not self.symptoms:
            messagebox.showwarning("Advertencia", "Por favor agregue al menos un síntoma")
            return
        
        # Si hay un callback, llamarlo con los síntomas
        if self.search_callback:
            self.search_callback(self.symptoms)
        else:
            # Devolver los síntomas para compatibilidad
            return self.symptoms
    
    def get_symptoms(self):
        return self.symptoms.copy()