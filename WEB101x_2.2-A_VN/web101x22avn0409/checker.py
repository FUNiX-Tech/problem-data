from bs4 import BeautifulSoup, Comment
from dmoj.result import CheckerResult
from dmoj.utils.css_parser import parse_css
from dmoj.utils.chrome_driver import get_driver
  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  if len(soup.find_all("h2")) != 1:
    return CheckerResult(False, 0, "")
  
  h2 = soup.h2
  
  # criteria 1
  if input == "Phần tử h2 có chữ màu đỏ":
    driver = get_driver(source)
    element = driver.find_element_by_tag_name("h2")
    css = driver.get_computed_style(element, 'color') if element is not None else None
    driver.quit()
    
    if css == "rgb(255, 0, 0)":
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Phần tử h2 có class red-text":
    if h2.get("class") is not None and "red-text" in h2.get("class"):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 3
  if input == "Phần tử style khai báo class red-text với color được đặt là red":
    css = parse_css(soup)
    if css.get(".red-text") and css.get(".red-text").get('color') == "red":
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 4
  if input == "Không khai báo style inline cho phần tử h2, như style='color: red'":
    if h2.get("style") is not None:
      return CheckerResult(False, 0, "")
    return CheckerResult(True, point_value, "")
  
  return CheckerResult(False, 0, "Lỗi checker")