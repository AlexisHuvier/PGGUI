from pggui import Window
from pggui.utils import Color, Vec2


window = Window(Vec2(550, 300), Color.from_name("WHITE"), "TESTING PGGUI", 50, debug = True)
window.run()