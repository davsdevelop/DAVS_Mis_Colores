import reflex as rx
from datetime import datetime
import json
import sqlmodel


from .color_state import ColorState
from main.model.palette import Palette


def _build_preview_css(colors: list[str]) -> str:
    if not colors:
        return "linear-gradient(to right, #ccc, #999)"
    colores = ", ".join(colors)
    return f"linear-gradient(to right, {colores})"



class PaletteState(ColorState):
    
    saved_palettes: list[Palette] = []
    show_save_dialog: bool = False
    show_edit_dialog: bool = False
    palette_name_input: str = ""
    edit_palette_id: int = -1
    edit_palette_name_input: str = ""


    # Guardar
    @rx.event
    def set_palette_name_input(self, value: str):
        self.palette_name_input = value

    
    @rx.event
    def open_save_dialog(self):
        self.palette_name_input = ""
        self.show_save_dialog = True

    @rx.event
    def close_save_dialog(self):
        self.show_save_dialog = False


    
    @rx.event
    def save_palette(self):

        name = self.palette_name_input.strip() or "Mi Paleta"
        colors = list(self.current_colors)
        preview = _build_preview_css(colors)
        now = datetime.now().strftime("%d/%m/%Y %H:%M")
        with rx.session() as session:
            palette = Palette(
                name=name,
                created_at=now,
                colors_json=json.dumps(colors),
                preview_css=preview,
            )
            session.add(palette)
            session.commit()
        
        self.show_save_dialog = False
        self.palette_name_input = ""
        return [
            type(self).load_saved_palettes(),
            rx.toast.success(f"Paleta {name} guardada", duration=3000),
        ]
    

    #CARGAR DATOS
    @rx.event
    def load_saved_palettes(self):
        with rx.session() as session:
            palettes = session.exec(sqlmodel.select(Palette)).all()
            self.saved_palettes = list(palettes)


    @rx.event
    def load_palette(self, palette_id: int):
        with rx.session() as session:
            palette = session.get(Palette, palette_id)
            if palette:
                self.current_colors = json.loads(palette.colors_json)
                self.active_palette_id = palette_id


    

    # EDITAR
    @rx.event
    def set_edit_palette_name_input(self, value: str):
        self.edit_palette_name_input = value

    @rx.event
    def open_edit_dialog(self, palette_id: int):
        with rx.session() as session:
            palette = session.get(Palette, palette_id)
            if palette:
                self.edit_palette_id = palette_id
                self.edit_palette_name_input = palette.name
                self.show_edit_dialog = True


    @rx.event
    def close_edit_dialog(self):
        self.show_edit_dialog = False
        self.edit_palette_id = -1


    @rx.event
    def update_palette(self):
        if self.edit_palette_id == -1:
            return
        new_name = self.edit_palette_name_input.strip() or "Mi Paleta Actualizada"
        with rx.session() as session:
            palette = session.get(Palette, self.edit_palette_id)
            if palette:
                palette.name = new_name
                session.add(palette)
                session.commit()
        
        self.show_edit_dialog = False
        self.edit_palette_id = -1
        return[
            type(self).load_saved_palettes(),
            rx.toast.info("Paleta actualizada", duration=3000)
        ]
    

    #ELIMINAR
    @rx.event
    def delete_palette(self, palette_id: int):
        with rx.session() as session:
            palette = session.get(Palette, palette_id)
            if palette:
                session.delete(palette)
                session.commit()

        if self.active_palette_id == palette_id:
            self.active_palette_id = -1

        return[
            type(self).load_saved_palettes(),
            rx.toast.error("Paleta eliminada", duration=3000),
        ]