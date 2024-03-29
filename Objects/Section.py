from datetime import date, timedelta
import time
from .Lecture import *


class Section:

    def __init__(self, course_name: str, section_name: str, section_id: str, normal_professor: str, normal_lecture_time: date, normal_length: int, normal_lecture_days: str, lab_time: date or None=None, lab_length: int or None=None, lab_lecture_day: str or None= None, lab_professor: str or None= None, extra_professor: str or None= None, extra_length: str or None= None, extra_lecture_time: date or None= None, extra_lecture_days: str or None= None):
        self.course_name = course_name
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
        
        self.__extra_professor = extra_professor
        self.__extra_lecture_length = extra_length
        self.__extra_lecture_time = extra_lecture_time
        self.__extra_lecture_days = extra_lecture_days
        
        self.lectures = []
        self.add_lectures_to_list(self.get_normal_lecture_start_time(), self.get_normal_lecture_end_time(), self.get_normal_lecture_days())
        if self.__lab_lecture_time:
            self.add_lectures_to_list(self.get_lab_lecture_start_time(), self.get_lab_lecture_end_time(), self.get_lab_lecture_day())
        if self.__extra_lecture_time:
            self.add_lectures_to_list(self.get_extra_lecture_start_time(), self.get_extra_lecture_end_time(), self.get_extra_lecture_days())
    def get_normal_lecture_start_time(self):
        return self.__normal_lecture_time

    def get_lab_lecture_start_time(self):
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
    
    def get_extra_lecture_end_time(self):
        return self.__extra_lecture_time + timedelta(minutes=self.__extra_lecture_length)
    
    def get_extra_lecture_start_time(self):
        return self.__extra_lecture_time
    def get_extra_lecture_days(self):
        return self.__extra_lecture_days
    def get_normal_lecture_days(self):
        return self.__normal_lecture_days

    def get_lab_lecture_day(self):
        return self.__lab_lecture_day

    def add_lectures_to_list(self, start: date, end: date, days: str):
        days = list(days)
        for day in days:
            self.lectures.append(
                Lecture(self.__section_name, start, end, day, self.__section_id))

    def __str__(self) -> str:
        if not self.__lab_lecture_time and not self.__extra_lecture_time:
            return f'course name {self.course_name} professor:{self.__normal_professor} section name {self.__section_name} section id {self.__section_id} normal days {self.__normal_lecture_days}-{self.__normal_lecture_time.strftime("%H:%M:%S")}'
        elif not self.__extra_lecture_time:
            return f'course name {self.course_name} professor:{self.__normal_professor} section name {self.__section_name} section id {self.__section_id} normal days\n{self.__normal_lecture_days}-{self.__normal_lecture_time.strftime("%H:%M:%S")} lab professor:{self.__lab_professor} lab days {self.__lab_lecture_day} - {self.__lab_lecture_time.strftime("%H:%M:%S")}'
        else:
            return f'course name {self.course_name} professor:{self.__normal_professor} section name {self.__section_name} section id {self.__section_id} normal days\n{self.__normal_lecture_days}-{self.__normal_lecture_time.strftime("%H:%M:%S")} lab professor:{self.__lab_professor} lab days {self.__lab_lecture_day} - {self.__lab_lecture_time.strftime("%H:%M:%S")}\nextra lecture professor:{self.__extra_professor} extra lecture days {self.__extra_lecture_days} - {self.__extra_lecture_time.strftime("%H:%M:%S")}' 
