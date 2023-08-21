from bs4 import BeautifulSoup
from dmoj.result import CheckerResult
from dmoj.utils.chrome_driver import get_driver
  

def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  # criteria 1
  if input == "Phần tử img có class smaller-image":
    if soup.find("img", attrs={"class": "smaller-image"}):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Phần tử img rộng 100 pixels":
    if len(soup.find_all("img")) != 1:
      return CheckerResult(False, 0, "")

    driver = get_driver(source)
    
    element = driver.find_element_by_tag_name("img")
    
    css = "" if element is None else driver.get_computed_style(element, 'width')
    
    driver.quit()

    if css == '100px':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  return CheckerResult(False, 0, "Lỗi checker")