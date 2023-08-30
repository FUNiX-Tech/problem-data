Đúng: 

```html
<a href="https://www.freecatphotoapp.com">cat photos</a>
```

Chỉ check thẻ a đầu tiên.

Sai: 
Có dấu cách ở cuối `cat photos `
```html
<a href="https://www.freecatphotoapp.com">cat photos </a>
```

```python
from bs4 import BeautifulSoup
from dmoj.result import CheckerResult
  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  # criteria 1
  if input == "Có 1 phần tử a có nội dung 'cat photos'":
    if soup.find("a", string="cat photos"):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Phần tử a liên kết đến https://www.freecatphotoapp.com":
    if soup.find("a", href="https://www.freecatphotoapp.com"):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 3
  if input == "Phần tử a có thẻ đóng":
    if soup.a and len(soup.find_all("a")) == source.count("</a>"):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  return CheckerResult(False, 0, "Lỗi checker")
```