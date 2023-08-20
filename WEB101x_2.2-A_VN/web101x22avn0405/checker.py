from bs4 import BeautifulSoup, Comment
from dmoj.result import CheckerResult
from dmoj.utils.unicode import utf8text
from dmoj.utils.css_parser import parse_css, get_element_css_value, count_element
from dmoj.utils.chrome_driver import get_driver
  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')

  # criteria 1
  if input == "h1 có font-weight 800":
    if count_element(soup, "h1") != 1:
      return CheckerResult(False, 0, "")
    
    driver = get_driver(source)
    
    element = driver.find_element_by_tag_name("h1")

    css = driver.get_computed_style(element, 'font-weight') if element is not None else None

    driver.quit()
    
    if css == "800":
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
    

  # criteria 2
  if input == "h2 có font-weight 600":
    if count_element(soup, "h2") != 1:
      return CheckerResult(False, 0, "")
    
    driver = get_driver(source)
    
    element = driver.find_element_by_tag_name("h2")

    css = driver.get_computed_style(element, 'font-weight') if element is not None else None

    driver.quit()
    
    if css == "600":
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 3
  if input == "h3 có font-weight 500":
    if count_element(soup, "h3") != 1:
      return CheckerResult(False, 0, "")
    
    driver = get_driver(source)
    
    element = driver.find_element_by_tag_name("h3")

    css = driver.get_computed_style(element, 'font-weight') if element is not None else None

    driver.quit()
    
    if css == "500":
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 4
  if input == "h4 có font-weight 400":
    if count_element(soup, "h4") != 1:
      return CheckerResult(False, 0, "")
    
    driver = get_driver(source)
    
    element = driver.find_element_by_tag_name("h4")

    css = driver.get_computed_style(element, 'font-weight') if element is not None else None

    driver.quit()
    
    if css == "400":
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 5
  if input == "h5 có font-weight 300":
    if count_element(soup, "h5") != 1:
      return CheckerResult(False, 0, "")
    
    driver = get_driver(source)
    
    element = driver.find_element_by_tag_name("h5")

    css = driver.get_computed_style(element, 'font-weight') if element is not None else None

    driver.quit()
    
    if css == "300":
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 6
  if input == "h6 có font-weight 200":
    if count_element(soup, "h6") != 1:
      return CheckerResult(False, 0, "")
    
    driver = get_driver(source)
    
    element = driver.find_element_by_tag_name("h6")

    css = driver.get_computed_style(element, 'font-weight') if element is not None else None

    driver.quit()
    
    if css == "200":
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  return CheckerResult(False, 0, "Lỗi checker")