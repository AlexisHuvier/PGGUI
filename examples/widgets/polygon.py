from pggui import Window
from pggui.widgets import Polygon
from pggui.utils import Vec2, Color

window = Window(Vec2(200, 200), debug=True)
window.add_widget(Polygon((Vec2(30, 30), Vec2(30, 40), Vec2(40, 30))))
window.add_widget(Polygon((Vec2(40, 60), Vec2(60, 60), Vec2(60, 40)), Color.from_name("RED")))
window.add_widget(Polygon((Vec2(100, 60), Vec2(100, 100), Vec2(60, 100), Vec2(120, 154)), Color.from_name("RED"), 5))
window.run()