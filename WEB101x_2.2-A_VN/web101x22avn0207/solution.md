Đúng của freecodecamp: 

```html
<ul>
  <li>milk</li>
  <li>cheese</li>
</ul>
<ul>
  <li>milk</li>
  <li>cheese</li>
</ul>
```

```html
<ul>
  <li>milk</li>
  <li>cheese</li>
  <li>rat</li>
</ul>
```

---
Đúng của dmoj:

```html
<ul>
  <li>milk</li>
  <li>cheese</li>
  <li>rat</li>
</ul>
```

Sai: 

Thẻ ul đầu tiên không có 3 phần tử:
```html
<ul>
  <li>milk</li>
  <li>cheese</li>
</ul>
<ul>
  <li>milk</li>
  <li>cheese</li>
  <li>rat</li>
</ul>
```

Thẻ ul thứ 2 có thẻ li trống:
```html
<ul>
  <li>milk</li>
  <li>cheese</li>
  <li>rat</li>
</ul>
<ul>
  <li></li>
  <li>cheese</li>
</ul>
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
  if input == "Tạo phần tử ul":
    if soup.ul:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Tạo 3 phần tử li trong phần tử ul vừa tạo":
    ul = soup.ul

    if ul and len(ul.find_all("li")) == 3:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 3
  if input == "Phần tử ul cần có thẻ đóng":
    if soup.ul and len(soup.find_all("ul")) == source.count("</ul>"):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 4
  if input == "Phần tử li cần có thẻ đóng":
    if soup.li and len(soup.find_all("li")) == source.count("</li>"):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
    
  # criteria 5
  if input == "Phần tử li không được chứa chỉ khoảng trắng hoặc chuỗi rỗng":
    lis = soup.find_all("li")
    if len(lis) == 0:
      return CheckerResult(False, 0, "")

    for li in lis:
      if li.text.strip() == "":
        return CheckerResult(False, 0, "")
    return CheckerResult(True, point_value, "")
  
  return CheckerResult(False, 0, "Lỗi checker")
```