import reflex as rx

from main.state.palette_state import PaletteState
from .color_card import color_card_with_remove
from .styles import (CARD, BTN_GHOST, BTN_PRIMARY, BTN_SUCCESS, EDITOR_HEADER, EDITOR_SUBTITLE, EDITOR_TITLE, DIALOG_ACTIONS, DIALOG_CONTENT, DIALOG_DESC, DIALOG_INNER, DIALOG_INPUT, DIALOG_TITLE)


def _save_dialog() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.content(
            rx.box(
                rx.text("Guardar paleta", class_name=DIALOG_TITLE),
                rx.text("Pon un nombre a tu paleta de colores", class_name=DIALOG_DESC),
                rx.input(
                    placeholder="Nombre de la paleta...",
                    value=PaletteState.palette_name_input,
                    on_change=PaletteState.set_palette_name_input,
                    class_name=DIALOG_INPUT,
                    auto_focus=True
                ),
                rx.box(
                    rx.dialog.close(
                        rx.button(
                            "Cancelar",
                            on_click=PaletteState.close_save_dialog(),
                            class_name=BTN_GHOST,
                        ),
                    ),
                    rx.button(
                        "Guardar",
                        on_click=PaletteState.save_palette(),
                        class_name=BTN_PRIMARY,
                    ),
                    class_name=DIALOG_ACTIONS
                ),
                class_name=DIALOG_INNER,
            ),
            class_name=DIALOG_CONTENT
        ),
        open=PaletteState.show_save_dialog
    )


def _edit_dialog() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.content(
            rx.box(
                rx.text("Editar paleta", class_name=DIALOG_TITLE),
                rx.text("Actualiza el nombre de tu paleta de colores", class_name=DIALOG_DESC),
                rx.input(
                    placeholder="Nuevo nombre de la paleta...",
                    value=PaletteState.edit_palette_name_input,
                    on_change=PaletteState.set_edit_palette_name_input,
                    class_name=DIALOG_INPUT,
                    auto_focus=True
                ),
                rx.box(
                    rx.dialog.close(
                        rx.button(
                            "Cancelar",
                            on_click=PaletteState.close_edit_dialog(),
                            class_name=BTN_GHOST,
                        ),
                    ),
                    rx.button(
                        "Editar",
                        on_click=PaletteState.update_palette,
                        class_name=BTN_PRIMARY,
                    ),
                    class_name=DIALOG_ACTIONS
                ),
                class_name=DIALOG_INNER,
            ),
            class_name=DIALOG_CONTENT
        ),
        open=PaletteState.show_edit_dialog
    )




def palette_editor() -> rx.Component:
    return rx.box(
        # Ventanas modales del guardar y editar
        _save_dialog(),
        _edit_dialog(),
        rx.box(
            rx.box(
                rx.text("Paleta actual", class_name=EDITOR_TITLE),
                rx.text(
                    PaletteState.color_count.to_string() + " colores",
                    class_name=EDITOR_SUBTITLE,
                ),
                class_name="flex flex-col",
            ),
            rx.box(class_name="flex-1"),
            rx.box(
                rx.button(
                    rx.icon("shuffle", size=16),
                    "Aleatoria",
                    on_click=PaletteState.generate_random_palette(),
                    class_name=BTN_GHOST,
                ),
                rx.button(
                    rx.icon("plus", size=16),
                    "Agregar",
                    on_click=PaletteState.add_color(),
                    class_name=BTN_SUCCESS,
                ),
                class_name="flex items-center gap-2",
            ),
            class_name=EDITOR_HEADER,
        ),
        rx.box(
            rx.grid(
                rx.foreach(
                    PaletteState.current_colors,
                    lambda color, i: color_card_with_remove(color, i),
                ),
                columns="5",
                spacing="3",
                width="100%",
            ),
        ),
        class_name=CARD
    )