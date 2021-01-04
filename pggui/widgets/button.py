import pygame

from pggui.widgets.widget import Widget
from pggui.utils import Font, Color, clamp, Vec2


class Button(Widget):
    def __init__(self, position, text="", command=None, font=Font(), size=Vec2(100, 40), background=Color.from_name("GRAY").darker(5)):
        """
            Create Button Widget

            :param position: Position of Button
            :param text: Text of Button
            :param command: Click callback of Button
            :param font: Font of Button
            :param size: Size of Button
            :param background: Background of Button
            :type position: Vec2
            :type text: str
            :type command: Function
            :type font: Font
            :type size: Vec2
            :type background: Color or str
        """
        super().__init__(position)
        self.text = text
        self.command = command
        self.font = font
        self.background = background
        self.size = size
        self.is_hover = False
        self.update_render()

    def update_render(self):
        """
            Update Render of Button

            .. note:: You must use this method after any change in Button
        """
        if isinstance(self.background, Color):
            self.render = pygame.Surface(self.size.coords(), pygame.SRCALPHA, 32).convert_alpha()
            self.render.fill(self.background.get_rgba())
        else:
            self.render = pygame.image.load(self.background).convert()
            self.render = pygame.transform.scale(self.render, self.size.coords())
        
        text_render = self.font.render(self.text)
        x = self.size.x - self.render.get_rect().width / 2 - text_render.get_rect().width / 2
        y = self.size.y - self.render.get_rect().height / 2 - text_render.get_rect().height / 2
        self.render.blit(text_render, (x, y))
        
    def display(self, screen):
        """
            Display Button Widget

            .. note:: Don't use this function manually.
        """
        if self.displayed:
            screen.blit(self.render, self.position.coords())

    def event(self, evt):
        """
            Manage Pygame Event

            .. note:: Don't use this function manually.
        """
        if self.displayed and self.command is not None:
            if evt.type == pygame.MOUSEBUTTONDOWN and evt.button == pygame.BUTTON_LEFT:
                if self.render.get_rect(x=self.get_absolute_position().x, y=self.get_absolute_position().y).collidepoint(*evt.pos):
                    self.command()