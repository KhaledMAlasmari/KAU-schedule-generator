from .Lecture import Lecture
from .Day import *
class Schedule:
    def __init__(self) -> None:
        self.sunday = Sunday()
        self.monday = Monday()
        self.tuesday = Tuesday()
        self.wednesday = Wednesday()
        self.thursday = Thursday()
        self.sections: list[Section] = []

    def add_section(self, section: Section) -> bool:
        is_conflict = False
        lecture: Lecture
        for lecture in section.lectures:
            is_conflict = self.check_if_lecture_is_conflict(lecture.start_time, lecture.end_time, lecture.day)
            if(is_conflict):
                return False
        
        if(not is_conflict):
            for lecture in section.lectures:
                self.add_lectures_to_days(lecture, lecture.day)
            self.sections.append(section)
            return True
        return False
                
    def check_if_lecture_is_conflict(self, start_time: date, end_time: date, day: str) -> bool:
        if day == 'U':
            return self.sunday.is_conflict(start_time, end_time)
        elif day == 'M':
            return self.monday.is_conflict(start_time, end_time)
        elif day == 'T':
            return self.tuesday.is_conflict(start_time, end_time)
        elif day == 'W':
            return self.wednesday.is_conflict(start_time, end_time)
        elif day == 'R':
            return self.thursday.is_conflict(start_time, end_time)


    def add_lectures_to_days(self, lecture, day) -> bool:
        if day == 'U':
            return self.sunday.add_lecture(lecture)
        elif day == 'M':
            return self.monday.add_lecture(lecture)
        elif day == 'T':
            return self.tuesday.add_lecture(lecture)
        elif day == 'W':
            return self.wednesday.add_lecture(lecture)
        elif day == 'R':
            return self.thursday.add_lecture(lecture)


    def __str__(self):
        return "".join([str(x) + "\n" for x in self.sections])


    