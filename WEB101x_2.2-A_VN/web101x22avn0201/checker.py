from bs4 import BeautifulSoup
from dmoj.result import CheckerResult
from dmoj.utils.unicode import utf8text
from dmoj.utils.css_parser import parse_css
  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  h1s = soup.find_all('h1')
  
  if len(h1s) > 1:
    return CheckerResult(False, 0, "Qúa nhiều thẻ h1")
  
  
  if len(h1s) == 0:
    return CheckerResult(False, 0, "Thiếu thẻ h1")
  
  
  h1 = h1s[0]
  
  if h1.text == "Hello World":
    return CheckerResult(True, point_value, "Chính xác")
  else: 
    return CheckerResult(False, 0, "Thẻ h1 có nội dung 'Hello World' (không có dấu nháy đơn)")