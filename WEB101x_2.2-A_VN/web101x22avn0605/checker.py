from bs4 import BeautifulSoup
from dmoj.result import CheckerResult
from dmoj.utils.chrome_driver import get_driver
from dmoj.utils.css_parser import parse_css

def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  # criteria 1
  if input == "Class blue-box có padding top 40px":
    if len(soup.find(attrs={"class": "blue-box"})) != 1:
      return CheckerResult(False, 0, "")

    driver = get_driver(source)
    element = driver.find_element_by_class_name("blue-box")
    css = driver.get_computed_style(element, 'padding-top')
    driver.quit()

    if css == '40px':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Class blue-box có padding right 20px":
    if len(soup.find(attrs={"class": "blue-box"})) != 1:
      return CheckerResult(False, 0, "")

    driver = get_driver(source)
    element = driver.find_element_by_class_name("blue-box")
    css = driver.get_computed_style(element, 'padding-right')
    driver.quit()

    if css == '20px':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 3
  if input == "Class blue-box có padding bottom 20px":
    if len(soup.find(attrs={"class": "blue-box"})) != 1:
      return CheckerResult(False, 0, "")

    driver = get_driver(source)
    element = driver.find_element_by_class_name("blue-box")
    css = driver.get_computed_style(element, 'padding-bottom')
    driver.quit()

    if css == '20px':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 4
  if input == "Class blue-box có padding left 40px":
    if len(soup.find(attrs={"class": "blue-box"})) != 1:
      return CheckerResult(False, 0, "")

    driver = get_driver(source)
    element = driver.find_element_by_class_name("blue-box")
    css = driver.get_computed_style(element, 'padding-left')
    driver.quit()

    if css == '40px':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 5
  if input == "Sử dụng quy tắc theo chiều kim đồng hồ để set padding cho class blue-box":
    css = parse_css(soup)
    
    if css.get(".blue-box") and css.get(".blue-box").get("padding") in ["40px 20px 20px 40px", "40px 20px 20px 40px !important"]:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  return CheckerResult(False, 0, "Lỗi checker")