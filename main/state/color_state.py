import reflex as rx
import random


def _random_hex() -> str:
    return f"#{random.randint(0,0xFFFFFF):06X}"


class ColorState(rx.State):
    current_colors: list[str] = ["#FF6B6B", "#FFD93D", "#6BCB77", "#4D96FF", "#C77DFF"]
    active_palette_id: int = -1


    @rx.var
    def color_count(self) -> int:
        return len(self.current_colors)
    

    @rx.var
    def can_remove_color(self) -> bool:
        return len(self.current_colors) > 3
    

    @rx.var
    def all_colors_text(self) -> str:
        return ", ".join(self.current_colors)
    


    @rx.event
    def generate_random_palette(self):
        self.current_colors = [_random_hex() for _ in range(5)]
        self.active_palette_id = -1


    @rx.event
    def add_color(self):
        self.current_colors = self.current_colors + [_random_hex()]

    
    @rx.event
    def remove_color(self, index:int):
        if len(self.current_colors) > 3:
            colors = list(self.current_colors)
            colors.pop(index)
            self.current_colors = colors


    @rx.event
    def notify_copied_all(self):
        return rx.toast.success(f"Copiados: {self.all_colors_text}", duration=3000)