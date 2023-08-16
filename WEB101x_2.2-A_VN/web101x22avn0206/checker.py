from bs4 import BeautifulSoup, Comment
from dmoj.result import CheckerResult
import re
  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  # criteria 1
  if input == "Phần tử h1 cần được hiển thị trên trang bằng cách bỏ comment của nó.":
    
    if soup.h1:
      
      return CheckerResult(True, point_value, "")

    else: 
      
      return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Phần tử h2 cần được hiển thị trên trang bằng cách bỏ comment của nó.":
    
    if soup.h2:
      
      return CheckerResult(True, point_value, "")

    else: 
      
      return CheckerResult(False, 0, "")
  
  # criteria 3
  if input == "Phần tử p cần được hiển thị trên trang bằng cách bỏ comment của nó.":
    
    if soup.p:
      
      return CheckerResult(True, point_value, "")

    else: 
      
      return CheckerResult(False, 0, "")
  
  # criteria 4
  if input == "Thẻ đóng của comment không được hiển thị trên trang (i.e. -->).":
    text = soup.get_text()

    if re.search(r"-->", text):
      
      return CheckerResult(False, 0, "")
      
    else:
      
      return CheckerResult(True, point_value, "")
  
  return CheckerResult(False, 0, "Lỗi checker")