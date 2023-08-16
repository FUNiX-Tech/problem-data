from bs4 import BeautifulSoup, Comment
from dmoj.result import CheckerResult
  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  # criteria 1
  if input == "Trang web phải có một phần tử image.":
    if soup.img:
      return CheckerResult(True, point_value, "")
    else:
      return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Phần tử image cần có attribute src trỏ tới ảnh mèo.":
    img = soup.img

    if img and img.get('src') == "https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg":
      return CheckerResult(True, point_value, "")
  else:
    return CheckerResult(False, 0, "")
  
  # criteria 3
  if input == "Attribute alt của phần tử hình ảnh không được trống.":
    img = soup.img
    if img and img.get("alt"):
      return CheckerResult(True, point_value, "")
    else:
      return CheckerResult(False, 0, "")
  
  return CheckerResult(False, 0, "Lỗi checker")