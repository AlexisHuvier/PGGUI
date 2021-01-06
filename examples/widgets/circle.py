from pggui import Window
from pggui.widgets import Circle
from pggui.utils import Vec2, Color

window = Window(Vec2(200, 200), debug=True)
window.add_widget(Circle(Vec2(30, 30)))
window.add_widget(Circle(Vec2(80, 40), 30, Color.from_name("RED")))
window.add_widget(Circle(Vec2(30, 80), 20, Color.from_name("RED"), 3))
window.run()