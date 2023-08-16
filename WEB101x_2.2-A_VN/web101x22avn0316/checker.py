from bs4 import BeautifulSoup, Comment
from dmoj.result import CheckerResult
import re
  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  # criteria 1
  if input == "Có 2 radio button":
    if len(soup.find_all("input", type="radio")) == 2:
      return CheckerResult(True, point_value, "")
    else:
      return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Các radio button có attribute name có giá trị là indoor-outdoor":
    if len(soup.find_all("input", type="radio", name="indoor-outdoor")) == 2:
      return CheckerResult(True, point_value, "")
    else:
      return CheckerResult(False, 0, "")
      
  # criteria 3
  if input == "Mỗi radio button cần nằm trong một label":
    if len(soup.find_all("input", type="radio")) != 2:
      return CheckerResult(False, 0, "")
    
    if len(soup.find_all("label")) != 2:
      return CheckerResult(False, 0, "")
    
    inputs = soup.find_all("input", type="radio")
    
    if inputs[0].parent and inputs[0].parent.name == 'label' and inputs[1].parent and inputs[1].parent.name == 'label':
      return CheckerResult(True, point_value, "")
    
    return CheckerResult(False, 0, "")
  
  # criteria 4
  if input == "Mỗi phần tử label cần có thẻ đóng":
    if len(soup.find_all("label")) != 2:
      return CheckerResult(False, 0, "")

    if re.findall(r"</label>", source) != 2:
      return CheckerResult(False, 0, "")
    
    return CheckerResult(True, point_value, "")
  
  # criteria 5
  if input == "Một radio button có label indoor":
    correct = False
    labels = soup.find_all("label")

    for label in labels:
      if "indoor" in label.contents:
        correct = True
        
    if correct:
      return CheckerResult(True, point_value, "")
    else:
      return CheckerResult(False, 0, "")
  
  # criteria 6
  if input == "Một radio button có label là outdoor":
    correct = False
    labels = soup.find_all("label")

    for label in labels:
      if "outdoor" in label.contents:
        correct = True
        
    if correct:
      return CheckerResult(True, point_value, "")
    else:
      return CheckerResult(False, 0, "")
  
  # criteria 7
  if input == "Các label cần nằm trong thẻ form":
    if len(soup.find_all("label")) != 2:
      return CheckerResult(False, 0, "")
    
    labels = soup.find_all("label")
    if labels[0].parent and labels[0].parent.name == "form"  and labels[1].parent and labels[1].parent.name == "form":
      return CheckerResult(True, point_value, "")
      
    return CheckerResult(False, 0, "")
  
  return CheckerResult(False, 0, "Lỗi checker")