from bs4 import BeautifulSoup, Comment
from dmoj.result import CheckerResult
from dmoj.utils.unicode import utf8text
from dmoj.utils.css_parser import parse_css, get_element_css_value
from dmoj.utils.chrome_driver import get_driver
import re

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
  if input == "Class blue-box có padding top 40px":
    driver = get_driver(source)
    
    blue_box = driver.get_element_by_class_name("blue-box")
    
    css = driver.get_computed_style(blue_box, 'padding-top')
    
    driver.quit()

    if css == '40px':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Class blue-box có padding right 20px":
    driver = get_driver(source)
    
    blue_box = driver.get_element_by_class_name("blue-box")
    
    css = driver.get_computed_style(blue_box, 'padding-right')
    
    driver.quit()

    if css == '20px':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 3
  if input == "Class blue-box có padding bottom 20px":
    driver = get_driver(source)
    
    blue_box = driver.get_element_by_class_name("blue-box")
    
    css = driver.get_computed_style(blue_box, 'padding-bottom')
    
    driver.quit()

    if css == '20px':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 4
  if input == "Class blue-box có padding left 40px":
    driver = get_driver(source)
    
    blue_box = driver.get_element_by_class_name("blue-box")
    
    css = driver.get_computed_style(blue_box, 'padding-left')
    
    driver.quit()

    if css == '40px':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 5
  if input == "Sử dụng quy tắc theo chiều kim đồng hồ để set padding cho class blue-box":
    bluebox = soup.find('h5', attrs={'class': 'box blue-box'})
    
    if bluebox is None:
      return CheckerResult(False, 0, "")


    padding = get_element_css_value(soup, bluebox, 'padding')

    if len(padding.strip().split(" ")) >= 2:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  return CheckerResult(False, 0, "Lỗi checker")