from bs4 import BeautifulSoup
from dmoj.result import CheckerResult
from dmoj.utils.chrome_driver import get_driver

def structure_changed(soup):
  return len(soup.find_all("nav", id="navbar")) != 1 or len(soup.find_all("nav",)) != 1 or len(soup.find_all( id="navbar")) != 1
  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  if structure_changed(soup):
    return CheckerResult(False, 0, "")
  
  # criteria 1
  if input == "Phần từ #navbar có position fixed":
    driver = get_driver(source)
    
    element = driver.find_element_by_id("navbar")
    
    css = driver.get_computed_style(element, 'position')
    
    driver.quit()

    if css == 'fixed':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Sử dụng CSS top 0 pixels cho #navbar":
    driver = get_driver(source)
    
    element = driver.find_element_by_id("navbar")
    
    css = driver.get_computed_style(element, 'top')
    
    driver.quit()

    if css == '0px':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 3
  if input == "Sử dụng CSS left 0 pixels cho #navbar":
    driver = get_driver(source)
    
    element = driver.find_element_by_id("navbar")
    
    css = driver.get_computed_style(element, 'left')
    
    driver.quit()

    if css == '0px':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  return CheckerResult(False, 0, "Lỗi checker")