import reflex as rx
from main.components.styles import (NAVBAR_WRAPPER, NAVBAR_INNER, NAVBAR_LOGO, NAVBAR_LOGO_ICON, NAVBAR_LOGO_TEXT, NAVBAR_ACTIONS, BTN_GHOST, BTN_PRIMARY, BTN_GHOST_RED)
from main.state.palette_state import PaletteState

def navbar() -> rx.Component:
    return rx.box(
        rx.box(
            #Logo
            rx.box(
                rx.icon("palette", size=30, class_name=NAVBAR_LOGO_ICON), # <-- Ícono cambiado
                rx.text("DAVS Mis Colores", class_name=NAVBAR_LOGO_TEXT), # <-- Título cambiado
                class_name=NAVBAR_LOGO,
            ),
            rx.box(class_name="flex-1"),
            
            #Botones
            rx.box(
                rx.button(
                    rx.icon("clipboard-copy", size=16),
                    "Copiar todos",
                    on_click=[
                        rx.set_clipboard(PaletteState.all_colors_text),
                        PaletteState.notify_copied_all(),
                    ],
                    class_name=BTN_GHOST_RED, # <-- Aquí aplicamos el nuevo estilo
                ),
                rx.button(
                    rx.icon("bookmark", size=16),
                    "Guardar",
                    on_click=PaletteState.open_save_dialog(),
                    class_name=BTN_PRIMARY
                ),
                class_name=NAVBAR_ACTIONS,
            ),
            class_name=NAVBAR_INNER
        ),
        class_name=NAVBAR_WRAPPER,
        style={
            "backdrop_filter": "blur(20px)",
            "background": "#000000" # <-- Cambiado de rgba(255,255,255,0.8) a negro absoluto
        }
    )


