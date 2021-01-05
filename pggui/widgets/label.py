import pygame

from pggui.widgets.widget import Widget
from pggui.utils import Font


class Label(Widget):
    def __init__(self, position, text, font=Font(), background=None, spacing_line=2):
        """
            Create Label Widget

            Parameters
            ----------
            position: Vec2
                Position of Label
            text: str
                Text of Label
            font: Font
                Font of Label
            background: Color or None
                Background of Label. Set to None to transparent background
            spacing_line: int
                Space between two lines
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

            .. warning:: You must use this method after changing Font or Text of Label
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

            .. warning:: Don't use this function manually.
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
    