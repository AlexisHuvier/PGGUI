import pygame

from pggui.widgets.widget import Widget
from pggui.utils import Color, Vec2


class Circle(Widget):
    def __init__(self, position, radius = 20, color=Color.from_name("BLACK"), width = 0):
        """
            Create Circle Widget

            Parameters
            ----------
            position: Vec2
                Position of Circle
            radius: int or float
                Radius of Circle
            color: Color
                Color of Circle
            width: int
                Width of Circle (0 fill Circle)
        """
        super().__init__(position)
        self.color = color
        self.radius = radius
        self.width = width
    
    def display(self, screen):
        """
            Display Circle Widget

            .. warning:: Don't use this function manually.
        """
        if self.displayed:
            pygame.draw.circle(screen, self.color.get_rgba(), self.position.coords(), self.radius, self.width)
