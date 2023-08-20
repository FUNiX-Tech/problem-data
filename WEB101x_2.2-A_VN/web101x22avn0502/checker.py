from bs4 import BeautifulSoup, Comment
from dmoj.result import CheckerResult
from dmoj.utils.unicode import utf8text
from dmoj.utils.css_parser import parse_css, get_element_css_value
  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  if len(soup.find_all('h1')) != 1:
    return CheckerResult(False, 0, "")
  
  h1 = soup.h1
  
  # criteria 1
  if input == "Thẻ h1 có class pink-text":
    if "pink-text" in h1.get("class"):
      return CheckerResult(True, point_value, "")

    return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Thẻ <style> có pink-text CSS class dùng để đổi màu chữ":
    css = parse_css(soup)

    if css.get(".pink-text") and css.get(".pink-text").get("color") == "pink":
      return CheckerResult(True, point_value, "")
    
    return CheckerResult(False, 0, "")
  
  # criteria 3
  if input == "Thẻ h1 có chữ màu hồng (pink)":
    color = get_element_css_value(soup, h1, "color")
    if color and color.lower() in ["pink", "pink !important"]:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  

  return CheckerResult(False, 0, "Lỗi checker")