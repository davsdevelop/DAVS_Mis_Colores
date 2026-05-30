import reflex as rx
import sqlmodel

class Palette(rx.Model, table=True):
    name: str = sqlmodel.Field(default="Mi Paleta")
    created_at: str = sqlmodel.Field(default="")
    colors_json: str = sqlmodel.Field(default="[]")
    preview_css: str = sqlmodel.Field(default="linear-gradient(to right, #ccc, #999)")
