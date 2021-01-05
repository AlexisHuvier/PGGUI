from pggui import Window
from pggui.widgets import TextEdit
from pggui.utils import Vec2, Color, Font

import os

window = Window(Vec2(170, 510), debug=True)
file = os.path.join(os.path.dirname(__file__), "image.png")
window.add_widget(TextEdit(Vec2(10, 10)))
window.add_widget(TextEdit(Vec2(10, 120), Vec2(150, 50)))
window.add_widget(TextEdit(Vec2(10, 180), font=Font(color=Color.from_name("RED"))))
window.add_widget(TextEdit(Vec2(10, 290), accepted="abc"))
window.add_widget(TextEdit(Vec2(10, 400), image=file))
window.run()