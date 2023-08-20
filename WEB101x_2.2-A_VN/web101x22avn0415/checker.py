from bs4 import BeautifulSoup, Comment
from dmoj.result import CheckerResult
from dmoj.utils.unicode import utf8text
from dmoj.utils.css_parser import parse_css, get_element_css_value
import re

black = [
  "#000000",
  "#000",
  "rgb(0,0,0)",
  "rgb(0%,0%,0%)",
  "hsl(0,0%,0%)",
  "hsla(0,0%,0%,1)"
]
  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  css = parse_css(soup)
  
  if css.get("body") is None:
    return CheckerResult(False, 0, "")
  
  color = css.get("body").get("background-color")

  if color is None:
    return CheckerResult(False, 0, "")
  
  color = re.sub(r" !important", "", color)
  color = re.sub(r" +", "", color)

  # criteria 1
  if input == "Thẻ body có background màu đen":
    if color in black:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Bạn phải sử dụng rgb để đặt background màu đen cho thẻ body":
    if color in [ "rgb(0,0,0)","rgb(0%,0%,0%)"]:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  return CheckerResult(False, 0, "Lỗi checker")