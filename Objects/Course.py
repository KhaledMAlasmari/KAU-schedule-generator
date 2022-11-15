from .Section import Section
from typing import List

class Course:
    def __init__(self, sections: List[Section], course_name: str) -> None:
        self.__sections = sections
        self.__course_name = course_name


    def get_sections(self):
        return self.__sections

    def get_course_name(self):
        return self.__course_name