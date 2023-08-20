from bs4 import BeautifulSoup, Comment
from dmoj.result import CheckerResult
from dmoj.utils.unicode import utf8text
from dmoj.utils.css_parser import parse_css, get_element_css_value
  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  if len(soup.find_all("style")) != 1:
    return CheckerResult(False, 0, "")
  
  if len(soup.find_all("h1")) != 1:
    return CheckerResult(False, 0, "")
  
  h1 = soup.h1
  
  # criteria 1
  if input == "Thẻ h1 có class pink-text":
    if h1.get("class") is not None and "pink-text" in h1.get("class"):
      return CheckerResult(True, point_value, "")

    return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Thẻ h1 có class blue-text":
    if h1.get("class") is not None and "blue-text" in h1.get("class"):
      return CheckerResult(True, point_value, "")
      
    return CheckerResult(False, 0, "")
  
  # criteria 3
  if input == "Class blue-text và class pink-text đều thuộc về thẻ h1":
    if h1.get("class") is not None and "blue-text" in h1.get("class") and "pink-text" in h1.get("class"):
      return CheckerResult(True, point_value, "")
      
    return CheckerResult(False, 0, "")
  
  # criteria 4
  if input == "Thẻ h1 có chữ màu xanh (blue)":
    if get_element_css_value(soup, h1, "color") == "blue":
      return CheckerResult(True, point_value, "")
      
    return CheckerResult(False, 0, "")
  
  return CheckerResult(False, 0, "Lỗi checker")