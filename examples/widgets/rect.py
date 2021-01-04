from pggui import Window
from pggui.widgets import Rect
from pggui.utils import Vec2, Color

window = Window(Vec2(200, 200), debug=True)
window.add_widget(Rect(Vec2(10, 10), Vec2(120, 180), Color.from_name("WHITE")))
window.add_widget(Rect(Vec2(10, 10), Vec2(20, 124), Color.from_name("ORANGE")))
window.add_widget(Rect(Vec2(100, 32), Vec2(50, 100), Color.from_name("RED")))
window.run()