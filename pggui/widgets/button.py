import pygame

from pggui.widgets.widget import Widget
from pggui.utils import Font, Color, clamp, Vec2


class Button(Widget):
    def __init__(self, position, text="", command=None, font=Font(), size=Vec2(100, 40), background=Color.from_name("GRAY").darker(5)):
        """
            Create Button Widget

            Parameters
            ----------
            position: Vec2
                Position of Button
            text: str
                Text of Button
            command: Function or None
                Click callback of Button
            font: Font
                Font of Button
            size: Vec2
                Size of Button
            background: Color or str
                Background of Button. May be a Color or a path to a image
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

            .. warning:: You must use this method after any change in Button
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

            .. warning:: Don't use this function manually.
        """
        if self.displayed:
            screen.blit(self.render, self.position.coords())

    def event(self, evt):
        """
            Manage Pygame Event

            .. warning:: Don't use this function manually.
        """
        if self.displayed and self.command is not None:
            if evt.type == pygame.MOUSEBUTTONDOWN and evt.button == pygame.BUTTON_LEFT:
                if self.render.get_rect(x=self.get_absolute_position().x, y=self.get_absolute_position().y).collidepoint(*evt.pos):
                    self.command()