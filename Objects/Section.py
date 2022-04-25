from datetime import date, timedelta


class Section:
    __section_name = None
    __section_id = None
    __normal_professor = None
    __lab_professor = None
    __normal_lecture_time = None
    __lab_lecture_time = None
    __normal_lecture_length = None
    __lab_lecture_length = None
    __normal_lecture_days = None
    __lab_lecture_day = None
    def __init__(self, section_name: str, section_id: str, normal_professor: str, normal_lecture_time: date, normal_length: int, normal_lecture_days: str, lab_time: date|None, lab_length: int|None, lab_lecture_day: str|None, lab_professor: str|None):
        self.__section_name = section_name
        self.__section_id = section_id
        self.__normal_professor = normal_professor
        self.__normal_lecture_length = normal_length
        self.__lab_lecture_length = lab_length
        self.__normal_lecture_time = normal_lecture_time
        self.__lab_lecture_time = lab_time
        self.__normal_lecture_days = normal_lecture_days
        self.__lab_lecture_day = lab_lecture_day
        self.__lab_professor = lab_professor


    def get_normal_lecture_start_time(self):
        return self.__normal_lecture_time
    def get_lab_time(self):
        return self.__lab_lecture_time
    def get_section_name(self):
        return self.__section_name
    def get_section_id(self):
        return self.__section_id
    def get_professor(self):
        return self.__normal_professor
    def get_normal_lecture_end_time(self):
        return self.__normal_lecture_time + timedelta(minutes=self.__normal_lecture_length)
    def get_lab_lecture_end_time(self):
        return self.__lab_lecture_time + timedelta(minutes=self.__lab_lecture_length)
    def get_normal_lecture_days(self):
        return self.__normal_lecture_days
    def get_lab_lecture_day(self):
        return self.__lab_lecture_day

    def __str__(self) -> str:
        return f'course name {self.__section_name} section id {self.__section_id} professor {self.__normal_professor}'