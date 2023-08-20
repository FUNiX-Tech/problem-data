from bs4 import BeautifulSoup
from dmoj.result import CheckerResult
import re
  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  # criteria 1
  if input == 'Có 1 phần tử h2':
    h2 = soup.find("h2")
    if h2 is not None:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 2
  if input == 'Phần tử h2 phải có thẻ đóng':
    if len(soup.find_all("h2")) == source.count("</h2>") and len(soup.find_all("h2")) > 0:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 3
  if input == 'Phần tử h2 có nội dung CatPhotoApp':
    if soup.h2 and soup.h2.text == "CatPhotoApp":
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
    
  # criteria 4
  if input == "Phần tử h1 có nội dung Hello World":
    if soup.h1 and soup.h1.text == "Hello World":
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 5
  if input == 'Phần tử h1 nằm trước phần tử h2':
    
    if soup.h1.find_next_sibling("h2"):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  return CheckerResult(False, 0, "Lỗi checker")