Chỉ đánh giá thẻ img đầu tiên.

Đúng: 

```html
<img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg" alt="f" />
```

Sai:

```html
<img />
<img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg" alt="f" />
```

Thiếu alt: 

```html
<img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg" alt="  " />
```

src sai: 

```html
<img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg2" alt="kitty" />
```

```python
from bs4 import BeautifulSoup, Comment
from dmoj.result import CheckerResult
  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  # criteria 1
  if input == "Có một phần tử image":
    if soup.img:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Phần tử image có attribute src trỏ tới ảnh mèo":
    if soup.img and soup.img.get('src') == "https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg":
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 3
  if input == "Attribute alt của phần tử hình ảnh không được trống":
    if soup.img and soup.img.get("alt") is not None and soup.img.get("alt").strip() != "":
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  return CheckerResult(False, 0, "Lỗi checker")
```