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
    return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Mỗi checkbox trong 3 checkbox đều nằm trong thẻ label của nó":
    if soup.label is None or soup.find("input", type="checkbox") is None:
      return CheckerResult(False, 0, "")

    if all(input.parent and input.parent.name == "label" for input in soup.find_all("input", type="checkbox")):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 3
  if input == "Các label phải có thẻ đóng":
    if soup.label and len(soup.find_all("label")) == source.count("</label>"):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 4
  if input == "Các checkbox có attribute name có giá trị là personality":
    checkboxes = len(soup.find_all("input", type="checkbox"))
    personality_checkboxes = len(soup.find_all("input", attrs={"type": "checkbox", "name": "personality"}))
    if personality_checkboxes > 0 and \
      personality_checkboxes == checkboxes:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
    
  
  # criteria 5
  if input == "Mỗi checkbox được nằm trong phần từ form":
    if len(soup.find_all("form")) == 1 and \
    len(soup.find_all("input", type="checkbox")) > 0 and \
      len(soup.find_all("input", type="checkbox")) == len(soup.form.find_all("input", type="checkbox")):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  return CheckerResult(False, 0, "Lỗi checker")