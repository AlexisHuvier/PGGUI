from pggui.widgets.widget import Widget
from pggui.utils import Color, clamp, Font

import pygame


class Selector(Widget):
    def __init__(self, position, *texts, font=Font(), color=Color.from_name("GRAY").darker(5)):
        """
            Create Selector Widget

            Parameters
            ----------
            position: Vec2
                Position of Selector
            texts: List of str
                Texts will be selected
            font: Font
                Font of Selector
            color: Color
                Color of Buttons
            
            .. warning:: You must give one text minimum.
        """
        super().__init__(position)
        self.texts = texts
        self.font = font
        self.color = color
        self.current = 0

        self.render_pred = None
        self.render_next = None
        self.max_size_text = None
        self.render = None
        self.update_size()
        self.update_render()
    
    def update_size(self):
        """
            Update size of Selector

            .. warning:: You must use this method after change list of texts of Selector
        """
        self.max_size_text = max([self.font.rendered_size(i).x for i in self.texts])

    def update_render(self):
        """
            Update Render of Button

            .. warning:: You must use this method after any change in Button
        """
        self.render_pred = pygame.Surface((25, 25), pygame.SRCALPHA, 32).convert_alpha()
        self.render_pred.fill(self.color.get_rgba())
        text_render = self.font.render("<")
        x = 25 / 2 - text_render.get_width() / 2
        y = 25 / 2 - text_render.get_height() / 2
        self.render_pred.blit(text_render, (x, y))

        self.render_next = pygame.Surface((25, 25), pygame.SRCALPHA, 32).convert_alpha()
        self.render_next.fill(self.color.get_rgba())
        text_render = self.font.render(">")
        x = 25 / 2 - text_render.get_rect().width / 2
        y = 25 / 2 - text_render.get_rect().height / 2
        self.render_next.blit(text_render, (x, y))

        text_render = self.font.render(self.texts[self.current])

        self.render = pygame.Surface((25 + 5 + self.max_size_text + 5 + 25, 25), pygame.SRCALPHA, 32).convert_alpha()
        self.render.blit(self.render_pred, (0, 0))
        self.render.blit(text_render, (25 + 5 + self.max_size_text / 2 - text_render.get_rect().width / 2,
                                       25 / 2 - text_render.get_rect().height / 2))
        self.render.blit(self.render_next, (25 + 5 + self.max_size_text + 5, 0))
        
    def display(self, screen):
        """
            Display Button Widget

            .. warning:: Don't use this function manually.
        """
        if self.displayed:
            screen.blit(self.render, self.position.coords())

    def event(self, evt):
        """
            Manage Pygame Event

            .. warning:: Don't use this function manually.
        """
        if self.displayed :
            if evt.type == pygame.MOUSEBUTTONDOWN and evt.button == pygame.BUTTON_LEFT:
                if self.render_pred.get_rect(x=self.get_absolute_position().x, y=self.get_absolute_position().y).collidepoint(*evt.pos):
                    if self.current == 0:
                        self.current = len(self.texts) - 1
                    else:
                        self.current -= 1
                    self.update_render()
                elif self.render_next.get_rect(x=self.get_absolute_position().x + 40 + self.max_size_text, y=self.get_absolute_position().y).collidepoint(*evt.pos):
                    if self.current == len(self.texts) - 1:
                        self.current = 0
                    else:
                        self.current += 1
                    self.update_render()