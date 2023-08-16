from bs4 import BeautifulSoup, Comment
from dmoj.result import CheckerResult
from dmoj.utils.unicode import utf8text
from dmoj.utils.css_parser import parse_css
  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  # criteria 1
  if input == "Một trong các radio buttons có value là indoor":
    if soup.find("input", type="radio", value="indoor"):
      return CheckerResult(True, point_value, "")
    else:
      return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Một trong các radio buttons có value là outdoor":
    if soup.find("input", type="radio", value="outdoor"):
      return CheckerResult(True, point_value, "")
    else:
      return CheckerResult(False, 0, "")
  
  # criteria 3
  if input == "Một trong các checkbox có value là loving":
    if soup.find("input", type="checkbox", value="loving"):
      return CheckerResult(True, point_value, "")
    else:
      return CheckerResult(False, 0, "")
  
  # criteria 4
  if input == "Một trong các checkbox có value là lazy":
    if soup.find("input", type="checkbox", value="lazy"):
      return CheckerResult(True, point_value, "")
    else:
      return CheckerResult(False, 0, "")
  
  # criteria 5
  if input == "Một trong các checkbox có value là energetic":
    if soup.find("input", type="checkbox", value="energetic"):
      return CheckerResult(True, point_value, "")
    else:
      return CheckerResult(False, 0, "")
  
  return CheckerResult(False, 0, "Lỗi checker")