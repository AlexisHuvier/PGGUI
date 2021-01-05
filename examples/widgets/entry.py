from pggui import Window
from pggui.widgets import Entry
from pggui.utils import Vec2, Color, Font

import os

window = Window(Vec2(170, 260), debug=True)
file = os.path.join(os.path.dirname(__file__), "image.png")
window.add_widget(Entry(Vec2(10, 10)))
window.add_widget(Entry(Vec2(10, 60), 150))
window.add_widget(Entry(Vec2(10, 110), font=Font(color=Color.from_name("RED"))))
window.add_widget(Entry(Vec2(10, 160), accepted="abc"))
window.add_widget(Entry(Vec2(10, 210), image=file))
window.run()