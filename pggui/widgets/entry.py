import pygame

from pggui.widgets.widget import Widget
from pggui.widgets.label import Label
from pggui.utils import Font, clamp, Color, Vec2


class Entry(Widget):
    def __init__(self, position, width=100, font=Font(color=Color.from_name("BLACK")), accepted=None, image=None):
        """
            Create Entry Wiget

            Parameters
            ----------
            position: Vec2
                Position of Entry
            width: int
                Width of Entry
            font: Font
                Font of Label of Entry
            accepted: sstr
                String of accepted characters
            image: str or None
                Background image of Entry (or None)
        """
        super().__init__(position)

        self.width = width
        self.image = image
        self.label = Label(Vec2.zero(), "", font)
        self.text = ""
        self.focus = False
        self.accepted = accepted

        self.render = None
        self.update_render()
    
    def update_render(self):
        """
            Update Render of Entry

            .. warning:: You must use this method after any change in Entry
        """
        if self.label.text != self.text:
            self.label.text = self.text
            text_size = self.label.font.rendered_size(self.text)
            self.label.position = Vec2(clamp(self.width - text_size.x - 10, maxi=0), self.render.get_rect().height/2 - text_size.y/2)
            self.label.update_render()

        if self.image:
            self.render = pygame.image.load(self.image).convert()
            self.render = pygame.transform.scale(self.render, (self.width, 35))
        else:
            self.render = pygame.Surface((self.width, 35), pygame.SRCALPHA, 32).convert_alpha()
            self.render.fill((50, 50, 50))
            white = pygame.Surface((self.width - 8, 27))
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
    
    def display(self, screen):
        """
            Display Entry Widget

            .. warning:: Don't use this function manually.
        """
        if self.displayed:
            render_rect = self.render.get_rect()
            sub = self.render.subsurface(render_rect.x + 5, render_rect.y, render_rect.width - 10, render_rect.height)
            self.label.display(sub)
            screen.blit(self.render, self.position.coords())