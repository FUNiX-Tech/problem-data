from bs4 import BeautifulSoup
from dmoj.result import CheckerResult
from dmoj.utils.css_parser import parse_css, parse_inline_css
from dmoj.utils.chrome_driver import get_driver
  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  # criteria 1
  if input == "Thẻ h1 có class pink-text":
    if soup.find("h1", attrs={"class": "pink-text"}):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Thẻ h1 có class blue-text":
    if soup.find("h1", attrs={"class": "blue-text"}):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 3
  if input == "Thẻ h1 có id orange-text":
    if soup.find("h1", attrs={"id": "orange-text"}):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 4
  if input == "Thẻ h1 có inline style là color: white":
    if len(soup.find_all("h1")) == 1 and soup.h1.get("style") is not None and parse_inline_css(soup.h1).get('color') == 'white':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 5
  if input == "Khai báo class pink-text cần có !important để ghi đè tất cả các khai báo khác":
    css = parse_css(soup)

    if css.get(".pink-text") and css.get(".pink-text").get("color") and " !important" in css.get(".pink-text").get("color"):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 6
  if input == "Thẻ h1 có chữ màu hồng (pink)":
    if len(soup.find_all("h1")) != 1:
      return CheckerResult(False, 0, "")
    
    driver = get_driver(source)

    element = driver.find_element_by_tag_name("h1")

    css = "" if element is None else driver.get_computed_style(element, 'color')

    driver.quit()
    
    if css == "rgb(255, 192, 203)":
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  return CheckerResult(False, 0, "Lỗi checker")