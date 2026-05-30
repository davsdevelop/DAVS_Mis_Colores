import reflex as rx

from main.state.palette_state import PaletteState
from .styles import (COLOR_CARD, COLOR_CARD_ACTIONS, COLOR_CARD_BTN, COLOR_CARD_FOOTER, COLOR_CARD_HEX_CHIP, COLOR_CARD_HEX_TEXT, COLOR_CARD_REMOVE_BTN, COLOR_CARD_WRAPPER)


def _color_card(color: str, index: int) -> rx.Component:
    return rx.box(
        rx.box(
            rx.box(
                rx.text(
                    color,
                    class_name=COLOR_CARD_HEX_TEXT,
                ),
                class_name=COLOR_CARD_HEX_CHIP,
            ),
            #icono
            rx.box(
                rx.icon_button(
                    rx.icon("copy", size=24),
                    on_click=[rx.set_clipboard(color), rx.toast.success("Color copiado...")],
                    variant="ghost",
                    class_name=COLOR_CARD_BTN,
                ),
                class_name=COLOR_CARD_ACTIONS,
            ),
            class_name=COLOR_CARD_FOOTER,
        ),
        class_name=COLOR_CARD,
        style={"background_color": color}
    )


def color_card_with_remove(color: str, index: int) -> rx.Component:
    return rx.box(
        _color_card(color, index),
        rx.cond(
            PaletteState.can_remove_color,
            rx.button(
                rx.icon("x", size=12),
                "Eliminar",
                on_click=PaletteState.remove_color(index),
                class_name=COLOR_CARD_REMOVE_BTN,
            ),
            rx.box(height="28px")
        ),
        class_name=COLOR_CARD_WRAPPER
    )

