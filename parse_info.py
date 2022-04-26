from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup
import re
from Objects.Section import Section
from Objects.Course import Course

def parse_info(sections_links : list[str]) -> Course:
    length = len(sections_links)
    sections: list[Section] = []
    for i in range(length):
        response = requests.get(sections_links[i])
        soup = BeautifulSoup(response.text, 'html.parser')
        course_info = soup.select_one('body > table:nth-child(2)').findChild('tr')
        normal_lecture_info = soup.select_one('body > table:nth-child(3) > tr:nth-child(3)')
        lab_lecture_info = soup.select_one('body > table:nth-child(3) > tr:nth-child(4)')
        time: str = normal_lecture_info.findAll('td')[1].text
        lab_time: str = lab_lecture_info.findAll('td')[1].text
        normal_lecture_time = parse_time(time)
        lab_lecture_time = parse_time(lab_time)
        normal_lecture_days  = parse_days(normal_lecture_info)
        lab_lecture_days  = parse_days(lab_lecture_info)
        normal_lecture_professor = parse_professor(normal_lecture_info)
        lab_lecture_professor = parse_professor(lab_lecture_info)
        course_name = parse_course_name(course_info.text)
        section_name = parse_section_name(course_info.text)
        section_id = parse_section_id(course_info.text)
        normal_length = calculate_lecture_length(normal_lecture_info)
        lab_length = calculate_lecture_length(lab_lecture_info)
        section = Section(course_name, section_name, section_id, normal_lecture_professor, normal_lecture_time, normal_length, normal_lecture_days, lab_lecture_time, lab_length, lab_lecture_days, lab_lecture_professor)
        sections.append(section)
    return Course(sections, course_name)



def parse_time(time):
    match_time = re.search('^(\d*:\d* (AM|PM))', time).group(1)
    classtime = datetime.strptime(match_time, '%I:%M %p')
    return classtime

def parse_days(lecture):
    days: str = lecture.findAll('td')[2].text
    return days


def parse_professor(lecture):
    professor: str = lecture.findAll('td')[6].text
    return professor

def parse_course_name(course_info):
    course_name = re.search('[a-zA-Z]{2,4} \d+', course_info).group(0)
    return course_name

def parse_section_name(course_info):
    section_name = re.search('\w+$', course_info).group(0)
    return section_name

def parse_section_id(course_info):
    section_id = re.search("\d{5}", course_info).group(0)
    return section_id

def calculate_lecture_length(lecture):
    time: str = lecture.findAll('td')[1].text
    match_start_time = re.search('^(\d*:\d* (AM|PM))', time).group(1)
    match_end_time = re.search('(\d*:\d* (AM|PM))$', time).group(1)
    class_start_time = datetime.strptime(match_start_time, '%I:%M %p')
    class_end_time = datetime.strptime(match_end_time, '%I:%M %p')
    length = timedelta(hours=class_end_time.time().hour, minutes=class_end_time.time().minute) - timedelta(hours=class_start_time.time().hour, minutes=class_start_time.time().minute)
    return length.seconds / 60