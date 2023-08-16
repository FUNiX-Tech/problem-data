from bs4 import BeautifulSoup, Comment
from dmoj.result import CheckerResult
import re
  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  # criteria 1
  if input == "Chỉ có một thẻ a":

    if len(soup.find_all("a")) == 1:

      return CheckerResult(True, point_value, "")
    
    else:
      
      return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Thẻ a liên kết tới https://www.freecatphotoapp.com":
    if len(soup.find_all("a")) == 1:

      return CheckerResult(True, point_value, "")

    if soup.a.get("href") == "https://www.freecatphotoapp.com":
    
      return CheckerResult(True, point_value, "")

    else:

      return CheckerResult(False, 0, "")
  
  # criteria 3
  if input == "Thẻ a có nội dung chữ cat photos":
    if len(soup.find_all("a")) == 1:

      return CheckerResult(True, point_value, "")

    if soup.a.text == "cat photos":
    
      return CheckerResult(True, point_value, "")

    else:

      return CheckerResult(False, 0, "")
  
  # criteria 4
  if input == "Tạo một thẻ p mới. Có tổng cộng 3 thẻ p trong code của bạn.":
    if len(soup.find_all("p")) == 3:

      return CheckerResult(True, point_value, "")
    
    else:
      
      return CheckerResult(False, 0, "")
  
  # criteria 5
  if input == "Thẻ a nằm trong thẻ p":
    if len(soup.find_all("a")) != 1:

      return CheckerResult(False, 0, "")
    
    if len(soup.find_all("p")) != 3:

      return CheckerResult(False, 0, "")

    if soup.a.parent.name == "p":
      
      return CheckerResult(True, point_value, "")
    
    else:
      
      return CheckerResult(False, 0, "")
  
  # criteria 6
  if input == "Thẻ p có nội dung chữ 'View more ' (không có dấu nháy đơn, lưu ý có một ký tự khoảng trắng phía sau)":
    if len(soup.find_all("p")) != 3:

      return CheckerResult(False, 0, "")
    
    ps = soup.find_all('p')

    correct = False
    
    for p in ps:
      
      if len(p.contents) > 0 and p.contents[0] == "View more ":
        
        correct = True

    if correct:
      
      return CheckerResult(True, point_value, "")
    
    else:
      
      return CheckerResult(False, 0, "")
      
    
  # criteria 7
  if input == "Thẻ a không có nội dung chữ là View more":
    if len(soup.find_all("a")) != 1:

      return CheckerResult(False, 0, "")
    
    if soup.a.text == "View more":
      
      return CheckerResult(False, 0, "")
    
    else:
      
      return CheckerResult(True, point_value, "")
  
  # criteria 8
  if input == "Mỗi thẻ p cần có thẻ đóng":
    if len(soup.find_all("p") > 0) and len(re.findall(r"<p>", source)) == len(re.findall(r"</p>")):
      
      return CheckerResult(True, point_value, "")
      
    else:
      
      return CheckerResult(False, 0, "")
  
  # criteria 9
  if input == "Thẻ a phải có thẻ đóng":
    if len(soup.find_all("a")) != 1:

      return CheckerResult(False, 0, "")
    
    if re.search(r"</a>") is None:
      
      return CheckerResult(True, point_value, "")
      
    else:
      
      return CheckerResult(False, 0, "")
  
  return CheckerResult(False, 0, "Lỗi checker")