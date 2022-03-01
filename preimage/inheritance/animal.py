
class Animal:

    noise = ''

    def __init__(self, owner: str, name: str):
        """

        :param owner: the owner of the animal
        :param name: the name of the animal
        """

        self.owner = owner
        self.name = name

    def __repr__(self):
        """
        The __repr__ method is used to construct the text representation of an object. The default
        method produces text similar to <__main__.Dog at 0x7f72e5144670>, which isn't informative.

        :return: animal's name
        """

        return f'<{type(self).__name__}: {self.name}>'

    def make_noise(self, n: int = 1, volume: int = 0) -> str:
        """
        Make noise

        :param n: number of times
        :return: noise
        """

        text = self.noise * n

        if volume == 0:
            return ''
        elif volume == 1:
            return text
        elif volume == 2:
            return text.upper()
        else:
            raise ValueError('Unknown volume value.  The volume value must be 0, 1, or 2')


