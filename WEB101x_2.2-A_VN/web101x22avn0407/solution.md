### Freecodecamp

```html
<style>
  h1 {
    font-size: 68px;
  }

  h2 {
    font-size: 52px;
  }

  h3 {
    font-size: 40px;
  }

  h4 {
    font-size: 32px;
  }

  h5 {
    font-size: 21px;
  }

  h6 {
    font-size: 14px;
  }
</style>
<h1></h1>
<h2></h2>
<h3></h3>
<h4></h4>
<h5></h5>
<h6></h6>
```

Sai:

```html
<style>
  .h1 {
    font-size: 68px;
  }

  .h2 {
    font-size: 52px;
  }

  .h3 {
    font-size: 40px;
  }

  .h4 {
    font-size: 32px;
  }

  .h5 {
    font-size: 21px;
  }

  .h6 {
    font-size: 14px;
  }
</style>
<h1 class="h1"></h1>
<h2 class="h2"></h2>
<h3 class="h3"></h3>
<h4 class="h4"></h4>
<h5 class="h5"></h5>
<h6 class="h6"></h6>
```

Sai:

```html
<h1 style="font-size: 68px"></h1>
<h2 style="font-size: 52px"></h2>
<h3 style="font-size: 40px"></h3>
<h4 style="font-size: 32px"></h4>
<h5 style="font-size: 21px"></h5>
<h6 style="font-size: 14px"></h6>
```

### DMOJ

Giống Freecodecamp, chỉ check seletors h1, h2, h3, h4, h5, h6 trong thẻ style

```python
from bs4 import BeautifulSoup
from dmoj.result import CheckerResult
from dmoj.utils.css_parser import parse_css

def _check(soup, element, font_size, point_value):
  if len(soup.find_all(element)) != 1:
    return CheckerResult(False, 0, "")

  css = parse_css(soup)

  fz = css.get(element) and css.get(element).get("font-size")

  if fz == f"{font_size}px" or fz == f"{font_size}px !important":
    return CheckerResult(True, point_value, "")

  return CheckerResult(False, 0, "")

def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()

  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')

  # criteria 1
  if input == "Đặt font-size cho phần tử h1 bằng 68 pixels ở trong phần tử style":
    return _check(soup, "h1", 68, point_value)

  # criteria 2
  if input == "Đặt font-size cho phần tử h2 bằng 52 pixels ở trong phần tử style":
    return _check(soup, "h2", 52, point_value)

  # criteria 3
  if input == "Đặt font-size cho phần tử h3 bằng 40 pixels ở trong phần tử style":
    return _check(soup, "h3", 40, point_value)

  # criteria 4
  if input == "Đặt font-size cho phần tử h4 bằng 32 pixels ở trong phần tử style":
    return _check(soup, "h4", 32, point_value)

  # criteria 5
  if input == "Đặt font-size cho phần tử h5 bằng 21 pixels ở trong phần tử style":
    return _check(soup, "h5", 21, point_value)

  # criteria 6
  if input == "Đặt font-size cho phần tử h6 bằng 14 pixels ở trong phần tử style":
    return _check(soup, "h6", 14, point_value)

  return CheckerResult(False, 0, "Lỗi checker")
```
