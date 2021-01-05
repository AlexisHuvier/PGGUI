from pggui import Window
from pggui.utils import Keys


window = Window(debug=True)
window.set_key_callback(Keys.K_ESCAPE, window.stop)
window.run()