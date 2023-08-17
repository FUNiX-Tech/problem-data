from bs4 import BeautifulSoup, Comment
from dmoj.result import CheckerResult

  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  # criteria 1
  if input == "Radio button đầu tiên mặc định được check ":
    
    radio = soup.find("input", type="radio")

    if radio and radio.get("checked") == "":

      return CheckerResult(True, point_value, "")

    return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Checkbox đầu tiên của form được check theo mặc định":

    form = soup.form

    if form is None: 
      
      return CheckerResult(False, 0, "")
      
    checkbox = form.find("input", type="checkbox")

    if checkbox and checkbox.get("checked") == "":

      return CheckerResult(True, point_value, "")

    return CheckerResult(False, 0, "")
  
  # criteria 3
  if input == "Không thay đổi text của label Indoor":
    label = soup.find("label",attrs={"for": "indoor"})
    if label and label.contents[1] == " Indoor":
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 4
  if input == "Không thay đổi text của label Loving":
    label = soup.find("label",attrs={"for": "loving"})
    if label and label.contents[1] == " Loving":
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  return CheckerResult(False, 0, "Lỗi checker")