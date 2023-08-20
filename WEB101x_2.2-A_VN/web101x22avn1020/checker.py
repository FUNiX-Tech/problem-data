from bs4 import BeautifulSoup, Comment
from dmoj.result import CheckerResult
from dmoj.utils.unicode import utf8text
from dmoj.utils.css_parser import parse_css
  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  css = parse_css(soup)

  item3 = css.get(".item3")

  if not item3:
    return CheckerResult(False, 0, "")
  
  # criteria 1
  if input == "Class item3 có grid-template-columns với giá trị là auto và 1fr":
    if item3.get("grid-template-columns") == 'auto 1fr':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Class item3 có display grid":
    if item3.get("display") == 'grid':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  
  return CheckerResult(False, 0, "Lỗi checker")