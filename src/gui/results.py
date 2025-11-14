import tkinter as tk
from tkinter import ttk

class ResultsDisplay:
    def __init__(self, parent):
        self.parent = parent
        self.setup_ui()
        
    def setup_ui(self):
        # Frame principal que se expandirá
        self.main_frame = ttk.Frame(self.parent)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.main_frame, bg="white")
        self.scrollbar = ttk.Scrollbar(self.main_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.bind("<Configure>", self.on_canvas_configure)
        
    def on_canvas_configure(self, event):
        self.canvas.itemconfig("all", width=event.width)
        
    def show_results(self, resultados):
        # Limpiar resultados anteriores
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        
        if not resultados:
            no_results_label = tk.Label(
                self.scrollable_frame,
                text="❌ No se encontraron enfermedades que coincidan con los síntomas",
                font=("Arial", 12),
                fg="red",
                bg="white",
                pady=20,
                wraplength=600
            )
            no_results_label.pack(fill=tk.X, padx=20, pady=10)
            return
        
        # Título de resultados
        results_title = tk.Label(
            self.scrollable_frame,
            text=f"✅ Se encontraron {len(resultados)} enfermedad(es):",
            font=("Arial", 12, "bold"),
            fg="green",
            bg="white",
            anchor="w"
        )
        results_title.pack(fill=tk.X, padx=20, pady=(10, 20))
        
        # Mostrar cada resultado
        for i, resultado in enumerate(resultados, 1):
            self.create_result_card(resultado, i)
    
    def create_result_card(self, resultado, index):
        card_frame = ttk.LabelFrame(
            self.scrollable_frame,
            text=f"🏥 {index}. {resultado.get('nombre', 'Sin nombre')}",
            padding=15
        )
        card_frame.pack(fill=tk.X, padx=20, pady=5, ipady=5)
        
        # Síntomas coincidentes
        condiciones = resultado.get('condiciones', [])
        
        if condiciones:
            symptoms_label = tk.Label(
                card_frame,
                text="Síntomas coincidentes:",
                font=("Arial", 10, "bold"),
                anchor="w"
            )
            symptoms_label.pack(anchor="w", pady=(0, 10))
            
            # Frame para síntomas
            symptoms_frame = ttk.Frame(card_frame)
            symptoms_frame.pack(fill=tk.X, padx=10)
            
            for cond in condiciones:
                if isinstance(cond, dict):
                    symptom_text = f"• {cond.get('valor', '')}"
                else:
                    symptom_text = f"• {cond}"
                
                symptom_label = tk.Label(
                    symptoms_frame,
                    text=symptom_text,
                    font=("Arial", 9),
                    anchor="w",
                    justify="left"
                )
                symptom_label.pack(anchor="w", padx=5, pady=1)
        
    def show_results(self, resultados):
        # Limpiar resultados anteriores
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        
        if not resultados:
            no_results_label = tk.Label(
                self.scrollable_frame,
                text="❌ No es posible diagnosticar una enfermedad con los sintomas proporcionados",
                font=("Arial", 12),
                fg="red",
                bg="white",
                pady=20
            )
            no_results_label.pack(fill=tk.X, padx=20, pady=10)
            return
        
        # Título de resultados
        results_title = tk.Label(
            self.scrollable_frame,
            text=f"✅ Se encontraron {len(resultados)} enfermedad(es):",
            font=("Arial", 12, "bold"),
            fg="green",
            bg="white"
        )
        results_title.pack(fill=tk.X, padx=20, pady=(10, 20))
        
        # Mostrar cada resultado
        for i, resultado in enumerate(resultados, 1):
            self.create_result_card(resultado, i)
    
    def create_result_card(self, resultado, index):
        card_frame = ttk.LabelFrame(
            self.scrollable_frame,
            text=f"🏥 {index}. {resultado.get('nombre', 'Sin nombre')}",
            padding=15
        )
        card_frame.pack(fill=tk.X, padx=20, pady=10, ipady=5)
        
        # Síntomas coincidentes
        condiciones = resultado.get('condiciones', [])
        
        if condiciones:
            symptoms_label = tk.Label(
                card_frame,
                text="Síntomas incluidos:",
                font=("Arial", 10, "bold"),
                anchor="w"
            )
            symptoms_label.pack(anchor="w", pady=(0, 10))
            
            # Frame para síntomas
            symptoms_frame = ttk.Frame(card_frame)
            symptoms_frame.pack(fill=tk.X, padx=10)
            
            for cond in condiciones:
                if isinstance(cond, dict):
                    symptom_text = f"• {cond.get('valor', '')}"
                else:
                    symptom_text = f"• {cond}"
                
                symptom_label = tk.Label(
                    symptoms_frame,
                    text=symptom_text,
                    font=("Arial", 9),
                    anchor="w",
                    justify="left"
                )
                symptom_label.pack(anchor="w", padx=5)