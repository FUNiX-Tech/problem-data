from bs4 import BeautifulSoup, Comment
from dmoj.result import CheckerResult
from dmoj.utils.unicode import utf8text
from dmoj.utils.css_parser import parse_css
import re
  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  css = parse_css(soup)
  
  item5 = css.get("item5")

  if item5 is None:
    return CheckerResult(False, 0, "")


    
  # criteria 1
  if input == "Class item5 có property grid-column":
    if item5.get("grid-column") is not None:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Class item5 có grid-column sao cho nó chiếm 2 cột cuối cùng của grid":
    grid_column = item5.get("grid-column")
    
    if not grid_column:
      return CheckerResult(False, 0, "")
      
      
    if re.fullmatch(r"\s?2\s?/\s?4\s?", grid_column):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  return CheckerResult(False, 0, "Lỗi checker")