from bs4 import BeautifulSoup, Comment
from dmoj.result import CheckerResult
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
  if input == "Class blue-box có padding top là 40px":
    driver = get_driver(source)
    
    blue_box = driver.get_element_by_class_name("blue-box")
    
    padding_top = driver.get_computed_style(blue_box, 'padding-top')
    
    driver.quit()

    if padding_top == '40px':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Class blue-box có padding-right là 20px":
    driver = get_driver(source)
    
    blue_box = driver.get_element_by_class_name("blue-box")
    
    padding_right = driver.get_computed_style(blue_box, 'padding-right')
    
    driver.quit()

    if padding_right == '20px':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 3
  if input == "Class blue-box có padding bottom là 20px":
    driver = get_driver(source)
    
    blue_box = driver.get_element_by_class_name("blue-box")
    
    padding_bottom = driver.get_computed_style(blue_box, 'padding-bottom')
    
    driver.quit()

    if padding_bottom == '20px':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 4
  if input == "Class blue-box có padding left là 40px":
    driver = get_driver(source)
    
    blue_box = driver.get_element_by_class_name("blue-box")
    
    padding_left = driver.get_computed_style(blue_box, 'padding-left')
    
    driver.quit()

    if padding_left == '40px':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  return CheckerResult(False, 0, "Lỗi checker")