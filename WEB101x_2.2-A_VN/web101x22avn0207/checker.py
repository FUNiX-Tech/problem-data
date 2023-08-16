from bs4 import BeautifulSoup, Comment
from dmoj.result import CheckerResult
import re
  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  # criteria 1
  if input == "Tạo phần tử ul":
    if soup.ul:
      return CheckerResult(True, point_value, "")
    else:
      return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Tạo 3 phần tử li trong phần tử ul vừa tạo":
    ul = soup.ul

    if not ul:
      return CheckerResult(False, 0, "")

    
    lis = ul.find_next_siblings("li")

    if len(lis) != 3:
      return CheckerResult(False, 0, "")
    else: 
       return CheckerResult(True, point_value, "")
  
  # criteria 3
  if input == "Phần tử ul cần có thẻ đóng":
    ul = soup.ul

    if not ul:
      return CheckerResult(False, 0, "")
  
    regex = r"(?s)<ul>.*</ul>"

    if re.search(regex, source):
      return CheckerResult(True, point_value, "")
    else: 
      return CheckerResult(False, 0, "")

  # criteria 4
  if input == "Phần tử li cần có thẻ đóng":
    regex = r"(?s).*(<li>.*</li>)+.*"
    
    
  # criteria 5
  if input == "":
    return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  return CheckerResult(False, 0, "Lỗi checker")