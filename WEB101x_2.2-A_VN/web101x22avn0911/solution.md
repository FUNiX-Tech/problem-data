```html
<style>
  #box-1 {
    align-self: center;
  }

  #box-2 {
    align-self: flex-end;
  }
</style>

<div id="box-1"></div>
<div id="box-2"></div>
```

```html
<div id="box-1" style="align-self: center;"></div>
<div id="box-2" style="align-self: flex-end;"></div>
```

```python
from bs4 import BeautifulSoup
from dmoj.result import CheckerResult
from dmoj.utils.chrome_driver import get_driver

def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()

  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')

  # criteria 1
  if input == "#box-1 có align-self là center":
    if len(soup.find_all(id="box-1")) != 1:
      return CheckerResult(False, 0, "")

    driver = get_driver(source)

    element = driver.find_element_by_id("box-1")

    css = driver.get_computed_style(element, 'align-self')

    driver.quit()

    if css == 'center':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")


  # criteria 2
  if input == "#box-2 có align-self là flex-end":
    if len(soup.find_all(id="box-2")) != 1:
      return CheckerResult(False, 0, "")

    driver = get_driver(source)

    element = driver.find_element_by_id("box-2")

    css = driver.get_computed_style(element, 'align-self')

    driver.quit()

    if css == 'flex-end':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  return CheckerResult(False, 0, "Lỗi checker")
```
