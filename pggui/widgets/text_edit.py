import pygame

from pggui.widgets.widget import Widget
from pggui.widgets.label import Label
from pggui.utils import Font, clamp, Color, Vec2


class TextEdit(Widget):
    def __init__(self, position, size=Vec2(100, 100), font=Font(color=Color.from_name("BLACK")), accepted=None, image=None):
        """
            Create TextEdit Wiget

            Parameters
            ----------
            position: Vec2
                Position of TextEdit
            size: Vec2
                Size of TextEdit
            font: Font
                Font of Label of TextEdit
            accepted: str
                String of accepted characters
            image: str or None
                Path of Background image of TextEdit or None
        """
        super().__init__(position)

        self.size = size
        self.image = image
        self.label = Label(Vec2.zero(), "", font)
        self.text = ""
        self.focus = False
        self.accepted = accepted

        self.render = None
        self.update_render()
    
    def update_render(self):
        """
            Update Render of TextEdit

            .. warning:: You must use this method after any change in TextEdit
        """
        if self.label.text != self.text:
            self.label.text = self.text
            self.label.update_render()

        if self.image:
            self.render = pygame.image.load(self.image).convert()
            self.render = pygame.transform.scale(self.render, self.size.coords())
        else:
            self.render = pygame.Surface(self.size.coords(), pygame.SRCALPHA, 32).convert_alpha()
            self.render.fill((50, 50, 50))
            white = pygame.Surface((self.size - 8).coords())
            white.fill((255, 255, 255))
            self.render.blit(white, (4, 4))
    
    def event(self, evt):
        """
            Manage Pygame Event

            .. warning:: Don't use this function manually.
        """
        if self.displayed:
            if evt.type == pygame.KEYDOWN and self.focus:
                self.keypress(evt.key, evt.mod)
            elif evt.type == pygame.TEXTINPUT and self.focus:
                if self.accepted is None or evt.text in self.accepted:
                    self.text += evt.text
                    self.update_render()
            elif evt.type == pygame.MOUSEBUTTONDOWN and evt.button == pygame.BUTTON_LEFT:
                if self.render.get_rect(x=self.get_absolute_position().x, y= self.get_absolute_position().y).collidepoint(*evt.pos):
                    self.focus = True
                else:
                    self.focus = False
                    self.update_render()

    def keypress(self, key, mod):
        """
            Manage Pygame KeyPress Event

            .. warning:: Don't use this function manually.
        """
        mod -= 4096
        if key == pygame.K_BACKSPACE:
            if len(self.text):
                self.text = self.text[:-1]
                self.update_render()
        elif key == pygame.K_RETURN:
            self.text += "\n"
            self.update_render()
    
    def display(self, screen):
        """
            Display TextEdit Widget

            .. warning:: Don't use this function manually.
        """
        if self.displayed:
            render_rect = self.render.get_rect()
            sub = self.render.subsurface(render_rect.x + 5, render_rect.y + 5, render_rect.width - 10, render_rect.height - 10)
            self.label.display(sub)
            screen.blit(self.render, self.position.coords())