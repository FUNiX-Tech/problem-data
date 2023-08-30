from bs4 import BeautifulSoup
from dmoj.result import CheckerResult
from dmoj.utils.css_parser import parse_css, get_element_css_value

def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  # criteria 1
  if input == "#box-1 có flex là 2 2 150px":
    if soup.find(id="box-1") and get_element_css_value(soup, soup.find(id="box-1"), 'flex') == "2 2 150px": 
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 2
  if input == "#box-2 có flex là 1 1 150px":
    if soup.find(id="box-2") and get_element_css_value(soup, soup.find(id="box-2"), 'flex') == "1 1 150px": 
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 3
  if input == "#box-1 và #box-2 có property flex":
    if soup.find(id="box-1") and get_element_css_value(soup, soup.find(id="box-1"), 'flex') and soup.find(id="box-2") and get_element_css_value(soup, soup.find(id="box-2"), 'flex'):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  return CheckerResult(False, 0, "Lỗi checker")
