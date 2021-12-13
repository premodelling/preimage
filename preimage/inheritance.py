import sys
import os


def inheritance():

    dog = preimage.inheritance.dog.Dog(owner='Lee Duncan', name='Rin Tin Tin', breed='German Shepherd')
    print(f'{dog}: {dog.make_noise(n=3, volume=1)}')

    cat = preimage.inheritance.cat.Cat(owner='Sabrina', name='Salem', breed='Moggie')
    print(cat)
    print(cat.make_noise(n=3, volume=2))


if __name__ == '__main__':
    root = os.getcwd()
    sys.path.append(root)

    import preimage.inheritance.dog
    import preimage.inheritance.cat

    inheritance()
