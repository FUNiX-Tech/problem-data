```html
<style>
  .container {
    /* Only change code below this line */

    align-items: end;
    /* Only change code above this line */
  }
</style>
```

```python
from bs4 import BeautifulSoup
from dmoj.result import CheckerResult
from dmoj.utils.css_parser import parse_css
import re

def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()

  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')

  css = parse_css(soup)

  container = css.get(".container")

  if container is None:
    return CheckerResult(False, 0, "")

  align_items = container.get("align-items")

  if css.get(".container") and   css.get(".container").get("align-items") == 'end':
    return CheckerResult(True, point_value, "")
  return CheckerResult(False, 0, "")

```
