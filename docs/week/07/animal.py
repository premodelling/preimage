class Animal():
    noise = ""
    def __init__(self, owner, name):
        self.owner = owner
        self.name = name
    def make_noise(self):
        """ make the noise """
        return self.noise

class Dog(Animal):
    noise = "woof"
    def __init__(self, owner, name, breed):
        super().__init__(owner, name)
        self.breed = breed

d = Dog(owner="Lee Duncan",name="Rin Tin Tin",
        breed="German Shepherd")
print(d)
print(d.make_noise())
