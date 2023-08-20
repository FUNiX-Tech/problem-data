from bs4 import BeautifulSoup
from dmoj.result import CheckerResult
  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  # criteria 1
  if input == "Chỉ có một phần tử a":
    if len(soup.find_all("a")) == 1:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Chỉ có một phần tử  footer":
    if len(soup.find_all("footer")) == 1:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 3
  if input == "Phần tử a có attribute href với giá trị là #footer":
    if soup.find("a", href="#footer"):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 4
  if input == "Phần tử a không có attribute target":
    if soup.find("a", target=True) is None:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 5
  if input == "Nội dung phần tử a là Jump to Bottom":
    if soup.find("a", string="Jump to Bottom"):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 6
  if input == "Phần tử footer có id là footer":
    if soup.find("footer", id="footer"):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  return CheckerResult(False, 0, "Lỗi checker")