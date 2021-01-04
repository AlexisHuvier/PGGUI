import pygame

from pggui.widgets.widget import Widget
from pggui.utils import Color, Vec2


class Rect(Widget):
    def __init__(self, position, length=Vec2.zero(), color=Color.from_name("BLACK")):
        """
            Create Rect Widget

            :param position: Position of Rect
            :param length: Length of Rect
            :param width: Width of Rect
            :param color: Color of Rect
            :type position: Vec2
            :type length: Vec2
            :type width: int
            :type color: Color
        """
        super().__init__(position)
        self.length = length
        self.color = color
    
    def display(self, screen):
        """
            Display Rect Widget

            .. note:: Don't use this function manually.
        """
        if self.displayed:
            pygame.draw.rect(screen, self.color.get_rgba(), pygame.Rect(*self.position.coords(), *self.length.coords()))
