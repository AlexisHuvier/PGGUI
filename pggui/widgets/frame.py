from pggui.widgets.widget import Widget
from pggui.utils import Color, Vec2

import pygame


class Frame(Widget):
    def __init__(self, position, size = Vec2(200, 150), color=None):
        """
            Create Frame Widget

            Parameters
            ----------
            position: Vec2
                Position of Frame
            size: Vec2
                Size of Frame
            color: Color or None
                Background Color of Frame (or None)
        """
        super().__init__(position)
        self.size = size
        self.color = color
        self.childrens = []
        self.render = None
        self.update_render()
    
    def add_widget(self, widget):
        """
            Add Widget to Frame

            Parameters
            ----------
            widget: Widget
                Widget will be added
        """
        widget.parent = self
        self.childrens.append(widget)

    def update_render(self):
        """
            Update Render of Frame

            .. warning:: You must use this method after change color bakground or size in Image
        """
        self.render = pygame.Surface(self.size.coords())
        if self.color is not None:
            self.render.fill(self.color.get_rgba())
    
    
    def display(self, screen):
        """
            Display Image Widget

            .. warning:: Don't use this function manually.
        """
        if self.displayed:
            screen.blit(self.render, self.position.coords())
            for i in self.childrens:
                i.display(self.render)