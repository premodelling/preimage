"""
The main module
"""

import sys
import os


def structure():

    # dict
    emily = dictionaries.new_student(name='Emily Bronte')
    print(emily)
    dictionaries.add_grade(record=emily, course='Physics', grade=89)
    dictionaries.add_grade(record=emily, course='Anthropology', grade=91)
    print(emily)


if __name__ == '__main__':
    root = os.getcwd()
    sys.path.append(root)

    import preimage.grades.dictionaries

    dictionaries = preimage.grades.dictionaries.Dictionaries()

    structure()
