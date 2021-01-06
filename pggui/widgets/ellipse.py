import pygame

from pggui.widgets.widget import Widget
from pggui.utils import Color, Vec2


class Ellipse(Widget):
    def __init__(self, position, size=Vec2.zero(), color=Color.from_name("BLACK"), width=0):
        """
            Create Ellipse Widget

            Parameters
            ----------
            position: Vec2
                Position of Ellipse
            size: Vec2
                Size of Ellipse
            color: Color
                Color of Ellipse
            width: int
                Width of Ellipse (0 fill Ellipse)
        """
        super().__init__(position)
        self.size = size
        self.color = color
        self.width = width
    
    def display(self, screen):
        """
            Display Ellipse Widget

            .. warning:: Don't use this function manually.
        """
        if self.displayed:
            pygame.draw.ellipse(screen, self.color.get_rgba(), pygame.Rect(*self.position.coords(), *self.size.coords()), self.width)