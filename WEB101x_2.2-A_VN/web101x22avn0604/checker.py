from bs4 import BeautifulSoup
from dmoj.result import CheckerResult
from dmoj.utils.chrome_driver import get_driver

def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  # criteria 1
  if input == "Class blue-box có margin top 40px":
    if len(soup.find(attrs={"class": "blue-box"})) != 1:
      return CheckerResult(False, 0, "")

    driver = get_driver(source)
    element = driver.find_element_by_class_name("blue-box")
    css = driver.get_computed_style(element, 'margin-top')
    driver.quit()

    if css == '40px':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Class blue-box có margin right 20px":
    if len(soup.find(attrs={"class": "blue-box"})) != 1:
      return CheckerResult(False, 0, "")

    driver = get_driver(source)
    element = driver.find_element_by_class_name("blue-box")
    css = driver.get_computed_style(element, 'margin-right')
    driver.quit()

    if css == '20px':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 3
  if input == "Class blue-box có margin bottom 20px":
    if len(soup.find(attrs={"class": "blue-box"})) != 1:
      return CheckerResult(False, 0, "")

    driver = get_driver(source)
    element = driver.find_element_by_class_name("blue-box")
    css = driver.get_computed_style(element, 'margin-bottom')
    driver.quit()

    if css == '20px':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 4
  if input == "Class blue-box có margin left 40px":
    if len(soup.find(attrs={"class": "blue-box"})) != 1:
      return CheckerResult(False, 0, "")

    driver = get_driver(source)
    element = driver.find_element_by_class_name("blue-box")
    css = driver.get_computed_style(element, 'margin-left')
    driver.quit()

    if css == '40px':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  return CheckerResult(False, 0, "Lỗi checker")