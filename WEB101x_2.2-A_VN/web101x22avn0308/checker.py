from bs4 import BeautifulSoup, Comment
from dmoj.result import CheckerResult
import re

kitty_ipsum = "Purr jump eat the grass rip the couch scratched sunbathe, shed everywhere rip the couch sleep in the sink fluffy fur catnip scratched."
  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  # criteria 1
  if input == "Có 2 thẻ p":
    if len(soup.find_all("p")) == 2:
      return CheckerResult(True, point_value, "")
    else:
      return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Mỗi thẻ p cần có thẻ đóng":
    if len(soup.find_all("p")) != 2:
      return CheckerResult(False, 0, "")

    if len(re.findall(r"<p>", source)) == 2 and len(re.findall(r"</p>", source)) == 2:
      return CheckerResult(True, point_value, "")
    
    return CheckerResult(False, 0, "")
  
  # criteria 3
  if input == "Thẻ p thứ 2 có nội dung là đoạn văn kitty ipsum text được cho":
    if len(soup.find_all("p")) != 2:
      return CheckerResult(False, 0, "")
    
    if soup.find_all("p")[1].text == kitty_ipsum:
      return CheckerResult(True, point_value, "")
    
    return CheckerResult(False, 0, "")
      
  
  # criteria 4
  if input == "Chỉ có một thẻ main":
    if len(soup.find_all("main")) == 1:
      return CheckerResult(True, point_value, "")
    else:
      return CheckerResult(False, 0, "")
  
  # criteria 5
  if input == "Thẻ main có 2 thẻ p là thẻ con":
    if len(soup.find_all("main")) != 1 or len(soup.find_all("p")) != 2:
      return CheckerResult(False, 0, "")
    
    ps = soup.find_all("p")
    if ps[0].parent and ps[0].parent.name == "main" and ps[1].parent and ps[1].parent.name == "main":
      return CheckerResult(True, point_value, "")
    else:
      return CheckerResult(False, 0, "")
  
  # criteria 6
  if input == "Thẻ mở của thẻ main nằm trước thẻ mở của thẻ p thứ nhất":
    if soup.p and soup.p.parent and soup.p.parent.namt == "main":
      return CheckerResult(True, point_value, "")
    else:
      return CheckerResult(False, 0, "")
  
  # criteria 7
  if input == "Thẻ đóng của thẻ main nằm sau thẻ đóng của thẻ p thứ 2":
    if len(soup.find_all("main")) != 1 or len(soup.find_all("p")) != 2:
      return CheckerResult(False, 0, "")
    
    ps = soup.find_all("p")
    if \
      ps[0].parent and \
      ps[0].parent.name == "main" and \
      ps[1].parent and \
      ps[1].parent.name == "main" and \
      len(re.findall(r"</p>", source)) == 2 and \
      len(re.findall(r"</main>", source)) == 1:  
        
      return CheckerResult(True, point_value, "")
    else:
      return CheckerResult(False, 0, "")
    
  
  return CheckerResult(False, 0, "Lỗi checker")