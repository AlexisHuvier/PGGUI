import pygame

from pggui.widgets.widget import Widget
from pggui.utils import Color, Vec2


class Polygon(Widget):
    def __init__(self, positions, color=Color.from_name("BLACK"), width = 0):
        """
            Create Polygon Widget

            Parameters
            ----------
            position: List of Vec2
                Positions of Points of Polygon
            color: Color
                Color of Polygon
            width: int
                Width of Polygon (0 fill Polygon)
        """
        super().__init__(None)
        self.positions = positions
        self.color = color
        self.width = width
    
    def display(self, screen):
        """
            Display Polygon Widget

            .. warning:: Don't use this function manually.
        """
        if self.displayed:
            pygame.draw.polygon(screen, self.color.get_rgba(), tuple(i.coords() for i in self.positions), self.width)