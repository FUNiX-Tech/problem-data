### Freecodecamp

```html
<style>
  .pink-text {
    color: red;
  }
</style>
<h1 class="pink-text" style="color: pink;">Hello World!</h1>
```

```html
<style>
  .pink-text {
    color: pink;
  }
</style>
<h1 class="pink-text">Hello World!</h1>
```

### DMOJ

Chỉ trường hợp dùng class selector để set color là được tính:

```html
<style>
  .pink-text {
    color: pink;
  }
</style>
<h1 class="pink-text">Hello World!</h1>
```

```python
from bs4 import BeautifulSoup
from dmoj.result import CheckerResult
from dmoj.utils.css_parser import parse_css, get_element_css_value
from dmoj.utils.chrome_driver import get_driver

def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()

  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')

  if len(soup.find_all('h1')) != 1:
    return CheckerResult(False, 0, "")

  h1 = soup.h1

  # criteria 1
  if input == "Thẻ h1 có class pink-text":
    if h1.get("class") and "pink-text" in h1.get("class"):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Thẻ <style> có pink-text CSS class dùng để đổi màu chữ":
    css = parse_css(soup)

    if css.get(".pink-text") and css.get(".pink-text").get("color") == "pink":
      return CheckerResult(True, point_value, "")

    return CheckerResult(False, 0, "")

  # criteria 3
  if input == "Thẻ h1 có chữ màu hồng (pink)":
    driver = get_driver(source)

    element = driver.find_element_by_tag_name("h1")

    css = "" if element is None else driver.get_computed_style(element, "color")

    driver.quit()

    if css == "rgb(255, 192, 203)":
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  return CheckerResult(False, 0, "Lỗi checker")
```
