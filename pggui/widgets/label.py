import pygame

from pggui.widgets.widget import Widget
from pggui.utils import Font


class Label(Widget):
    def __init__(self, position, text, font=Font(), background=None, spacing_line=2):
        """
            Create Label Widget

            :param position: Position of Label
            :param text: Text of Label
            :param font: Font of Label
            :param background: Background of Label (or None)
            :param spacing_line: Space between two line
            :type position: Vec2
            :type text: str
            :type font: Font
            :type background: Color
            :type spacing_line: int
        """
        super().__init__(position)
        self.text = text
        self.font = font
        self.background = background
        self.spacing_line = spacing_line
        self.update_render()
    
    def update_render(self):
        """
            Update Render of Label

            .. note:: You must use this method after changing Font or Text of Label
        """
        if "\n" in self.text:
            self.renders = [self.font.render(i) for i in self.text.split("\n")]
            self.single = False
        else:
            self.render = self.font.render(self.text)
            self.single = True

    def display(self, screen):
        """
            Display Label Widget

            .. note:: Don't use this function manually.
        """
        if self.displayed and len(self.text):
            if self.single:
                if self.background is not None:
                    screen.fill(self.background.get_rgba(), self.render.get_rect(x=self.position.x, y=self.position.y))
                screen.blit(self.render, self.position.coords())
            else:
                for i, render in enumerate(self.renders):
                    if len(self.text.split("\n")[i]):
                        if self.background is not None:
                            screen.fill(self.background.get_rgba(), render.get_rect(x=self.position.x, y=self.position.y+(self.spacing_line + render.get_rect().height)*i))
                        screen.blit(render, (self.position.x, self.position.y + (self.spacing_line + render.get_rect().height)*i))
    