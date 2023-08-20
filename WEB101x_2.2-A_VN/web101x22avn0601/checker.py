from bs4 import BeautifulSoup, Comment
from dmoj.result import CheckerResult
from dmoj.utils.css_parser import parse_css
  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  css = parse_css(soup)

  if css.get(".blue-box") and css.get(".blue-box").get("padding") == '20px':
    return CheckerResult(True, point_value, "")
    
  
  return CheckerResult(False, 0, "Lỗi checker")