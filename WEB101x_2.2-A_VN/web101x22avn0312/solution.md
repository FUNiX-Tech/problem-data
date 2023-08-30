```html
<input type="text" placeholder="cat photo URL" />
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
  if input == "Thêm attribute placeholder cho phần tử input đang có sẵn":
    if soup.find("input", placeholder=True):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Giá trị của placeholder là 'cat photo URL'":
    if soup.find("input", placeholder="cat photo URL"):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 3
  if input == "Phần tử input không có thẻ đóng":
    if soup.input and re.search(r"</input>", source) is None:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 4
  if input == "Phần tử input có cấu trúc đúng":
    if soup.input:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  return CheckerResult(False, 0, "Lỗi checker")
```
