
class Dictionaries:

    def __init__(self):
        """

        """

    @staticmethod
    def new_student(name: str):

        return dict(name=name, courses=[])

    @staticmethod
    def add_grade(record: dict, course: str, grade: int):

        return record['courses'].append(dict(name=course, mark=grade))



