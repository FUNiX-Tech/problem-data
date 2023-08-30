from bs4 import BeautifulSoup
from dmoj.result import CheckerResult
  
h1_str = "<h1>Hello World</h1>"
h2_str = "<h2>CatPhotoApp</h2>"
p_str = "<p>Kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching attack your ankles chase the red dot, hairball run catnip eat the grass sniff.</p>"

def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  # structure change
  if not h1_str in source: 
    return CheckerResult(False, 0, "")

  if not h2_str in source: 
    return CheckerResult(False, 0, "")
  
  if not p_str in source: 
    return CheckerResult(False, 0, "")
  
  
  # criteria 1
  if input == "Phần tử h1 cần được comment để nó không được hiển thị trên trang web":
    if soup.h1 is None:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Phần tử h2 không bị comment để nó có thể được hiển thị trên trang web":
    if soup.h2:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 3
  if input == "Phần tử p được comment để nó không được hiển thị trên trang web":
    if soup.p is None:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 4
  if input == "Mỗi comment của bạn cần được kết thúc bởi -->":
    if source.count("<!--") > 0 and source.count("<!--") == source.count("-->"): 
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 5
  if input == "Thứ tự của h1, h2, p không thay đổi":
    def get_index(substring):
      try:
        position = source.index(substring)
        return position
      except:
        return -1
      
    if get_index(p_str) > get_index(h2_str) and get_index(h2_str) > get_index(h1_str) and get_index(h1_str) >= 0:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
      
  return CheckerResult(False, 0, "Lỗi checker")