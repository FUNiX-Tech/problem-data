from bs4 import BeautifulSoup
from dmoj.result import CheckerResult
from dmoj.utils.css_parser import parse_css, get_element_css_value
from dmoj.utils.chrome_driver import get_driver
import re

red = [
"#ff0000",
"#f00",
]

green = [
"#00ff00", "#0f0"
]

orange = [
  "#ffa500",
]

dodgerblue = [
  "#1e90ff",
]

def structure_changed(soup):
  print(len(soup.find_all('h1',string= "I am red!", attrs={ "class": "red-text"} )) )
  print(len(soup.find_all('h1',string= "I am orange!",  attrs={"class": "orange-text"} )) )
  print(len(soup.find_all('h1', string= "I am dodger blue!", attrs={"class": "dodger-blue-text"} )) )
  print(len(soup.find_all('h1', string= "I am green!", attrs={"class": "green-text"} )))
    
  return len(soup.find_all("h1")) != 4 or \
    len(soup.find_all('h1',string= "I am red!", attrs={ "class": "red-text"} )) != 1 or \
    len(soup.find_all('h1',string= "I am orange!",  attrs={"class": "orange-text"} )) != 1 or \
    len(soup.find_all('h1', string= "I am dodger blue!", attrs={"class": "dodger-blue-text"} )) != 1 or \
    len(soup.find_all('h1', string= "I am green!", attrs={"class": "green-text"} )) != 1

  
def tidy_color(color):
  color = re.sub(r" !important", "", color)
  color = re.sub(r"[ \r\n\t]+", " ", color)
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
  if input == "Sử dụng mã hex cho màu đỏ thay vì dùng từ red":
    h1 = soup.find("h1", string="I am red!")
    
    color = get_element_css_value(soup, h1, 'color')
    color = tidy_color(color)
    
    if color in red:
      return CheckerResult(True, point_value, "")
      
    return CheckerResult(False, 0, "")
  
  # criteria 3
  if input == "Thẻ h1 có nội dung I am green! có chữ màu xanh lá (green)":
    driver = get_driver(source)
    element = driver.find_element_by_class_name("green-text")
    css = "" if element is None else driver.get_computed_style(element, "color")
    driver.quit()   
    if css == "rgb(0, 255, 0)":
      return CheckerResult(True, point_value, "")
      
    return CheckerResult(False, 0, "")
  
  # criteria 4
  if input == "Sử dụng mã hex cho màu xanh lá thay vì dùng từ green":
    h1 = soup.find("h1", string="I am green!")
    
    color = get_element_css_value(soup, h1, 'color')
    color = tidy_color(color)
    
    if color in green:
      return CheckerResult(True, point_value, "")
      
    return CheckerResult(False, 0, "")
  
  # criteria 5
  if input == "Thẻ h1 có nội dung I am dodger blue! có chữ màu xanh da trời (dodgerblue)":
    driver = get_driver(source)
    element = driver.find_element_by_class_name("dodger-blue-text")
    css = "" if element is None else driver.get_computed_style(element, "color")
    driver.quit()   
    if css == "rgb(30, 144, 255)":
      return CheckerResult(True, point_value, "")
      
    return CheckerResult(False, 0, "")

  # criteria 6
  if input == "Sử dụng mã hex cho màu xanh da trời thay vì dùng từ dodgerblue":
    h1 = soup.find("h1", string="I am dodger blue!")
    
    color = get_element_css_value(soup, h1, 'color')
    color = tidy_color(color)
    
    if color in dodgerblue:
      return CheckerResult(True, point_value, "")
      
    return CheckerResult(False, 0, "")
  
  # criteria 7
  if input == "Thẻ h1 có nội dung I am orange! có màu cam":
    driver = get_driver(source)
    element = driver.find_element_by_class_name("orange-text")
    css = "" if element is None else driver.get_computed_style(element, "color")
    driver.quit()   
    if css == "rgb(255, 165, 0)":
      return CheckerResult(True, point_value, "")
      
    return CheckerResult(False, 0, "")
  
  # criteria 8
  if input == "Sử dụng mã hex cho cam thay vì dùng từ orange":
    h1 = soup.find("h1", string="I am orange!")
    
    color = get_element_css_value(soup, h1, 'color')
    color = tidy_color(color)
    
    if color in orange:
      return CheckerResult(True, point_value, "")
      
    return CheckerResult(False, 0, "")
  
  return CheckerResult(False, 0, "Lỗi checker")