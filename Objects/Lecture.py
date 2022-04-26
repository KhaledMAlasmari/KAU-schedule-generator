from datetime import date

class Lecture:
    def __init__(self,course_name: str, start: date, end: date, day: str, section_id: str) -> None:
        self.course_name = course_name
        self.start_time = start
        self.end_time = end
        self.day = day
        self.section_id = section_id