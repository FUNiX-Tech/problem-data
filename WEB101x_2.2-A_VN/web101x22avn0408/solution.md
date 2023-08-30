```html
<style>
  p {
    line-height: 25px;
  }
</style>
<p></p>
```

```html
<style>
  .p {
    line-height: 25px;
  }
</style>
<p class="p"></p>
```

```html
<p style="line-height: 25px"></p>
```

```python
from bs4 import BeautifulSoup
from dmoj.result import CheckerResult
from dmoj.utils.chrome_driver import get_driver

def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()

  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')

  if len(soup.find_all("p")) != 1:
    return CheckerResult(False, 0, "")

  driver = get_driver(source)

  element = driver.find_element_by_tag_name("p")

  css = driver.get_computed_style(element, 'line-height') if element is not None else None

  driver.quit()

  if css == "25px":
    return CheckerResult(True, point_value, "")
  return CheckerResult(False, 0, "")
```
