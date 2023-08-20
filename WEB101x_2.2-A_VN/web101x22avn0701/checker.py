from bs4 import BeautifulSoup, Comment
from dmoj.result import CheckerResult
from dmoj.utils.unicode import utf8text
from dmoj.utils.css_parser import parse_css, get_element_css_value
from dmoj.utils.chrome_driver import get_driver

def structure_changed(soup):
  return soup.find_all("h2") != 1

def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  if structure_changed(soup):
    return CheckerResult(False, 0, "")
  
  # criteria 1
  if input == "Phần tử h2 có position relative":
    driver = get_driver(source)
    
    element = driver.get_element_by_tag_name("h2")
    
    css = driver.get_computed_style(element, 'position')
    
    driver.quit()

    if css == 'relative':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Sử dụng CSS offset để đặt vị trí h2 cách 15px so với vị trí top ban đầu của nó":
    driver = get_driver(source)
    
    element = driver.get_element_by_tag_name("h2")
    
    css = driver.get_computed_style(element, 'top')
    
    driver.quit()

    if css == '15px':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  return CheckerResult(False, 0, "Lỗi checker")