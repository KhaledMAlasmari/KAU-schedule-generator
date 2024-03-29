from re import A
from Objects.Course import Course
from Objects.Schedule import Schedule
from Objects.Section import Section
from parse_info import parse_info
from itertools import product
from typing import List

def main():
    sections_401 = [
        'https://odusplus-ss.kau.edu.sa/PROD/xwckschd.p_disp_detail_sched?term_in=202201&crn_in=38833'
    ]

    sections_204 = [
        'https://odusplus-ss.kau.edu.sa/PROD/xwckschd.p_disp_detail_sched?term_in=202201&crn_in=40202',
        'https://odusplus-ss.kau.edu.sa/PROD/xwckschd.p_disp_detail_sched?term_in=202201&crn_in=40203',
        'https://odusplus-ss.kau.edu.sa/PROD/xwckschd.p_disp_detail_sched?term_in=202201&crn_in=40198',
        'https://odusplus-ss.kau.edu.sa/PROD/xwckschd.p_disp_detail_sched?term_in=202201&crn_in=40199',
        'https://odusplus-ss.kau.edu.sa/PROD/xwckschd.p_disp_detail_sched?term_in=202201&crn_in=40200',
        'https://odusplus-ss.kau.edu.sa/PROD/xwckschd.p_disp_detail_sched?term_in=202201&crn_in=40201'
    ]
    sections_211 = [
        'https://odusplus-ss.kau.edu.sa/PROD/xwckschd.p_disp_detail_sched?term_in=202201&crn_in=40208',
        'https://odusplus-ss.kau.edu.sa/PROD/xwckschd.p_disp_detail_sched?term_in=202201&crn_in=40207',
        'https://odusplus-ss.kau.edu.sa/PROD/xwckschd.p_disp_detail_sched?term_in=202201&crn_in=40206',
        'https://odusplus-ss.kau.edu.sa/PROD/xwckschd.p_disp_detail_sched?term_in=202201&crn_in=40205'
    ]
    sections_212 = [
        'https://odusplus-ss.kau.edu.sa/PROD/xwckschd.p_disp_detail_sched?term_in=202201&crn_in=40211',
        'https://odusplus-ss.kau.edu.sa/PROD/xwckschd.p_disp_detail_sched?term_in=202201&crn_in=40212',
        'https://odusplus-ss.kau.edu.sa/PROD/xwckschd.p_disp_detail_sched?term_in=202201&crn_in=40210',
        'https://odusplus-ss.kau.edu.sa/PROD/xwckschd.p_disp_detail_sched?term_in=202201&crn_in=40209'
    ]
    course1 = parse_info(sections_401)
    course2 = parse_info(sections_211)
    course3 = parse_info(sections_212)
    course4 = parse_info(sections_204)
    schedules = get_all_possible_schedules(course1, course2, course3, course4)
    print_schedules(schedules)

def get_all_possible_schedules(*argv: Course) -> List[Schedule]:
    schedules: List[Schedule] = []
    sections = []
    for course in (argv):
        sections.append(course.get_sections())
    for tuple_of_sections in product(*sections):
        section : Section
        schedule: Schedule = Schedule()
        for section in tuple_of_sections: #type: Section
            # if the section is conflicted with another, just break and don't consider this schedule 
            if(not schedule.add_section(section)):
                break
        if(len(schedule.sections) == len(argv)):
            schedules.append(schedule)
    return schedules
        


def print_schedules(schedules: List[Schedule]):
    length = len(schedules)
    for i in range(length):
        print("########################################")
        print(schedules[i])
        print(f"days with lectures are: {schedules[i].get_days_with_lectures()}")
if __name__ == "__main__":
    main()
