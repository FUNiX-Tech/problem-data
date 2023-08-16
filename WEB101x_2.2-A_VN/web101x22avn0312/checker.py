from bs4 import BeautifulSoup, Comment
from dmoj.result import CheckerResult
import re  

def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  # criteria 1
  if input == "Thêm attribute placeholder cho thẻ input đang có sẵn":
    if len(soup.find_all("input")) == 1 and soup.input.get("placeholder") is not None:
      return CheckerResult(True, point_value, "")
    else:
      return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Giá trị của placeholder là 'cat photo URL'":
    if len(soup.find_all("input")) == 1 and soup.input.get("placeholder") == "cat photo URL":
      return CheckerResult(True, point_value, "")
    else:
      return CheckerResult(False, 0, "")
  
  # criteria 3
  if input == "Thẻ input không có thẻ đóng":
    if len(soup.find_all("input")) == 1 and re.search(r"</input>", source) is None:
      return CheckerResult(True, point_value, "")
    else:
      return CheckerResult(False, 0, "")
  
  # criteria 4
  if input == "Thẻ input có cấu trúc đúng":
    if soup.input is not None:
      return CheckerResult(True, point_value, "")
    else:
      return CheckerResult(False, 0, "")
  
  return CheckerResult(False, 0, "Lỗi checker")