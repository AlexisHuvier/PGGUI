from pggui.utils import Vec2

class Widget:
    def __init__(self, position = Vec2.zero()):
        """
            Create empty Widget

            :param position: Position of Widget
            :type position: Vec2

            .. note:: You should not use this class without inheritance
        """
        self.position = position
        self.displayed = True
        self.parent = None

    def get_absolute_position(self):
        """
            Get Absolute Position

            :return: Absolute Position
            :rtype: Vec2
        """
        if self.parent is None:
            return self.position
        else:
            return self.parent.get_absolute_position() + self.position
    
    def update(self):
        """
            Update Widget

            .. note:: Don't use this function manually.
        """
        pass

    def event(self, evt):
        """
            Manage Pygame Event

            .. note:: Don't use this function manually.
        """
        pass
    
    def display(self, screen):
        """
            Display Widget

            .. note:: Don't use this function manually.
        """
        pass