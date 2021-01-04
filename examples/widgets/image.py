from pggui import Window
from pggui.widgets import Image
from pggui.utils import Vec2, Color

import os

window = Window(Vec2(400, 400), debug=True)
file = os.path.join(os.path.dirname(__file__), "image.png")
window.add_widget(Image(Vec2(10, 10), file))
window.add_widget(Image(Vec2(250, 10), file, Vec2(100, 100), 127))
window.add_widget(Image(Vec2(10, 250), file, Vec2(100, 100), flipy=True))
window.add_widget(Image(Vec2(250, 250), file, Vec2(100, 100), flipx=True, flipy=True))
window.run()