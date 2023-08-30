```html
<a href="#"><img /></a>
```

```python
from bs4 import BeautifulSoup, Comment
from dmoj.result import CheckerResult
  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  # criteria 1
  if input == "Phần tử img phải nằm trong phần tử a":
    if len(soup.find_all("a")) == 1 and  len(soup.find_all("img")) == 1 and soup.img.parent.name == "a":
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
    

  # criteria 2
  if input == "Phần tử a là dead link với href là #":
    if soup.find("a", href="#"):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
    
  
  # criteria 3
  if input == "Mỗi phần tử a phải có thẻ đóng":
    if soup.a and len(soup.find_all("a")) == source.count("</a>"):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  return CheckerResult(False, 0, "Lỗi checker")
```