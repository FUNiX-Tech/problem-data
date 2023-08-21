from bs4 import BeautifulSoup
from dmoj.result import CheckerResult
from dmoj.utils.chrome_driver import get_driver
  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  # criteria 1
  if input == "Phần tử có id left có float là left":
    if len(soup.find_all(id="left")) != 1:
      return CheckerResult(False, 0, "")
      
    driver = get_driver(source)
    
    element = driver.find_element_by_id("left")
    
    css = driver.get_computed_style(element, 'float')
    
    driver.quit()

    if css == 'left':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Phần tử có id right có float right":
    if len(soup.find_all(id="right")) != 1:
      return CheckerResult(False, 0, "")

    driver = get_driver(source)
    
    element = driver.find_element_by_id("right")
    
    css = driver.get_computed_style(element, 'float')
    
    driver.quit()

    if css == 'right':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  return CheckerResult(False, 0, "Lỗi checker")