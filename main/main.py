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
        rx.box(
            rx.box(
                rx.box(palette_editor(), class_name=COL_SPAN_2),
                rx.box(saved_palettes(), class_name=COL_SPAN_1),
                class_name=GRID_3_COLS,
            ),
            class_name=CONTENT_WRAPPER
        ),
        class_name=PAGE
    )


app = rx.App()
app.add_page(
    index, 
    title="DAVS Mis Colores",
    on_load=PaletteState.load_saved_palettes
)

