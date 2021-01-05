from pggui import Window
from pggui.widgets import Checkbox
from pggui.utils import Vec2, Color, Font

window = Window(Vec2(60, 150), debug=True)
window.add_widget(Checkbox(Vec2(10, 10), "Check 1"))
window.add_widget(Checkbox(Vec2(10, 40), "Check 2", font=Font(size=20)))
window.add_widget(Checkbox(Vec2(10, 70), "Check 3", checked=True))
window.add_widget(Checkbox(Vec2(10, 100), "Check 4", scale=2))
window.run()