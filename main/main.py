import reflex as rx
from .components.navbar import navbar
from .components.styles import PAGE, CONTENT_WRAPPER, GRID_3_COLS, COL_SPAN_1, COL_SPAN_2
from .components.palette_editor import palette_editor
from .components.seved_palette import saved_palettes
from .state.palette_state import PaletteState


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.box(
        navbar(),
        # Contenedor principal del contenido
        rx.box(
            rx.box(
                rx.box(palette_editor(), class_name=COL_SPAN_2),
                rx.box(saved_palettes(), class_name=COL_SPAN_1),
                class_name=GRID_3_COLS,
            ),
            class_name=CONTENT_WRAPPER,
            # Esto empuja el footer hacia el final de la pantalla
            flex_grow="1", 
        ),
        
        # ==== FOOTER ====
        rx.box(
            rx.text(
                "Desarrollado por: Diego Videla Silva",
                size="2",
                # Un gris azulado claro para que contraste con el fondo oscuro
                color="#94A3B8", 
            ),
            rx.image("/DAVS.png", width="70px"),
            rx.text(
                "© 2026 Mis Colores. Todos los derechos reservados.",
                size="2",
                color="#94A3B8",
                text_align="center",
            ),
            width="100%",
            # Fondo negro puro para que haga juego con el Navbar
            background_color="#000000", 
            display="flex",
            # Responsivo: Columna en móviles, fila en escritorio
            flex_direction=rx.breakpoints(initial="column", sm="row"),
            justify_content="space-between",
            align_items="center",
            padding_x="4",
            padding_y=rx.breakpoints(initial="4", sm="2"),
            gap="3",
            # Un borde superior sutil igual al del Navbar
            border_top="1px solid rgba(255,255,255,0.08)",
        ),
        
        class_name=PAGE
    )


app = rx.App()
app.add_page(
    index, 
    title="DAVS Mis Colores",
    on_load=PaletteState.load_saved_palettes
)