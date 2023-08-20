from bs4 import BeautifulSoup, Comment
from dmoj.result import CheckerResult
from dmoj.utils.unicode import utf8text
from dmoj.utils.css_parser import parse_css, get_element_css_value
from dmoj.utils.chrome_driver import get_driver
  
def structure_changed(soup):
  return soup.find_all("div", attrs={"class": "follow-button"}) != 1 or \
        soup.find_all("header") != 1 or \
        soup.find_all("footer") != 1 or

  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  if structure_changed(soup):
    return CheckerResult(False, 0, "")
  
  # criteria 1
  if input == ".follow-btn được hiển thị trên trang. Đảm bảm rằng đã tắt các tiện ích mở rộng như ad blockers":
    
    return CheckerResult(True, point_value, "")
  
  # criteria 2
  if input == "header có flex-direction là row":
    
    driver = get_driver(source)
    
    element = driver.get_element_by_tag_name("header")
    
    css = driver.get_computed_style(element, 'flex-direction')
    
    driver.quit()

    if css == 'row':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 3
  if input == "footer có flex-direction là row":
    
    driver = get_driver(source)
    
    element = driver.get_element_by_tag_name("footer")
    
    css = driver.get_computed_style(element, 'flex-direction')
    
    driver.quit()

    if css == 'row':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  return CheckerResult(False, 0, "Lỗi checker")