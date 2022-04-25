from Objects.Schedule import Schedule
from Objects.Section import Section
from parse_info import parse_info
def main():
    sections = [
        'https://odusplus-ss.kau.edu.sa/PROD/xwckschd.p_disp_detail_sched?term_in=202201&crn_in=40202',
        'https://odusplus-ss.kau.edu.sa/PROD/xwckschd.p_disp_detail_sched?term_in=202201&crn_in=40203'
    ]
    course1 = parse_info(sections, "cpcs-204")
    sorted_sections = sort_sections_based_on_time(course1.get_sections())
    #get_all_courses_permutations()


def get_all_courses_permutations():
    schedules: Schedule = []



def sort_sections_based_on_time(sections: list[Section]):
    sorted_list = sorted(sections, key=lambda section: section.get_normal_lecture_start_time())
    return sorted_list


if __name__ == "__main__":
    main()
