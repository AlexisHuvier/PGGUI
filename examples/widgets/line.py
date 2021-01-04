from pggui import Window
from pggui.widgets import Line
from pggui.utils import Vec2, Color

window = Window(Vec2(200, 200), debug=True)
window.add_widget(Line(Vec2(10, 10), Vec2(120, 180), color=Color.from_name("WHITE")))
window.add_widget(Line(Vec2(10, 10), Vec2(2, 124), color=Color.from_name("ORANGE")))
window.add_widget(Line(Vec2(150, 32), Vec2(15, 184), 10, Color.from_name("RED")))
window.run()