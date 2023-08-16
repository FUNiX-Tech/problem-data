from bs4 import BeautifulSoup, Comment
from dmoj.result import CheckerResult
import re
  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  # criteria 1
  if input == "Thẻ input đang có sẵn nằm trong thẻ form":
    if len(soup.find_all("form")) == 1 and len(soup.find_all("input")) == 1 and soup.input.parent and soup.input.parent.name == 'form':
      return CheckerResult(True, point_value, "")
    else:
      return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Thẻ form có attribute action có giá trị là https://www.freecatphotoapp.com/submit-cat-photo":
    if len(soup.find_all("form")) == 1 and soup.form.get("action") == "https://www.freecatphotoapp.com/submit-cat-photo":
      return CheckerResult(True, point_value, "")
    else:
      return CheckerResult(False, 0, "")
  
  # criteria 3
  if input == "Form cần có thẻ đóng":
    if len(soup.find_all("form")) == 1 and len(re.findall(r"</form>", source)) == 1:
      return CheckerResult(True, point_value, "")
    else:
      return CheckerResult(False, 0, "")
  
  
  return CheckerResult(False, 0, "Lỗi checker")