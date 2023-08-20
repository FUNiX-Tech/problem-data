from bs4 import BeautifulSoup, Comment
from dmoj.result import CheckerResult
from dmoj.utils.unicode import utf8text
from dmoj.utils.css_parser import parse_css, count_element, get_element_css_value
from dmoj.utils.chrome_driver import get_driver
  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  # criteria 1
  if input == "Chữ của h4 phải được viết hoa toàn bộ":
    if count_element(soup, "h4") != 1:
      return CheckerResult(False, 0, "")
    
    driver = get_driver(source)
    
    element = driver.find_element_by_tag_name("h4")

    css = driver.get_computed_style(element, 'text-transform') if element is not None else None

    driver.quit()
    
    if css == "uppercase":
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Nội dung chữ ban đầu của h4 không bị thay đổi":
    if count_element(soup, "h4") != 1:
      return CheckerResult(False, 0, "")

    if soup.h4.text == "Alphabet":
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  return CheckerResult(False, 0, "Lỗi checker")