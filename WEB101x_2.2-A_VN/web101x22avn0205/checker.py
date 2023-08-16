from bs4 import BeautifulSoup, Comment
from dmoj.result import CheckerResult
from dmoj.utils.unicode import utf8text
from dmoj.utils.css_parser import parse_css
  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  # criteria 1
  if input == "":
    return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 2
  if input == "":
    return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 3
  if input == "":
    return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 4
  if input == "":
    return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 5
  if input == "Thứ tự của h1, h2, p không thay đổi.":
    ps = soup.find_all("p")
    h1s = soup.find_all("h1")
    h2s = soup.find_all("h2")
    
    if len(ps) != 1 or len(h1s) != 1 or len(h2s) != 1:
      return CheckerResult(False, 0, "")
    
    if soup.h1.find_next_sibling("h2") is None or soup.h2.find_next_sibling("p") is None:
      return CheckerResult(False, 0, "")
    
    return CheckerResult(True, point_value, "")
      
  return CheckerResult(False, 0, "Lỗi checker")