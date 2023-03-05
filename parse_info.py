from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup
import re
from Objects.Section import Section
from Objects.Course import Course
from Objects.Exceptions import NoExtraLectureException, NoLabLectureException

from typing import List


def parse_info(sections_links : List[str]) -> Course:
    length = len(sections_links)
    sections: List[Section] = []
    for i in range(length):
        response = requests.get(sections_links[i])
        soup = BeautifulSoup(response.text.encode("utf-8"), 'html.parser', from_encoding="UTF-8")
        normal_lecture_time, normal_lecture_days, normal_lecture_professor, course_name, section_name, section_id, normal_length = parse_normal_lecture_info(soup)
        section: Section
        try:
            lab_lecture_time, lab_lecture_days, lab_lecture_professor, lab_length = parse_lab_lecture_info(soup)
            extra_lecture_time, extra_lecture_days, extra_lecture_professor, extra_lecture_length = parse_extra_lecture_info(soup)
            section = Section(course_name, section_name, section_id, normal_lecture_professor, normal_lecture_time, normal_length, normal_lecture_days, lab_lecture_time, lab_length, lab_lecture_days, lab_lecture_professor, extra_lecture_professor, extra_lecture_length, extra_lecture_time, extra_lecture_days)
        except NoLabLectureException:
            section = Section(course_name, section_name, section_id, normal_lecture_professor, normal_lecture_time, normal_length, normal_lecture_days)
        except NoExtraLectureException:
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


def parse_lab_lecture_info(soup: BeautifulSoup):
        try:
            lab_lecture_info = soup.select_one('body > table:nth-child(3) > tr:nth-child(4)')
            lab_time = lab_lecture_info.findAll('td')[1].text
            lab_lecture_time = parse_time(lab_time)
            lab_lecture_days  = parse_days(lab_lecture_info)
            lab_lecture_professor = parse_professor(lab_lecture_info)
            lab_length = calculate_lecture_length(lab_lecture_info)
            return lab_lecture_time, lab_lecture_days, lab_lecture_professor, lab_length
        except (NameError, AttributeError) as e:
            raise NoLabLectureException



def parse_normal_lecture_info(soup: BeautifulSoup):
        course_info = soup.select_one('body > table:nth-child(2)').findChild('tr')
        normal_lecture_info = soup.select_one('body > table:nth-child(3) > tr:nth-child(3)')
        time: str = normal_lecture_info.findAll('td')[1].text
        normal_lecture_time = parse_time(time)
        normal_lecture_days  = parse_days(normal_lecture_info)
        normal_lecture_professor = parse_professor(normal_lecture_info)
        course_name = parse_course_name(course_info.text)
        section_name = parse_section_name(course_info.text)
        section_id = parse_section_id(course_info.text)
        normal_length = calculate_lecture_length(normal_lecture_info)
        return normal_lecture_time, normal_lecture_days, normal_lecture_professor, course_name, section_name, section_id, normal_length
    
    
def parse_extra_lecture_info(soup: BeautifulSoup):
        try:
            extra_lecture_info = soup.select_one('body > table:nth-child(3) > tr:nth-child(5)')
            extra_time = extra_lecture_info.findAll('td')[1].text
            extra_lecture_time = parse_time(extra_time)
            extra_lecture_days  = parse_days(extra_lecture_info)
            extra_lecture_professor = parse_professor(extra_lecture_info)
            extra_length = calculate_lecture_length(extra_lecture_info)
            return extra_lecture_time, extra_lecture_days, extra_lecture_professor, extra_length
        except (NameError, AttributeError) as e:
            raise NoExtraLectureException
