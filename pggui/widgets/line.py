import pygame

from pggui.widgets.widget import Widget
from pggui.utils import Color, Vec2


class Line(Widget):
    def __init__(self, position, end=Vec2.zero(), width=2, color=Color.from_name("BLACK")):
        """
            Create Line Widget

            Parameters
            ----------
            position: Vec2
                Position of Line
            end: Vec2
                End of Line
            width: int
                Width of Line
            color: Color
                Color of Line
        """
        super().__init__(position)
        self.end = end
        self.width = width
        self.color = color
    
    def display(self, screen):
        """
            Display Line Widget

            .. warning:: Don't use this function manually.
        """
        if self.displayed:
            pygame.draw.line(screen, self.color.get_rgba(), self.position.coords(), self.end.coords(), self.width)
