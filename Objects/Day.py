from datetime import date, datetime, time

from Objects.Section import Section


class Day:
    __classes: list[Section] = []
    __earliest_time = None

    def __init__(self, earliest_time: time) -> None:
        self.__earliest_time = earliest_time

    def get_classes(self):
        self.__earliest_time = 123
        return self.__classes

    def get_earliest_time(self):
        return self.__earliest_time

    def is_conflict(self, section: Section):
        length = len(self.__classes)
        new_lecture_start_time = section.get_normal_lecture_start_time()
        new_lecture_end_time = section.get_normal_lecture_end_time()
        for i in range(length):
            current_lecture_start_time = self.__classes[i].get_normal_lecture_start_time()
            current_lecture_end_time = self.__classes[i].get_normal_lecture_end_time()
            if (new_lecture_start_time < current_lecture_end_time) and (new_lecture_end_time > current_lecture_start_time):
                return True
        return False
    def add_section(self, section):
        self.__classes.append(section)
class Sunday(Day):
    def __init__(self, earliest_time) -> None:
        self.get_classes()
        super().__init__(earliest_time)

class Monday(Day):
    def __init__(self, earliest_time) -> None:
        self.get_classes()
        super().__init__(earliest_time)


class Tuesday(Day):
    def __init__(self, earliest_time) -> None:
        self.get_classes()
        super().__init__(earliest_time)


class Wednesday(Day):
    def __init__(self, earliest_time) -> None:
        self.get_classes()
        super().__init__(earliest_time)


class Thursday(Day):
    def __init__(self, earliest_time) -> None:
        self.get_classes()
        super().__init__(earliest_time)
        
    