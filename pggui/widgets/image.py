import pygame

from pggui.widgets.widget import Widget
from pggui.utils import Vec2

class Image(Widget):
    def __init__(self, position, sprite, size=None, rotation=0, flipx=False, flipy=False):
        """
            Create Image Widget

            :param position: Position of Image
            :param sprite: Sprite of Image
            :param size: Size of Image (or None)
            :param rotation: Rotation of Image
            :param flipx: True if Image is flip on X or False
            :param flipy: True if Image is flip on Y or False
            :type position: Vec2
            :type sprite: str
            :type size: Vec2
            :type rotation: int
            :type flipx: bool
            :type flipy: bool
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

            .. note:: You must use this method after any change in Image
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

            .. note:: Don't use this function manually.
        """
        if self.displayed:
            screen.blit(self.render, self.position.coords())