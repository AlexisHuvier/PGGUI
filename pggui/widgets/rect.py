import pygame

from pggui.widgets.widget import Widget
from pggui.utils import Color, Vec2


class Rect(Widget):
    def __init__(self, position, size=Vec2.zero(), color=Color.from_name("BLACK")):
        """
            Create Rect Widget

            Parameters
            ----------
            position: Vec2
                Position of Rect
            size: Vec2
                Size of Rect
            color: Color
                Color of Rect
        """
        super().__init__(position)
        self.size = size
        self.color = color
    
    def display(self, screen):
        """
            Display Rect Widget

            .. warning:: Don't use this function manually.
        """
        if self.displayed:
            pygame.draw.rect(screen, self.color.get_rgba(), pygame.Rect(*self.position.coords(), *self.size.coords()))
