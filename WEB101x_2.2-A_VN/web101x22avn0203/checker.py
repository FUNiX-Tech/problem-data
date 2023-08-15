from bs4 import BeautifulSoup
from dmoj.result import CheckerResult
import re
  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  # criteria 1
  if input == 'Code của bạn phải có phần tử p hợp lệ':
    
    ps = soup.find_all("p")
    
    if len(ps) > 1: 
      
      return CheckerResult(False, 0, "Chỉ được tạo 1 thẻ p")
    
    if len(ps) == 0:
      
      return CheckerResult(False, 0, "Thiếu thẻ p")
    
    return CheckerResult(True, point_value, "")
  
  # criteria 2
  if input == "Phần tử p của bạn phải có nội dung 'Hello Paragraph'":
    
    p = soup.find("p")
    
    if p and p.text == 'Hello Paragraph':
      
      return CheckerResult(True, point_value, "")
    
    else:
      
      return CheckerResult(False, 0, "")

  # criteria 3
  if input == 'Phần tử p của bạn phải có thẻ đóng':
    regex = r"(?s)<p>.*</p>"
    
    if re.search(regex, source):
      
      return CheckerResult(True, point_value, "")
    
    else:
      
      return CheckerResult(False, 0, "")
      
  return CheckerResult(False, 0, "Lỗi checker")