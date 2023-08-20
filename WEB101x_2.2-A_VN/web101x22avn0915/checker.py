from bs4 import BeautifulSoup, Comment
from dmoj.result import CheckerResult
from dmoj.utils.unicode import utf8text
from dmoj.utils.css_parser import parse_css

  
def structure_changed(soup):
  return soup.find_all("div", id="box-1") != 1 or \
        soup.find_all("div", id="box-2") != 1 
  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  if structure_changed(soup):
    return CheckerResult(False, 0, "")
  
  css = parse_css(soup)

  css_box1 = css.get("#box-1")
  css_box2 = css.get("#box-2")
  
  # criteria 1
  if input == "#box-1 có property flex-basis":
    if css_box1 and css_box1.get("flex-basis") is not None: 
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 2
  if input == "#box-1 có flex-basis là 10em":
    if css_box1 and css_box1.get("flex-basis") == "10em": 
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 3
  if input == "#box-2 có property flex-basis":
    if css_box2 and css_box2.get("flex-basis") is not None: 
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 4
  if input == "#box-2 có flex-basis là 20em":
    if css_box2 and css_box2.get("flex-basis") == "20em": 
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  return CheckerResult(False, 0, "Lỗi checker")