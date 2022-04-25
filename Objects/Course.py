from .Section import Section

class Course:
    __sections = None
    __course_name = None
    def __init__(self, sections: list[Section], course_name: str) -> None:
        self.__sections = sections
        self.__course_name = course_name


    def get_sections(self):
        return self.__sections

    def get_course_name(self):
        return self.__course_name