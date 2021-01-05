from pggui.widgets.widget import Widget
from pggui.utils import Font

import pygame


class Checkbox(Widget):
    def __init__(self, position, text="", font=Font(), checked=False, scale=1):
        """
            Create Checkbox Widget

            :param position: Position of Checkbox
            :param text: Text of Checkbox
            :param font: Font of Checkbox
            :param checked: True if Checkbox is checked or False
            :param scale: Scale of Checkbox
            :type position: Vec2
            :type text: str
            :type font: Font
            :type checked: bool
            :type scale: float
        """
        super().__init__(position)
        self.text = text
        self.font = font
        self.checked = checked
        self.scale = scale

        self.render = None
        self.render_btn = None
        self.update_render()

    def update_render(self):
        """
            Update Render of Checkbox

            .. note:: You must use this method after any change in Checkbox
        """
        self.render_btn = pygame.Surface((20*self.scale, 20*self.scale))
        self.render_btn.fill((50, 50, 50))
        self.render_btn.fill((255, 255, 255), pygame.Rect(2*self.scale, 2*self.scale, 16*self.scale, 16*self.scale))
        if self.checked:
            self.render_btn.fill((0, 0, 0), pygame.Rect(3*self.scale, 3*self.scale, 14*self.scale, 14*self.scale))

        render_label = self.font.render(self.text)
        self.render = pygame.Surface((20*self.scale + 5 + render_label.get_width(), 20*self.scale), pygame.SRCALPHA, 32).convert_alpha()
        self.render.blit(self.render_btn, (0, 0))
        self.render.blit(render_label, (20*self.scale + 5, 10*self.scale - render_label.get_height() / 2))
        
    def display(self, screen):
        """
            Display Checkbox Widget

            .. note:: Don't use this function manually.
        """
        if self.displayed:
            screen.blit(self.render, self.position.coords())

    def event(self, evt):
        """
            Manage Pygame Event

            .. note:: Don't use this function manually.
        """
        if self.displayed:
            if evt.type == pygame.MOUSEBUTTONDOWN and evt.button == pygame.BUTTON_LEFT:
                if self.render_btn.get_rect(x=self.get_absolute_position().x, y=self.get_absolute_position().y).collidepoint(*evt.pos):
                    self.checked = not self.checked
                    self.update_render()