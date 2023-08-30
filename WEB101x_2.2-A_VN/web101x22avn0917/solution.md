```html
<style>
  #box-1 {
    order: 2;
  }

  #box-2 {
    order: 1;
  }
</style>

<div id="box-1"></div>
<div id="box-2"></div>
```

```html
<div id="box-1" style="order: 2;"></div>
<div id="box-2" style="order: 1;"></div>
```

```python
from bs4 import BeautifulSoup
from dmoj.result import CheckerResult
from dmoj.utils.chrome_driver import get_driver


def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()

  source = submission_source.decode('utf-8').strip()

  # criteria 1
  if input == "#box-1 có order là 2":
    driver = get_driver(source)
    box = driver.find_element_by_id("box-1")
    css = "" if box is None else driver.get_computed_style(box, "order")
    driver.quit()
    if css == "2":
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 2
  if input == "#box-2 có order là 1":
    driver = get_driver(source)
    box = driver.find_element_by_id("box-2")
    css = "" if box is None else driver.get_computed_style(box, "order")
    driver.quit()
    if css == "1":
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  return CheckerResult(False, 0, "Lỗi checker")
```
