from bs4 import BeautifulSoup, Comment
from dmoj.result import CheckerResult
from dmoj.utils.css_parser import parse_css
import re
  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  # criteria 1
  if input == "Attribute style của thẻ h2 cần được loại bỏ":
  
    if len(soup.find_all("h2")) != 1:
  
      return CheckerResult(False, 0, "")

    if soup.h2.get("style") is None:
  
      return CheckerResult(True, point_value, "")
  
    return CheckerResult(False, 0, "")


  # criteria 2
  if input == "Có một thẻ style":
    
    if len(soup.find_all("style")) == 1:
    
      return CheckerResult(True, point_value, "")

    return CheckerResult(False, 0, "")
  
  # criteria 3
  if input == "Thẻ h2 có màu blue":
    
    if len(soup.find_all("style")) != 1:
    
      return CheckerResult(False, 0, "")

    if len(soup.find_all("h2")) != 1:
  
      return CheckerResult(False, 0, "")
    
    css = parse_css(soup)

    if css.get("h2") and css.get("h2").get("color") == "blue":
      
      return CheckerResult(True, point_value, "")

    return CheckerResult(False, 0, "")
  
  # criteria 4
  if input == "Khai báo stylesheet cho h2 cần hợp lệ với một dấu chấm phẩy và dấu ngoặc nhọn đóng":

    if len(soup.find_all("style")) != 1:
    
      return CheckerResult(False, 0, "")

    style_string = re.sub(r"[\n ]+", " ", soup.style.string).strip()
    
    if re.fullmatch(r"h2\s?\{\s?color\s?:\s?blue\s?;\s?\}", style_string):
      
      return CheckerResult(True, point_value, "")
    
    return CheckerResult(False, 0, "")
  
  # criteria 5
  if input == "Phần tử style cần có thẻ đóng":
    if len(soup.find_all("style")) != 1:
    
      return CheckerResult(False, 0, "")
    
    if re.findall(r"</style>", source) != 1:
      return CheckerResult(False, 0, "")
    
    if source.find("<style>") > source.find("</style>"):
      return CheckerResult(False, 0, "")
    
    return CheckerResult(True, point_value, "")
  
  return CheckerResult(False, 0, "Lỗi checker")