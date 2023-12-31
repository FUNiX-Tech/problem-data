```html
<style>
  h2 {
    position: relative;
    top: -10px;
    left: 15px;
  }
</style>
<h2></h2>
```

```html
<style>
  h2 {
    position: relative;
    bottom: 10px;
    right: -15px;
  }
</style>
<h2></h2>
```

```html
<h2
  style="   position: relative;
    bottom: 10px;
    right: -15px;"
></h2>
```

```html
<h2
  style="     position: relative;
    top: -10px;
    left: 15px;"
></h2>
```

```python
from bs4 import BeautifulSoup
from dmoj.result import CheckerResult
from dmoj.utils.chrome_driver import get_driver

def structure_changed(soup):
  return len(soup.find_all("h2")) != 1

def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()

  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')

  if structure_changed(soup):
    return CheckerResult(False, 0, "")

  # criteria 1
  if input == "Sử dụng CSS offset để đặt vị trí h2 10px lên trên":
    driver = get_driver(source)

    element = driver.find_element_by_tag_name("h2")

    top = driver.get_computed_style(element, 'top')
    bottom = driver.get_computed_style(element, 'bottom')

    driver.quit()

    if top == '-10px' and bottom == '10px':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Sử dụng CSS offset dể đặt vị trí tương đối của thẻ h2 15px về bên phải":
    driver = get_driver(source)

    element = driver.find_element_by_tag_name("h2")

    right = driver.get_computed_style(element, 'right')
    left = driver.get_computed_style(element, 'left')

    driver.quit()

    if right == '-15px' and left == '15px':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  return CheckerResult(False, 0, "Lỗi checker")
```
