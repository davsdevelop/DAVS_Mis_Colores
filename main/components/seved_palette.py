import reflex as rx

from main.state.palette_state import PaletteState
from main.model.palette import Palette

from .styles import (CARD_SCROLLABLE, PALETTE_ROW, PALETTE_ROW_BTNS, PALETTE_ROW_DATE, PALETTE_ROW_INFO, PALETTE_ROW_NAME, PALETTE_ROW_PREVIEW, PALETTES_COUNT, PALETTES_LIST, PALETTES_TITLE, BTN_ICON, BTN_ICON_DANGER, EMPTY_STATE, EMPTY_STATE_ICON, EMPTY_STATE_SUBTEXT, EMPTY_STATE_TEXT)

def icon_main(icon: str, title: str, on_click= rx.event.EventHandler) -> rx.Component:
    return rx.icon_button(
        rx.icon(icon, size=14),
        on_click=on_click,
        title=title,
        class_name=BTN_ICON,
        style={"background": "transparent", "border":"none"},
    )




def _palette_row(palette: Palette) -> rx.Component:
    return rx.box(
        rx.box(
            class_name=PALETTE_ROW_PREVIEW,
            style={"background": palette.preview_css},
        ),
        rx.box(
            rx.box(
                rx.text(palette.name, class_name=PALETTE_ROW_NAME),
                rx.text(palette.created_at, class_name=PALETTE_ROW_DATE),
                class_name="flex flex-col",
            ),
            rx.box(class_name="flex-1"),
            rx.box(
                icon_main(
                    "download",
                    title="Cargar paleta",
                    on_click=PaletteState.load_palette(palette.id)
                ),
                icon_main(
                    "pencil",
                    title="Editar nombre",
                    on_click=PaletteState.open_edit_dialog(palette.id)
                ),
                icon_main(
                    "trash-2",
                    title="Eliminar paleta",
                    on_click=PaletteState.delete_palette(palette.id)
                ),
                class_name=PALETTE_ROW_BTNS,
            ),
            class_name=PALETTE_ROW_INFO,
        ),
        class_name=PALETTE_ROW
    )



def _empty_list() -> rx.Component:
    return rx.box(
        rx.icon("bookmark", size=40, class_name=EMPTY_STATE_ICON),
        rx.text("Sin paletas guardadas", class_name=EMPTY_STATE_TEXT),
        rx.text("Guarda tu primera paleta", class_name=EMPTY_STATE_SUBTEXT),
        class_name=EMPTY_STATE
    )


def saved_palettes() -> rx.Component:
    return rx.box(
        rx.text("Guardadas", class_name=PALETTES_TITLE),
        rx.text(
            PaletteState.saved_palettes.length().to_string() + " paletas",
        ),
        rx.cond(
            PaletteState.saved_palettes.length() == 0,
            _empty_list(),
            rx.box(
                rx.foreach(PaletteState.saved_palettes, _palette_row),
                class_name=PALETTES_LIST,
            ),
        ),
        class_name=CARD_SCROLLABLE
    )