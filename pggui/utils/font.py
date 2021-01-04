import pygame
from pggui.utils.color import Color
from pggui.utils.vec2 import Vec2

pygame.font.init()


class Font:
    def __init__(self, name="arial", size=15, bold=False, italic=False, underline=False,
                 color=Color.from_name("WHITE"), background=None, antialias=False):
        """
            Create Font

            :param name: Name of font or name of file of font
            :param size: Size of font
            :param bold: True if font is in bold or False
            :param italic: True if font is in italic or False
            :param underline: True if font is in italic or False
            :param color: Color of Font
            :param background: Color of background of Font or None
            :param antialias: True if font have antialias or False
            :type name: str
            :type size: int
            :type bold: bool
            :type italic: bool
            :type underline: bool
            :type color: Color
            :type background: Color
            :type antialias: bool
        """
        self.name = name
        self.size = size
        self.bold = bold
        self.italic = italic
        self.underline = underline
        self.color = color
        self.background = background
        self.antialias = antialias
        self.transformed_font = None
        self.update_font()

    def update_font(self):
        """
            Update font with modifiers

            .. note:: You must use this method after any change in font except for color, antialiase and background
        """
        try:
            font = pygame.font.Font(self.name, self.size)
        except FileNotFoundError:
            font = pygame.font.SysFont(self.name, self.size)
        font.set_underline(self.underline)
        font.set_italic(self.italic)
        font.set_bold(self.bold)
        self.transformed_font = font

    def rendered_size(self, text):
        """
            Return the rendered size of font with a text

            :param text: Text will be rendered
            :type text: str
            :return: Size of rendered text
            :rtype: Vec2
        """
        size = self.transformed_font.size(text)
        return Vec2(size[0], size[1])

    def render(self, text):
        """
            Make a render of a text

            :param text: Text to be rendered
            :type text: str
            :return: Final render
        """
        if self.background:
            return self.transformed_font.render(text, self.antialias, self.color.get_rgba(), self.background.get_rgba())
        else:
            return self.transformed_font.render(text, self.antialias, self.color.get_rgba())

    def __eq__(self, other):
        return (isinstance(other, Font) and self.name == other.name and self.color == other.color and
                self.background == other.background and self.bold == other.bold and self.italic == other.italic and
                self.underline == other.underline and self.antialias == other.antialias)