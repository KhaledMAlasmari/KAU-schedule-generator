import datetime
import unittest
from requests import get
from bs4 import BeautifulSoup
from main import get_all_possible_schedules
from parse_info import calculate_lecture_length, parse_course_name, parse_days, parse_info, parse_professor, parse_section_id, parse_section_name, parse_time

class TestInfoParser(unittest.TestCase):

    def test_time_parser(self):
        response = get('https://odusplus-ss.kau.edu.sa/PROD/xwckschd.p_disp_detail_sched?term_in=202201&crn_in=40209')
        soup = BeautifulSoup(response.text, 'html.parser')
        lecture_info = soup.select_one('body > table:nth-child(3) > tr:nth-child(3)')
        time: str = lecture_info.findAll('td')[1].text
        lecture_time = parse_time(time)
        date = datetime.datetime(1900, 1, 1, 11, 0, 0)
        self.assertEqual(lecture_time, date)

    def test_days_parser(self):
        response = get('https://odusplus-ss.kau.edu.sa/PROD/xwckschd.p_disp_detail_sched?term_in=202201&crn_in=40209')
        soup = BeautifulSoup(response.text, 'html.parser')
        lecture_info = soup.select_one('body > table:nth-child(3) > tr:nth-child(3)')
        lecture_days = parse_days(lecture_info)
        self.assertEqual(lecture_days, 'MW')


    def test_professor_parser(self):
        response = get('https://odusplus-ss.kau.edu.sa/PROD/xwckschd.p_disp_detail_sched?term_in=202201&crn_in=40209')
        soup = BeautifulSoup(response.text, 'html.parser')
        lecture_info = soup.select_one('body > table:nth-child(3) > tr:nth-child(3)')
        professor_name = parse_professor(lecture_info)
        # goated professor wallah
        self.assertEqual(professor_name, 'احمد الحسين حرباوي (P)')

    def test_course_name_parser(self):
        response = get('https://odusplus-ss.kau.edu.sa/PROD/xwckschd.p_disp_detail_sched?term_in=202201&crn_in=40209')
        soup = BeautifulSoup(response.text, 'html.parser')
        course_info = soup.select_one('body > table:nth-child(2)').findChild('tr').text
        course_name = parse_course_name(course_info)
        # goated professor wallah
        self.assertEqual(course_name, "CPCS 212")


    def test_section_name_parser(self):
        response = get('https://odusplus-ss.kau.edu.sa/PROD/xwckschd.p_disp_detail_sched?term_in=202201&crn_in=40209')
        soup = BeautifulSoup(response.text, 'html.parser')
        course_info = soup.select_one('body > table:nth-child(2)').findChild('tr').text
        section_name = parse_section_name(course_info)
        # goated professor wallah
        self.assertEqual(section_name, "BE")

    def test_section_id_parser(self):
        response = get('https://odusplus-ss.kau.edu.sa/PROD/xwckschd.p_disp_detail_sched?term_in=202201&crn_in=40209')
        soup = BeautifulSoup(response.text, 'html.parser')
        course_info = soup.select_one('body > table:nth-child(2)').findChild('tr').text
        section_id = parse_section_id(course_info)
        # goated professor wallah
        self.assertEqual(section_id, "40209")
    def test_lecture_length_calculator(self):
        response = get('https://odusplus-ss.kau.edu.sa/PROD/xwckschd.p_disp_detail_sched?term_in=202201&crn_in=40209')
        soup = BeautifulSoup(response.text, 'html.parser')
        lecture_info = soup.select_one('body > table:nth-child(3) > tr:nth-child(3)')
        lecture_length = calculate_lecture_length(lecture_info)
        # goated professor wallah
        self.assertEqual(lecture_length, 80)

    def test_info_parser(self):
        sections_204 = [
        'https://odusplus-ss.kau.edu.sa/PROD/xwckschd.p_disp_detail_sched?term_in=202201&crn_in=40202',
        'https://odusplus-ss.kau.edu.sa/PROD/xwckschd.p_disp_detail_sched?term_in=202201&crn_in=40203',
        'https://odusplus-ss.kau.edu.sa/PROD/xwckschd.p_disp_detail_sched?term_in=202201&crn_in=40198',
        'https://odusplus-ss.kau.edu.sa/PROD/xwckschd.p_disp_detail_sched?term_in=202201&crn_in=40199',
        'https://odusplus-ss.kau.edu.sa/PROD/xwckschd.p_disp_detail_sched?term_in=202201&crn_in=40200',
        'https://odusplus-ss.kau.edu.sa/PROD/xwckschd.p_disp_detail_sched?term_in=202201&crn_in=40201']
        course = parse_info(sections_204)
        self.assertEqual(len(course.get_sections()), 6)
        self.assertEqual(course.get_course_name(), "CPCS 204")

   

class TestSchedulesGenerator(unittest.TestCase):
    def test_conflicted_sections(self):
        sections_204 = ['https://odusplus-ss.kau.edu.sa/PROD/xwckschd.p_disp_detail_sched?term_in=202201&crn_in=40202']
        sections_211 = ['https://odusplus-ss.kau.edu.sa/PROD/xwckschd.p_disp_detail_sched?term_in=202201&crn_in=40205']
        sections_212 = ['https://odusplus-ss.kau.edu.sa/PROD/xwckschd.p_disp_detail_sched?term_in=202201&crn_in=40212']
        course1 = parse_info(sections_204)
        course2 = parse_info(sections_211)
        course3 = parse_info(sections_212)
        schedules = get_all_possible_schedules(course1, course2, course3)
        self.assertEqual(len(schedules), 0)

if __name__ == '__main__':
    unittest.main()