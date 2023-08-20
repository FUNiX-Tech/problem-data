from bs4 import BeautifulSoup, Comment
from dmoj.result import CheckerResult
from dmoj.utils.unicode import utf8text
from dmoj.utils.css_parser import parse_css, get_element_css_value
from dmoj.utils.chrome_driver import get_driver
  
def structure_changed(soup):
  return soup.find_all("div", id="box-container") != 1 
  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  if structure_changed(soup):
    return CheckerResult(False, 0, "")
  
  # criteria 1
  if input == "Phần tử có id left có float là left":
    driver = get_driver(source)
    
    element = driver.get_element_by_id("box-container")
    
    css = driver.get_computed_style(element, 'display')
    
    driver.quit()

    if css == 'flex':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  return CheckerResult(False, 0, "Lỗi checker")