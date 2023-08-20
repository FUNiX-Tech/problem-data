from bs4 import BeautifulSoup, Comment
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
  if input == "Phần tử a liên kết tới https://www.freecatphotoapp.com":
    if soup.find("a", href="https://www.freecatphotoapp.com"):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 3
  if input == "Phần từ a có nội dung cat photos":
    if soup.find("a", string="cat photos"):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 4
  if input == "Tạo 1 phần tử p mới. Có tổng cộng 3 phần tử p trong code của bạn.":
    if len(soup.find_all("p")) == 3:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 5
  if input == "Phần tử a nằm trong phần tử p":
    if len(soup.find_all("a")) == 1 and soup.p and soup.a.parent.name == "p":
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 6
  if input == "Phần tử p có nội dung 'View more ' (không có dấu nháy đơn, lưu ý có một ký tự khoảng trắng phía sau)":
    for p in soup.find_all("p"):
      if p.find("a") and len(p.contents) >= 2 and p.contents[0] == "View more ":
        return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
    
  # criteria 7
  if input == "Phần tử a không có nội dung chữ là View more":
    if soup.find("a", string="View more") or  soup.find("a", string="View more "):
      return CheckerResult(False, 0, "")
    return CheckerResult(True, point_value, "")
  
  # criteria 8
  if input == "Mỗi phần tử p cần có thẻ đóng":
    if soup.a and len(soup.find_all("p")) == source.count("</p>"):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 9
  if input == "Phần tử a phải có thẻ đóng":
    if soup.a and len(soup.find_all("a")) == source.count("</a>"):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  return CheckerResult(False, 0, "Lỗi checker")