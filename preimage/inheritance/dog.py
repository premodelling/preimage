import preimage.inheritance.animal as animal


class Dog(animal.Animal):
    noise = 'woof'

    def __init__(self, owner, name, breed):
        super(Dog, self).__init__(owner=owner, name=name)
        self.breed = breed
