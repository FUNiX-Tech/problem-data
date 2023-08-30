from bs4 import BeautifulSoup, Comment
from dmoj.result import CheckerResult
from dmoj.utils.unicode import utf8text
from dmoj.utils.css_parser import parse_css, count_element, get_element_css_value
from dmoj.utils.chrome_driver import get_driver
import re

red = [
"#f00",
]

cyan = [
"#0ff",
]

fuchsia = [
"#f0f",
]

green = [
"#0f0",
]

def structure_changed(soup):
  return \
    len(soup.find_all("h1")) != 4 or \
    len(soup.find_all('h1', string="I am red!", attrs={"class": "red-text"} )) != 1 or \
    len(soup.find_all('h1', string="I am fuchsia!", attrs={"class": "fuchsia-text"} )) != 1 or \
    len(soup.find_all('h1', string="I am cyan!", attrs={"class": "cyan-text"} )) != 1 or \
    len(soup.find_all('h1', string="I am green!", attrs={"class": "green-text"} )) != 1

  
def tidy_color(color):
  color = re.sub(r"!important", "", color)
  color = re.sub(r" +", "", color)
  color = color.lower()
  return color

def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  if structure_changed(soup) is True:
    return CheckerResult(False, 0, "Không thay đổi ")
  
  
  # criteria 1
  if input == "Thẻ h1 có nội dung I am red! có chữ màu đỏ":
    driver = get_driver(source)
    element = driver.find_element_by_class_name("red-text")
    css = "" if element is None else driver.get_computed_style(element, "color")
    driver.quit()   
    if css == "rgb(255, 0, 0)":
      return CheckerResult(True, point_value, "")
      
    return CheckerResult(False, 0, "")
    

  # criteria 2
  if input == "Sử dụng mã hex rút gọn cho màu đỏ (red) thay vì #FF0000":
    h1 = soup.find("h1", string="I am red!")
    color = get_element_css_value(soup, h1, 'color')
    color = tidy_color(color)
    
    if color in red:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 3
  if input == "Thẻ h1 có nội dung I am green! có chữ màu xanh lá (lime)":
    driver = get_driver(source)
    element = driver.find_element_by_class_name("green-text")
    css = "" if element is None else driver.get_computed_style(element, "color")
    driver.quit()   
    if css == "rgb(0, 255, 0)":
      return CheckerResult(True, point_value, "")
      
    return CheckerResult(False, 0, "")
  
  # criteria 4
  if input == "Sử dụng mã hex rút gọn cho màu xanh lá (lime) thay vì #00FF00":
    h1 = soup.find("h1", string="I am green!")
    color = get_element_css_value(soup, h1, 'color')
    color = tidy_color(color)
    
    if color in green:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 5
  if input == "Thẻ h1 có nội dung I am cyan! có chữ màu lục lam (cyan)":
    driver = get_driver(source)
    element = driver.find_element_by_class_name("cyan-text")
    css = "" if element is None else driver.get_computed_style(element, "color")
    driver.quit()   
    if css == "rgb(0, 255, 255)":
      return CheckerResult(True, point_value, "")
      
    return CheckerResult(False, 0, "")

  # criteria 6
  if input == "Sử dụng mã hex rút gọn cho màu lục lam (cyan) thay vì #00FFFF":
    h1 = soup.find("h1", string="I am cyan!")
    color = get_element_css_value(soup, h1, 'color')
    color = tidy_color(color)
    
    if color in cyan:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 7
  if input == "Thẻ h1 có nội dung I am fuchsia! có màu fuchsia":
    driver = get_driver(source)
    element = driver.find_element_by_class_name("fuchsia-text")
    css = "" if element is None else driver.get_computed_style(element, "color")
    driver.quit()   
    if css == "rgb(255, 0, 255)":
      return CheckerResult(True, point_value, "")
      
    return CheckerResult(False, 0, "")

  
  # criteria 8
  if input == "Sử dụng mã hex rút gọn cho màu hoa vân anh (fuchsia) thay vì #FF00FF":
    h1 = soup.find("h1", string="I am fuchsia!")
    color = get_element_css_value(soup, h1, 'color')
    color = tidy_color(color)
    
    if color in fuchsia:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  return CheckerResult(False, 0, "Lỗi checker")