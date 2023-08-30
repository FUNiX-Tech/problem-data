```html
<style>
  .container2 {
    /* Only change code below this line */
    grid-template-columns: repeat(auto-fit, minmax(60px, 1fr));
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

  container = css.get(".container2")

  if container is None:
    return CheckerResult(False, 0, "")

  need_to_check = container.get("grid-template-columns")

  need_to_check = re.sub(r" +", " ", need_to_check)

  if re.fullmatch(r'repeat\s?\(\s?auto-fit\s?,\s?minmax\(\s?60px\s?,\s?1fr\s?\)\s?\)', need_to_check):
    return CheckerResult(True, point_value, "")
  return CheckerResult(False, 0, "")

```
