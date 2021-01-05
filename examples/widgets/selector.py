from pggui import Window
from pggui.widgets import Selector
from pggui.utils import Vec2, Color, Font


window = Window(Vec2(150, 140), debug=True)
window.add_widget(Selector(Vec2(10, 10), "Ceci est", "un test"))
window.add_widget(Selector(Vec2(10, 50), "Ceci est", "un test", font=Font(size=20)))
window.add_widget(Selector(Vec2(10, 100), "Ceci est", "un test", color=Color.from_name("RED")))
window.run()