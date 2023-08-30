```html
<form action="https://www.freecatphotoapp.com/submit-cat-photo">
  <input type="text" placeholder="cat photo URL" required />
  <button type="submit">Submit</button>

  <label>indoor<input type="radio" name="indoor-outdoor" /></label>
  <label>outdoor<input type="radio" name="indoor-outdoor" /></label>
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
  if input == "Có 2 radio button":
    if len(soup.find_all("input", type="radio")) == 2:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Các radio button có attribute name có giá trị là indoor-outdoor":
    if len(soup.find_all("input", attrs={"type": "radio", "name": "indoor-outdoor"})) == 2:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 3
  if input == "Mỗi radio button cần nằm trong một label":
    correct = True

    if soup.label is None:
      return CheckerResult(False, 0, "")

    if len(soup.find_all("label")) != len(soup.find_all("input", type="radio")):
      return CheckerResult(False, 0, "")

    for label in soup.find_all("label"):
      if label.find("input", type="radio") is None:
        return CheckerResult(False, 0, "")

    return CheckerResult(True, point_value, "")


  # criteria 4
  if input == "Mỗi phần tử label cần có thẻ đóng":
    if soup.label and len(soup.find_all("label")) == source.count("</label>"):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 5
  if input == "Một radio button có label indoor":
    correct = False
    labels = soup.find_all("label")

    for label in labels:
      if "indoor" in label.contents:
        correct = True

    if correct:
      return CheckerResult(True, point_value, "")
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
    return CheckerResult(False, 0, "")

  # criteria 7
  if input == "Các label cần nằm trong phần tử form":
    if len(soup.find_all("form")) != 1:
      return CheckerResult(False, 0, "")

    if soup.label and len(soup.find_all("label")) == len(soup.form.find_all("label")):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  return CheckerResult(False, 0, "Lỗi checker")
```
