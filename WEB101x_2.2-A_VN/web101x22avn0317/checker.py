from bs4 import BeautifulSoup, Comment
from dmoj.result import CheckerResult
import re
  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  # criteria 1
  if input == "Có 3 phần tử checkbox":
    if len(soup.find_all("input", type="checkbox")) == 3:
      return CheckerResult(True, point_value, "")
    else:
      return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Mỗi checkbox trong 3 checkbox đều nằm trong thẻ label của nó":
    if len(soup.find_all("input", type="checkbox")) != 3:
      return CheckerResult(False, 0, "")

    if len(soup.find_all("label")) != 3:
      return CheckerResult(False, 0, "")

    checkboxes = soup.find_all("input", type="checkbox")

    if all(lambda checkbox: checkbox.parent and checkbox.parent.name == 'label' for checkbox in checkboxes):
      return CheckerResult(True, point_value, "")
    else:
      return CheckerResult(False, 0, "")
  
  # criteria 3
  if input == "Các label phải có thẻ đóng":
    if len(soup.find_all("label")) != 3:
      return CheckerResult(False, 0, "")

    if re.findall(r"</label>", source) != 3:
      return CheckerResult(False, 0, "")
      
    return CheckerResult(True, point_value, "")
  
  # criteria 4
  if input == "Các checkbox có attribute name có giá trị là personality":
    if len(soup.find_all("input", type="checkbox", name="personality")) != 3:
      return CheckerResult(False, 0, "")
    
    return CheckerResult(True, point_value, "")
  
  # criteria 5
  if input == "Mỗi checkbox được nằm trong phần từ form":
    if len(soup.find_all("input", type="checkbox")) != 3:
      return CheckerResult(False, 0, "")
    
    if soup.form and soup.form.find_all("input", type="checkbox") != 3:
      return CheckerResult(True, point_value, "")
    
    return CheckerResult(False, 0, "")
  
  return CheckerResult(False, 0, "Lỗi checker")