from nicegui import ui
@ui.page('/')
def gallery_page():
    ui.dark_mode(True)

ui.run()