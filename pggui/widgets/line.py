import pygame

from pggui.widgets.widget import Widget
from pggui.utils import Color, Vec2


class Line(Widget):
    def __init__(self, position, end=Vec2.zero(), width=2, color=Color.from_name("BLACK")):
        """
            Create Line Widget

            :param position: Position of Line
            :param end: End of Line
            :param width: Width of Line
            :param color: Color of Line
            :type position: Vec2
            :type end: Vec2
            :type width: int
            :type color: Color
        """
        super().__init__(position)
        self.end = end
        self.width = width
        self.color = color
    
    def display(self, screen):
        """
            Display Line Widget

            .. note:: Don't use this function manually.
        """
        if self.displayed:
            pygame.draw.line(screen, self.color.get_rgba(), self.position.coords(), self.end.coords(), self.width)
