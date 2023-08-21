from bs4 import BeautifulSoup, Comment
from dmoj.result import CheckerResult
from dmoj.utils.unicode import utf8text
from dmoj.utils.css_parser import parse_css, get_element_css_value
from dmoj.utils.chrome_driver import get_driver

def structure_changed(soup):
  return len(soup.find_all("form", id="searchbar")) != 1 or len(soup.find_all("form")) != 1 or len(soup.find_all(id="searchbar")) != 1 
  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  if structure_changed(soup):
    return CheckerResult(False, 0, "")
  
  # criteria 1
  if input == "Phần từ có id #searchbar có position absolute":
    driver = get_driver(source)
    
    element = driver.find_element_by_id("searchbar")
    
    css = driver.get_computed_style(element, 'position')
    
    driver.quit()

    if css == 'absolute':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Sử dụng CSS top 50 pixels cho #searchbar":
    driver = get_driver(source)
    
    element = driver.find_element_by_id("searchbar")
    
    css = driver.get_computed_style(element, 'top')
    
    driver.quit()

    if css == '50px':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 3
  if input == "Sử dụng CSS right 50 pixels cho #searchbar":
    driver = get_driver(source)
    
    element = driver.find_element_by_id("searchbar")
    
    css = driver.get_computed_style(element, 'right')
    
    driver.quit()

    if css == '50px':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  return CheckerResult(False, 0, "Lỗi checker")