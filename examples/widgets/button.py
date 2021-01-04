from pggui import Window
from pggui.widgets import Button
from pggui.utils import Vec2, Color, Font

import os

def click():
    print("clicked")

window = Window(Vec2(230, 110), debug=True)
file = os.path.join(os.path.dirname(__file__), "image.png")
window.add_widget(Button(Vec2(10, 10), "Click 1", click))
window.add_widget(Button(Vec2(120, 10), "Click 2", click, Font(size=20)))
window.add_widget(Button(Vec2(10, 60), "Click 3", click, background=Color.from_name("RED")))
window.add_widget(Button(Vec2(120, 60), "Click 4", click, background=file))
window.run()