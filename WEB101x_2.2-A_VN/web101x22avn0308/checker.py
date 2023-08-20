from bs4 import BeautifulSoup, Comment
from dmoj.result import CheckerResult
import re

kitty_ipsum = "Purr jump eat the grass rip the couch scratched sunbathe, shed everywhere rip the couch sleep in the sink fluffy fur catnip scratched."
  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  # criteria 1
  if input == "Có 2 phần tử p":
    if len(soup.find_all("p")) == 2:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Mỗi phần tử p cần có thẻ đóng":
    if soup.p and len(soup.find_all("p")) == source.count("</p>"):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 3
  if input == "Phần tử p thứ 2 có nội dung là đoạn văn kitty ipsum text được cho":
    if len(soup.find_all("p")) < 2:
      return CheckerResult(False, 0, "")
    
    if soup.find_all("p")[1].text == kitty_ipsum:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 4
  if input == "Chỉ có một phần tử main":
    if len(soup.find_all("main")) == 1:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 5
  if input == "Phần tử main có 2 phần tử p là phần tử con":
    if len(soup.find_all("main")) == 1 and len(soup.main.find_all("p")) == 2:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 6
  if input == "Thẻ mở của phần tử main nằm trước thẻ mở của phần tử p thứ nhất":
    if len(soup.find_all("main")) == 1 and len(soup.main.find_all("p")) == 2:
      if re.search(r"<main>[ \n\t\r]*<p>", source):
        return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 7
  if input == "Thẻ đóng của phần tử main nằm sau thẻ đóng của phần tử p thứ 2":
    if len(soup.find_all("main")) == 1 and len(soup.main.find_all("p")) == 2:
      if re.search(r"</p>[ \r\n\t]*</main>", source):
        return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
    
  
  return CheckerResult(False, 0, "Lỗi checker")