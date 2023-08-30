Web developers traditionally use lorem ipsum text as placeholder text. The lorem ipsum text is randomly scraped from a famous passage by Cicero of Ancient Rome.

Lorem ipsum text has been used as placeholder text by typesetters since the 16th century, and this tradition continues on the web.

---

Replace the text inside your `p` element with the first few words of this kitty ipsum text: `Kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching attack your ankles chase the red dot, hairball run catnip eat the grass sniff.`

---

Văn bản Lorem ipsum đã được sử dụng làm văn bản giữ chỗ từ thế kỷ 16 và truyền thống này vẫn được duy trì cho đến nay.

Năm thế kỷ là đủ dài. Vì chúng ta đang xây dựng một CatPhotoApp, hãy sử dụng văn bản gọi là "kitty ipsum".

---

Thay thế văn bản bên trong phần tử `p` của bạn bằng một vài từ của đoạn đầu đoạn văn bản kitty ipsum này: `Kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching attack your ankles chase the red dot, hairball run catnip eat the grass sniff.`

---

```html
<h1>Hello World</h1>

<h2>CatPhotoApp</h2>

<p>Hello Paragraph</p>
```

```python
from bs4 import BeautifulSoup
from dmoj.result import CheckerResult
  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  kitty = "Kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching attack your ankles chase the red dot, hairball run catnip eat the grass sniff."
  if soup.p and soup.p.text is not None and soup.p.text in kitty and len(soup.p.text) > 30: 
    return CheckerResult(True, point_value, "")
  return CheckerResult(False, 0, "")
  
```