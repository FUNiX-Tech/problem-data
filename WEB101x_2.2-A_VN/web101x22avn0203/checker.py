from bs4 import BeautifulSoup
from dmoj.result import CheckerResult
  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  # criteria 1
  if input == 'Có phần tử p hợp lệ':
    if soup.p:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Phần tử p có nội dung Hello Paragraph":
    if soup.p and soup.p.text == 'Hello Paragraph':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 3
  if input == 'Phần tử p có thẻ đóng':
    if len(soup.find_all("p")) == source.count("</p>") and len(soup.find_all("p")) > 0:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
      
  return CheckerResult(False, 0, "Lỗi checker")