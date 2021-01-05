from pggui import Window
from pggui.widgets import ProgressBar
from pggui.utils import Vec2, Color, Font

from random import randint


window = Window(Vec2(220, 100), debug=True)
window.add_widget(ProgressBar(Vec2(10, 10)))
window.add_widget(ProgressBar(Vec2(10, 30), value=randint(10, 90)))
window.add_widget(ProgressBar(Vec2(10, 50), Vec2(200, 20), value=randint(10, 90)))
window.add_widget(ProgressBar(Vec2(10, 80), color=Color.from_name("RED"), value=randint(10, 90)))
window.run()