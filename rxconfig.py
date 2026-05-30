import reflex as rx

config = rx.Config(
    app_name="main",
    db_url="sqlite:///colors.db",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)