import pygame
import pygame.locals as pgconst
import os

from pggui.utils import Color, Vec2, Font

pygame.init()


class Window:
    def __init__(self, size=Vec2(900, 700), color=Color.from_name("BLACK"), title="PGGUI", fps=60, centered=True, debug=False):
        """
            Create Window

            :param size: Size of Window
            :param color: Color of background of Window
            :param title: Title of Window
            :param fps: Max FPS of Window (None if you don't want limit)
            :param centered: True if you want centered window, else False
            :param debug: True if you want some debug infos, else False
            :type size: Vec2
            :type color: Color
            :type title: str
            :type fps: int
            :type centered: bool
            :type debug: bool
        """

        self.fps = fps
        self.debug = debug
        self.color = color
        self.size = size

        if centered:
            os.environ['SDL_VIDEO_CENTERED'] = '1'
        
        pygame.display.set_caption(title)
        self.screen = pygame.display.set_mode(size.coords())

        self.clock = pygame.time.Clock()
        self.is_running = False
        self.debug_font = Font(bold=True, color=Color.from_name("ORANGE"))
        self.keys_callback = {}

        self.widgets = []

    def set_key_callback(self, key, callback):
        self.keys_callback[key.value] = callback

    def add_widget(self, widget):
        """
            Add Widget to Window

            :param widget: Widget to be added
            :type widget: Widget
        """
        if widget.parent is None:
            self.widgets.append(widget)
    
    def stop(self):
        """
            Stop Window
        """
        self.is_running = False
    
    def run(self):
        """
            Launch Window
        """
        self.is_running = True
        while self.is_running:
            for event in pygame.event.get():
                self.process_event(event)

            for i in self.widgets:
                i.update()
            
            self.screen.fill(self.color.get_rgba())

            for i in self.widgets:
                i.display(self.screen)

            if self.debug:
                try:
                    fps_label = self.debug_font.render("FPS : " + str(round(self.clock.get_fps())))
                except OverflowError:
                    fps_label = self.debug_font.render("FPS : Infinity")
                self.screen.blit(fps_label, (10, 10))
            
            if self.fps is None:
                self.clock.tick()
            else:
                self.clock.tick(self.fps)
            pygame.display.update()
        pygame.quit()
                
    def process_event(self, evt):
        """
            Process pygame event

            :param evt: PyGame Event to be processed
            :type evt: Event

            .. note:: You may not use this method. Window make it for you.
        """
        if evt.type == pgconst.QUIT:
            self.stop()
        
        if evt.type == pgconst.KEYUP and evt.key in self.keys_callback:
            self.keys_callback[evt.key]()

        for i in self.widgets:
            i.event(evt)