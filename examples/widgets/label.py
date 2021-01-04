from pggui import Window
from pggui.widgets import Label
from pggui.utils import Vec2, Color, Font

window = Window(Vec2(400, 400), debug=True)
window.add_widget(Label(Vec2(20, 30), "On y crois tous."))
window.add_widget(Label(Vec2(20, 50), "On y crois tous.", Font(size=20)))
window.add_widget(Label(Vec2(20, 80), "On y crois tous.", Font(size=20), Color.from_name("RED")))
window.add_widget(Label(Vec2(20, 110), "On y crois tous.\nOU PAS !", Font(size=20), Color.from_name("RED"), 0))
window.add_widget(Label(Vec2(20, 200), "On y crois pas tous.\nOU PAS PAS !", Font(size=20), Color.from_name("RED"), 10))
window.run()