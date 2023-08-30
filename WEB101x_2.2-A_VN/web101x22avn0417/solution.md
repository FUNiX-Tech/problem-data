### Freecodecamp

Đúng:

```html
<h4 style="padding: 10px; background-color: rgba(45, 45, 45, 0.1);"></h4>
```

```html
<style>
  h4 {
    background-color: rgba(45, 45, 45, 0.1);
    padding: 10px;
  }
</style>

<h4></h4>
```

```html
<style>
  .h4 {
    background-color: rgba(45, 45, 45, 0.1);
    padding: 10px;
  }
</style>
<h4 class="h4"></h4>
```

Sai:

Không có dấu chấm phẩy ở cuối

```html
<h4 style="padding: 10px; background-color: rgba(45, 45, 45, 0.1)"></h4>
```

### DMOJ

Đúng:

Như Freecodecamp, thêm trường hợp inline không có chấm phẩy ở cuối vẫn đúng:

```html
<h4 style="padding: 10px; background-color: rgba(45, 45, 45, 0.1)"></h4>
```

```python
from bs4 import BeautifulSoup
from dmoj.result import CheckerResult
from dmoj.utils.css_parser import parse_css, get_element_css_value, count_element
from dmoj.utils.chrome_driver import get_driver
import re

def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()

  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')

  if count_element(soup, 'h4') != 1:
    return CheckerResult(False, 0, "")

  h4 = soup.h4

  # criteria 1
  if input == "Thẻ h4 có background-color là rgba(45, 45, 45, 0.1)":
    driver = get_driver(source)
    element = driver.find_element_by_tag_name("h4")
    css = "" if element is None else driver.get_computed_style(element, "background-color")
    driver.quit()

    if css == "rgba(45, 45, 45, 0.1)":
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Thẻ h4 có padding 10 pixels":
    driver = get_driver(source)
    element = driver.find_element_by_tag_name("h4")
    css = "" if element is None else driver.get_computed_style(element, "padding")
    driver.quit()

    if css == "10px":
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 3
  if input == "Loại bỏ property height của thẻ h4":
    height = get_element_css_value(soup, h4, 'height')

    if height is None or height.strip() == "":
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  return CheckerResult(False, 0, "Lỗi checker")
```
