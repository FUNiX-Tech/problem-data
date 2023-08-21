from bs4 import BeautifulSoup
from dmoj.result import CheckerResult
from dmoj.utils.css_parser import parse_css
  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  css = parse_css(soup)

  css_box1 = css.get("#box-1")
  css_box2 = css.get("#box-2")
  
  # criteria 1
  if input == "#box-1 có order là 2":
    if css_box1 and css_box1.get("order") == "2": 
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 2
  if input == "#box-2 có order là 1":
    if css_box2 and css_box2.get("order") == "1": 
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  return CheckerResult(False, 0, "Lỗi checker")