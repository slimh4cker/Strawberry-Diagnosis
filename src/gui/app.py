import tkinter as tk
from tkinter import ttk, messagebox
import motores.retornar_concordancias
import lib.obtener_base
from gui.selector_sintoma import SymptomSelector
from gui.results import ResultsDisplay

class StrawberryExpertApp:
    def __init__(self):
        self.root = tk.Tk()
        self.setup_window()
        self.setup_ui()
        self.load_knowledge_base()
        
    def setup_window(self):
        self.root.title("Sistema Experto - Enfermedades de Fresas")
        self.root.geometry("800x600")
        self.root.minsize(700, 500)
        
        # Centrar ventana
        self.root.eval('tk::PlaceWindow . center')
        
    def setup_ui(self):
        # Notebook para pestañas
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Pestaña de búsqueda
        self.search_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.search_tab, text="🔍 Búsqueda de Enfermedades")
        
        # Pestaña de información
        self.info_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.info_tab, text="📚 Información")
        
        # Configurar pestañas
        self.setup_search_tab()
        self.setup_info_tab()
        
    def setup_search_tab(self):
        # Frame principal para la pestaña de búsqueda
        search_main_frame = ttk.Frame(self.search_tab)
        search_main_frame.pack(fill=tk.BOTH, expand=True)
        
        self.symptom_selector = SymptomSelector(search_main_frame, self.perform_search)
    
        separator = ttk.Separator(search_main_frame, orient='horizontal')
        separator.pack(fill=tk.X, padx=20, pady=10)
        
        self.results_display = ResultsDisplay(search_main_frame)
        self.results_display.main_frame.pack(fill=tk.BOTH, expand=True)
        
    def setup_info_tab(self):
        info_text = """
SISTEMA EXPERTO PARA IDENTIFICACIÓN DE ENFERMEDADES EN FRESAS

Este sistema le ayudará a identificar posibles enfermedades y plagas 
que afectan a sus plantas de fresa basándose en los síntomas observados.

INSTRUCCIONES:

1. Seleccione una categoría de síntoma (hojas, frutos, raíces, etc.)
2. Elija el síntoma específico observado
3. Haga clic en 'Agregar Síntoma' para añadirlo a la lista
4. Repita el proceso para agregar todos los síntomas observados
5. Haga clic en 'Realizar Búsqueda' para obtener diagnósticos

CARACTERÍSTICAS:

• Identifica más de 30 enfermedades diferentes
• Basado en una base de conocimiento especializada
• Interfaz intuitiva y fácil de usar
• Resultados instantáneos

Nota: Cuantos más síntomas precise, más exacto será el diagnóstico.
        """
        
        info_label = tk.Label(
            self.info_tab,
            text=info_text,
            font=("Arial", 10),
            justify="left",
            padx=20,
            pady=20
        )
        info_label.pack(fill=tk.BOTH, expand=True)
        
    def load_knowledge_base(self):
        try:
            self.base_conocimiento = lib.obtener_base.obtener_base()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar la base de conocimiento: {e}")
            self.base_conocimiento = None
    
    def perform_search(self, symptoms=None):
        # Si no se pasan síntomas, obtenerlos del selector
        if symptoms is None:
            symptoms = self.symptom_selector.get_symptoms()
        
        if not symptoms:
            messagebox.showwarning("Advertencia", "Por favor agregue al menos un síntoma")
            return
        
        if not self.base_conocimiento:
            messagebox.showerror("Error", "Base de conocimiento no disponible")
            return
        
        try:
            # Realizar búsqueda
            resultados = motores.retornar_concordancias.iniciar_busqueda(
                symptoms, 
                self.base_conocimiento
            )
            
            # Mostrar resultados
            self.results_display.show_results(resultados)
            
        except Exception as e:
            messagebox.showerror("Error", f"Error durante la búsqueda: {e}")
    
    def run(self):
        # Configurar el botón de búsqueda para usar nuestro método
        # Necesitamos modificar el SymptomSelector para que llame a esta función
        self.root.mainloop()

# Integracion
def create_integrated_app():
    app = StrawberryExpertApp()
    
    # Sobrescribir el método perform_search del selector
    original_perform_search = app.symptom_selector.perform_search
    
    def integrated_perform_search():
        symptoms = original_perform_search()
        if symptoms:
            app.perform_search()
    
    app.symptom_selector.perform_search = integrated_perform_search
    
    return app