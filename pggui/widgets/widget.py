from pggui.utils import Vec2

class Widget:
    def __init__(self, position):
        """
            Create empty Widget

            Parameters
            ----------
            position: Vec2
                Position of Widget

            .. note:: You should not use this class without inheritance
        """
        self.position = position
        self.displayed = True
        self.parent = None

    def get_absolute_position(self):
        """
            Get Absolute Position

            Returns
            -------
            Vec2
                Absolute Position
        """
        if self.parent is None:
            return self.position
        else:
            return self.parent.get_absolute_position() + self.position
    
    def update(self):
        """
            Update Widget

            .. warning:: Don't use this function manually.
        """
        pass

    def event(self, evt):
        """
            Manage Pygame Event

            .. warning:: Don't use this function manually.
        """
        pass
    
    def display(self, screen):
        """
            Display Widget

            .. warning:: Don't use this function manually.
        """
        pass