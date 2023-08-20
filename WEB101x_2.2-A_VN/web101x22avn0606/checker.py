from bs4 import BeautifulSoup, Comment
from dmoj.result import CheckerResult
from dmoj.utils.unicode import utf8text
from dmoj.utils.css_parser import parse_css, get_element_css_value
from dmoj.utils.chrome_driver import get_driver

def structure_changed(soup):
  return soup.find_all("h5", attrs={"class": "injected-text"}) != 1 or \
    soup.find_all("div", attrs={"class": "box yellow-box"}) != 1 or \
    soup.find_all("h5", attrs={"class": "box red-box"}) != 1 or \
    soup.find_all("h5", attrs={"class": "box blue-box"}) != 1
  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  if structure_changed(soup):
    return CheckerResult(False, 0, "")
  
  # criteria 1
  if input == "Class blue-box có margin top 40px":
    driver = get_driver(source)
    
    blue_box = driver.get_element_by_class_name("blue-box")
    
    css = driver.get_computed_style(blue_box, 'margin-top')
    
    driver.quit()

    if css == '40px':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Class blue-box có margin right 20px":
    driver = get_driver(source)
    
    blue_box = driver.get_element_by_class_name("blue-box")
    
    css = driver.get_computed_style(blue_box, 'margin-right')
    
    driver.quit()

    if css == '20px':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 3
  if input == "Class blue-box có margin-bottom 20px":
    driver = get_driver(source)
    
    blue_box = driver.get_element_by_class_name("blue-box")
    
    css = driver.get_computed_style(blue_box, 'margin-bottom')
    
    driver.quit()

    if css == '20px':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 4
  if input == "Class blue-box có margin left 40px":
    driver = get_driver(source)
    
    blue_box = driver.get_element_by_class_name("blue-box")
    
    css = driver.get_computed_style(blue_box, 'margin-left')
    
    driver.quit()

    if css == '40px':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 5
  if input == "Sử dụng quy tắc theo chiều kim đồng hồ để set margin cho class blue-box":
    driver = get_driver(source)
    
    blue_box = driver.get_element_by_class_name("blue-box")
    
    css = driver.get_computed_style(blue_box, 'margin-left')
    
    if blue_box is None:
      return CheckerResult(False, 0, "")

    padding = driver.get_computed_style(blue_box, 'margin-left')
    
    driver.quit()

    if len(padding.strip().split(" ")) >= 2:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  return CheckerResult(False, 0, "Lỗi checker")