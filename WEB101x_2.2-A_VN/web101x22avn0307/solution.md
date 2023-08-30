```html
<!DOCTYPE html>
<html>
  <head>
    <title></title>
  </head>

  <body>
    <h1></h1>
    <p></p>
  </body>
</html>
```

```python
from bs4 import BeautifulSoup, Comment
from dmoj.result import CheckerResult
from dmoj.utils.unicode import utf8text
from dmoj.utils.css_parser import parse_css

def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()

  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')

  # criteria 1
  if input == "Chỉ có duy nhất một phần tử head":
    if len(soup.find_all("head")) == 1:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Chỉ có duy nhất một phần tử body":
    if len(soup.find_all("body")) == 1:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 3
  if input == "Phần tử head là con của phần tử html":
    if len(soup.find_all("head")) != 1 or len(soup.find_all("html")) != 1:
      return CheckerResult(False, 0, "")

    if soup.head.parent and soup.head.parent.name == "html":
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 4
  if input == "Phần tử body là con của phần tử html":
    if len(soup.find_all("body")) != 1 or len(soup.find_all("html")) != 1:
      return CheckerResult(False, 0, "")

    if soup.body.parent and soup.body.parent.name == "html":
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 5
  if input == "Phần tử head bọc quanh phần tử title":
    if len(soup.find_all("head")) != 1 or len(soup.find_all("title")) != 1:
      return CheckerResult(False, 0, "")

    if soup.title.parent and soup.title.parent.name == "head":
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")


  # criteria 6
  if input == "Phần tử body bọc quanh phần tử h1 và p":
    if len(soup.find_all("body")) != 1 or len(soup.find_all("h1")) != 1 or len(soup.find_all("p")) != 1:
      return CheckerResult(False, 0, "")

    if soup.p.parent and soup.p.parent.name == "body" and soup.h1.parent and soup.h1.parent.name == "body":
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  return CheckerResult(False, 0, "Lỗi checker")
```
