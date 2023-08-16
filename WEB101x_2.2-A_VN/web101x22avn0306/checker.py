from bs4 import BeautifulSoup, Comment
from dmoj.result import CheckerResult
import re
  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  # criteria 1
  if input == "Thẻ img phải nằm trong thẻ a":
    
    if len(soup.find_all("a")) != 1 or len(soup.find_all("img")) != 1:
      
      return CheckerResult(False, 0, "")
    
    
    if soup.img.parent.name != "a":
      
      return CheckerResult(False, 0, "")
    
    return CheckerResult(True, point_value, "")

  # criteria 2
  if input == "Thẻ a phải là dead link với href là #":

    if len(soup.find_all("a")) != 1:
      
      return CheckerResult(False, 0, "")

    if soup.a.get("href") != "#":
      
      return CheckerResult(False, 0, "")
    
    return CheckerResult(True, point_value, "")
  
  # criteria 3
  if input == "Mỗi thẻ a phải có thẻ đóng":
    if len(soup.find_all("a")) != 1:
      
      return CheckerResult(False, 0, "")
    
    if re.search(r"</a>", source) is None:
      
      return CheckerResult(False, 0, "")
  
    return CheckerResult(True, point_value, "")
  
  return CheckerResult(False, 0, "Lỗi checker")