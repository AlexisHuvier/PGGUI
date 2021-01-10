from pggui import Window
from pggui.widgets import Frame, Label
from pggui.utils import Vec2, Color

window = Window(Vec2(310, 410), debug=True)
frame1 = Frame(Vec2(10, 10))
frame1.add_widget(Label(Vec2(10, 10), "Ceci est un test"))
frame2 = Frame(Vec2(10, 200), Vec2(100, 200))
frame2.add_widget(Label(Vec2(10, 10), "Ceci est un test"))
frame3 = Frame(Vec2(200, 200), Vec2(100, 200), Color.from_name("RED"))
frame3.add_widget(Label(Vec2(10, 10), "Ceci est un test"))
window.add_widget(frame1)
window.add_widget(frame2)
window.add_widget(frame3)
window.run()