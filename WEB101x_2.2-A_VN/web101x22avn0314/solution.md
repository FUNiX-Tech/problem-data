```html
<form action="https://www.freecatphotoapp.com/submit-cat-photo">
  <button type="submit">Submit</button>
  <input type="text" placeholder="cat photo URL" />
</form>
```

```python
from bs4 import BeautifulSoup, Comment
from dmoj.result import CheckerResult
import re

def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()

  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')

  # criteria 1
  if input == "Có một button ở trong phần tử form":
    if soup.form and soup.form.find("button"):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Submit button có attribute type có giá trị là submit":
    if soup.find("button", type="submit"):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 3
  if input == "Submit button có nội dung chữ là Submit":
    if soup.find("button", string="Submit"):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 4
  if input == "Button cần có thẻ đóng":
    if soup.button and len(soup.find_all("button")) == source.count("</button>"):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  return CheckerResult(False, 0, "Lỗi checker")
```
