from pggui.widgets.widget import Widget
from pggui.utils import Vec2, Color

import pygame


class ProgressBar(Widget):
    def __init__(self, position, size=Vec2(150, 10), color=Color.from_name("GREEN"), value=0):
        """
            Create ProgressBar Widget

            Parameters
            ----------
            position: Vec2
                Position of ProgressBar
            size: Vec2
                Size of ProgressBar
            color: Color
                Color of ProgressBar
            value: int
                Current value of ProgressBar. Between 1 and 100.
        """
        super().__init__(position)
        self.size = size
        self.color = color
        self.value = value
        self.render = None
        self.update_render()
    
    def update_render(self):
        """
            Update Render of ProgressBar

            .. warning:: You must use this method after any change in ProgressBar
        """
        self.render = pygame.Surface(self.size.coords(), pygame.SRCALPHA, 32).convert_alpha()
        self.render.fill((50, 50, 50))
        white = pygame.Surface((self.size - 2).coords(), pygame.SRCALPHA, 32).convert_alpha()
        white.fill((255, 255, 255))
        self.render.blit(white, (1, 1))
        bar = pygame.Surface((int((self.size.x - 4) * (self.value / 100)), self.size.y - 4), pygame.SRCALPHA, 32).convert_alpha()
        bar.fill(self.color.get_rgba())
        self.render.blit(bar, (2, 2))
    
    def display(self, screen):
        """
            Display ProgressBar Widget

            .. warning:: Don't use this function manually.
        """
        if self.displayed:
            screen.blit(self.render, self.position.coords())
    
    