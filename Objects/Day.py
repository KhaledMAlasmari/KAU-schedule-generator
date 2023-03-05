from datetime import date
from Objects.Lecture import Lecture
from typing import List
class Day:

    def __init__(self) -> None:
        self.__lectures: List[Lecture] = []

    def is_empty(self) -> bool :
        return len(self.__lectures) == 0
    def get_lectures(self):
        return self.__lectures

    def is_conflict(self, new_lecture_start_time: date, new_lecture_end_time: date):
        length = len(self.__lectures)
        for i in range(length):
            current_lecture_start_time = self.__lectures[i].start_time
            current_lecture_end_time = self.__lectures[i].end_time
            # check if normal lecture is conflict
            if (new_lecture_start_time < current_lecture_end_time) and (new_lecture_end_time > current_lecture_start_time):
                return True
        return False

    def add_lecture(self, lecture: Lecture):
        self.__lectures.append(lecture)
class Sunday(Day):
    def __init__(self, ) -> None:
        super().__init__()

class Monday(Day):
    def __init__(self, ) -> None:
        super().__init__()


class Tuesday(Day):
    def __init__(self, ) -> None:
        super().__init__()


class Wednesday(Day):
    def __init__(self, ) -> None:
        super().__init__()


class Thursday(Day):
    def __init__(self, ) -> None:
        super().__init__()
        
    