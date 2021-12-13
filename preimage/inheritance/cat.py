import preimage.inheritance.animal as animal


class Cat(animal.Animal):

    noise = 'meow'

    def __init__(self, owner, name, breed):
        super(Cat, self).__init__(owner=owner, name=name)
        self.breed = breed
