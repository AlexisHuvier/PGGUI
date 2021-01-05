from pggui.utils.utils import clamp


class Color:
    def __init__(self):
        """
            Initialize Color object with all parameters to 0

            .. note:: You may not use this constructor. Use "from" classmethod.
        """
        self.r = 0
        self.g = 0
        self.b = 0
        self.a = 255

    def darker(self, force=1):
        """
            Create darker color object with a force multiplier

            Parameters
            ----------
            force: int
                Force multiplier
            
            Returns
            -------
            Color
                Color object
        """
        nb = clamp(force, 1)
        rgb = (clamp(x - 10*nb, 0, 255) for x in self.get_rgb())
        return Color.from_rgba(*rgb, self.a)

    def lighter(self, force=1):
        """
            Create lighter color object with a force multiplier

            Parameters
            ----------
            force: int
                Force multiplier
            
            Returns
            -------
            Color
                Color object
        """
        nb = clamp(force, 1)
        rgb = (clamp(x + 10*nb, 0, 255) for x in self.get_rgb())
        return Color.from_rgba(*rgb, self.a)

    def get_rgb(self):
        """
            Return tuple with rgb values

            Returns
            -------
            Tuple(int, int, int)
                Tuple with rgb values
        """
        return self.r, self.g, self.b

    def get_rgba(self):
        """
            Return tuple with rgba values

            Returns
            -------
            Tuple(int, int, int, int)
                Tuple with rgba values
        """
        return self.r, self.g, self.b, self.a

    def get_html(self):
        """
            Return html color format for Color object

            Returns
            -------
            str
                html color
        """
        return ("#"+hex(self.r)[2:]+hex(self.g)[2:]+hex(self.b)[2:]+hex(self.a)[2:]).upper()

    def __repr__(self):
        """
            Represents Color Object

            Returns
            -------
            str
                RGBA Values convert in string
        """
        return str(self.get_rgba())

    @classmethod
    def from_rgb(cls, r, g, b):
        """
            Create Color object from rgb values

            Parameters
            ----------
            r: int
                Red Value
            b: int
                Blue Value
            g: int
                Green Value

            Returns
            -------
            Color
                Color Object
        """
        color = Color()
        color.r = r
        color.g = g
        color.b = b
        return color

    @classmethod
    def from_rgba(cls, r, g, b, a):
        """
            Create Color object from rgba values

            Parameters
            ----------
            r: int
                Red Value
            b: int
                Blue Value
            g: int
                Green Value
            a: int
                Alpha Value

            Returns
            -------
            Color
                Color Object
        """
        color = Color.from_rgb(r, g, b)
        color.a = a
        return color

    @classmethod
    def from_color(cls, color):
        """
            Create Color object from anthor color object

            Parameters
            ----------
            color: Color
                Basic Color

            Returns
            -------
            Color
                Color Object
        """
        return Color.from_rgba(*color.get_rgba())

    @classmethod
    def from_html(cls, html):
        """
            Create Color object from html color format

            Parameters
            ----------
            html: str
                HTML formatted Color

            Returns
            -------
            Color
                Color Object
        """
        if len(html) == 7 or len(html) == 9:
            if len(html) == 7:
                html += "FF"
            return Color.from_rgba(*(int(html[1:3], 16), int(html[3:5], 16), int(html[5:7], 16), int(html[7:9], 16)))
        else:
            raise ValueError("Hexa must be a 7 or 9 lenght string (#RRGGBBAA)")

    @classmethod
    def from_name(cls, name):
        """
            Create Color object from name
            
            Parameters
            ----------
            name: str
                Name of Color

            Returns
            -------
            Color
                Color Object
                
            .. note:: List of colors known : WHITE, BLACK, GRAY, RED, GREEN, BLUE, FUCHSIA, YELLOW, CYAN, LIME, BROWN, NAVY_BLUE, OLIVE, PURPLE, TEAL, SILVER, ORANGE
        """
        colors = {
            "WHITE": (255, 255, 255),
            "BLACK": (0, 0, 0),
            "GRAY": (128, 128, 128),
            "RED": (255, 0, 0),
            "GREEN": (0, 255, 0),
            "BLUE": (0, 0, 255),
            "FUCHSIA": (255, 0, 255),
            "YELLOW": (255, 255, 0),
            "CYAN": (0, 255, 255),
            "LIME": (0, 128, 0),
            "BROWN": (128, 0, 0),
            "NAVY_BLUE": (0, 0, 128),
            "OLIVE": (128, 128, 0),
            "PURPLE": (128, 0, 128),
            "TEAL": (0, 128, 128),
            "SILVER": (192, 192, 192),
            "ORANGE": (255, 128, 0)
        }
        return Color.from_rgb(*colors[name.upper()])