### Freecodecamp

Sai:

```html
<body style="background-color: #000000"></body>
```

```html
<style>
  body {
    background-color: #000000 !important;
  }
</style>
```

```html
<style>
  body {
    background-color: #000 !important;
  }
</style>
```

Đúng:

```html
<style>
  body {
    background-color: #000000;
  }
</style>
```

```html
<style>
  body {
    background-color: #000;
  }
</style>
```

### DMOJ

Đúng:

```html
<style>
  body {
    background-color: #000;
  }
</style>
```

```html
<style>
  body {
    background-color: #000 !important;
  }
</style>
```

```html
<style>
  body {
    background-color: #000000;
  }
</style>
```

```html
<style>
  body {
    background-color: #000000 important;
  }
</style>
```

```python
from bs4 import BeautifulSoup
from dmoj.result import CheckerResult
from dmoj.utils.css_parser import parse_css
from dmoj.utils.chrome_driver import get_driver

def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()

  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')

  if soup.style is None:
    return CheckerResult(False, 0, "")

  css = parse_css(soup)

  if css.get("body") is None:
    return CheckerResult(False, 0, "")

  # criteria 1
  if input == "Phần tử body có background-color là màu đen":


    driver = get_driver(source)

    body = driver.find_element_by_tag_name("body")

    bg = driver.get_computed_style(body, "background-color")

    driver.quit()

    if bg == "rgb(0, 0, 0)":
      return CheckerResult(True, point_value, "")

    return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Hãy sử dụng hex code thay vì dùng black để có màu nền màu đen":
    correct_answers = ['#000', '#000 !important', '#000000', '#000000 !importannt']
    bg = css.get("body").get("background-color") or ""
    if bg in correct_answers:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  return CheckerResult(False, 0, "Lỗi checker")
```
