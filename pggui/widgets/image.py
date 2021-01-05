import pygame

from pggui.widgets.widget import Widget
from pggui.utils import Vec2

class Image(Widget):
    def __init__(self, position, sprite, size=None, rotation=0, flipx=False, flipy=False):
        """
            Create Image Widget

            Parameters
            ----------
            position: Vec2
                Position of Image
            sprite: str
                Path of sprite of Image
            size: Vec2 or None
                Size of Image. Set to None to use original size
            rotation: int
                Rotation of Image (in degrees)
            flipx: bool
                True if Image is flip on X or False
            flipy: bool
                True if Image is flip on Y or False
        """
        super().__init__(position)
        self.sprite = sprite
        self.size = size
        self.rotation = rotation
        self.flipx = flipx
        self.flipy = flipy

        self.render = None
        self.update_render()
    
    def update_render(self):
        """
            Update Render of Image

            .. warning:: You must use this method after any change in Image
        """
        self.render = pygame.image.load(self.sprite).convert()
        if self.size is not None:
            self.render = pygame.transform.scale(self.render, self.size.coords())
        if self.rotation != 0:
            self.render = pygame.transform.rotate(self.render, self.rotation)
        if self.flipx or self.flipy:
            self.render = pygame.transform.flip(self.render, self.flipx, self.flipy)
    
    def display(self, screen):
        """
            Display Image Widget

            .. warning:: Don't use this function manually.
        """
        if self.displayed:
            screen.blit(self.render, self.position.coords())