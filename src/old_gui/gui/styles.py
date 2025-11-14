class Styles:
    # Colores
    PRIMARY = "#2E86AB"
    SECONDARY = "#A23B72"
    SUCCESS = "#18A558"
    WARNING = "#F39C12"
    DANGER = "#E74C3C"
    LIGHT = "#ECF0F1"
    DARK = "#2C3E50"
    
    # Fuentes
    TITLE_FONT = ("Arial", 16, "bold")
    HEADER_FONT = ("Arial", 12, "bold")
    NORMAL_FONT = ("Arial", 10)
    SMALL_FONT = ("Arial", 9)
    
    # Configuración de widgets
    BUTTON_STYLE = {
        "bg": PRIMARY,
        "fg": "white",
        "font": NORMAL_FONT,
        "relief": "flat",
        "bd": 0,
        "padx": 15,
        "pady": 8
    }
    
    ENTRY_STYLE = {
        "font": NORMAL_FONT,
        "relief": "solid",
        "bd": 1
    }
    
    FRAME_STYLE = {
        "bg": LIGHT,
        "relief": "flat",
        "bd": 1
    }