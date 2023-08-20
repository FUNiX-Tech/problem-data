from bs4 import BeautifulSoup, Comment
from dmoj.result import CheckerResult
from dmoj.utils.unicode import utf8text
from dmoj.utils.css_parser import parse_css, get_element_css_value
  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')

  if len(soup.find_all("h1")) != 1:
    return CheckerResult(False, 0, "")
  
  h1 = soup.h1
  
  # criteria 1
  if input == "Tạo 1 thẻ h1":
    return CheckerResult(True, point_value, "")

  # criteria 2
  if input == "Thẻ h1 có nội dung Hello World":
    if h1.text == 'Hello World':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 3
  if input == "Thẻ h1 có thẻ đóng":
    if source.count("</h1>") == 1:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 4
  if input == "Thẻ body có color là green":
    css = parse_css(soup)

    if css.get("body") is not None and css.get("body").get("color") == "green":
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 5
  if input == "Thẻ body có font-family là monospace":
    css = parse_css(soup)

    if css.get("body") is not None and css.get("body").get("font-family") == "monospace":
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 6
  if input == "Thẻ h1 thừa kế font monospace từ thẻ body":
    if get_element_css_value(soup, h1, 'font-family') == '':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 7
  if input == "Thẻ h1 thừa kế màu chữ là màu xanh (green) từ thẻ body":
    if get_element_css_value(soup, h1, 'color') == '':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  return CheckerResult(False, 0, "Lỗi checker")