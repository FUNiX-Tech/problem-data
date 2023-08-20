from bs4 import BeautifulSoup
from dmoj.result import CheckerResult
from dmoj.utils.css_parser import parse_css, get_element_css_value, count_element
import re
  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')

  if count_element(soup, 'h4') != 1:
    return CheckerResult(False, 0, "")
  
  h4 = soup.h4
  
  # criteria 1
  if input == "Thẻ h4 có background-color là rgba(45, 45, 45, 0.1)":
    bg = get_element_css_value(soup, h4, 'background-color')
    bg = re.sub(r" !important", "", bg)
    bg = re.sub(r" +", "", bg)

    if bg == "rgba(45, 45, 45, 0.1)":
      return CheckerResult(True, point_value, "")

    return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Thẻ h4 có padding 10 pixels":
    padding = get_element_css_value(soup, h4, 'padding')
    padding = re.sub(r" !important", "", padding)

    if padding == "10px":
      return CheckerResult(True, point_value, "")
      
    return CheckerResult(False, 0, "")
  
  # criteria 3
  if input == "Loại bỏ property height của thẻ h4":
    height = get_element_css_value(soup, h4, 'height')
    height = re.sub(r" !important", "", height)

    if height is None or height == "":
      return CheckerResult(True, point_value, "")
      
    return CheckerResult(False, 0, "")
  
  return CheckerResult(False, 0, "Lỗi checker")