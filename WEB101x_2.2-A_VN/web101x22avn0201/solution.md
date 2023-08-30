

Nếu có nhiều hơn 1 thẻ h1, thì kết quả sẽ là của thẻ h1 đầu tiên.

Nếu thẻ h1 không có thẻ đóng hoặc thẻ đóng không khớp, ví dụ: `</ h2>`, `</ a b c>`,... thì vẫn đúng. 

Nếu thể  h1 có thẻ đóng sai: `< /h1>` (có khoảng trống giữa `<` và `/`) thì đó sẽ được coi là text (được hiển thị trên iframe) nên sẽ cho kết quả sai

Đúng:
```html
<h1>Hello World</h1>
```

```html
<h1>Hello World</ fff>
```

```html
<h1>Hello World
```

Sai

```html 
<h1>Hello World fff</h1>
```

```html 
<h1>Hello World< /h1>
```

```html 
<h1>Cat</h1>
<h1>Hello World</h1>
```

```python
from bs4 import BeautifulSoup
from dmoj.result import CheckerResult
  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  if soup.h1 and soup.h1.text == "Hello World":
    return CheckerResult(True, point_value, "")
  return CheckerResult(False, 0, "")
```