```html
<style>
  .container {
    /* Only change code below this line */

    grid-template-columns: repeat(3, minmax(90px, 1fr));

    /* Only change code above this line */
  }
</style>

<div class="container"></div>
```

Sai:

```html
<style>
  .container {
    /* Only change code below this line */

    grid-template-columns: repeat(3, minmax(1fr, 90px));

    /* Only change code above this line */
  }
</style>

<div class="container"></div>
```

```python
from bs4 import BeautifulSoup, Comment
from dmoj.result import CheckerResult
from dmoj.utils.unicode import utf8text
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

  grid_template_columns = container.get("grid-template-columns")

  if grid_template_columns is None:
    return CheckerResult(False, 0, "")

  grid_template_columns = grid_template_columns.strip()

  if re.fullmatch(r"repeat\s?\(\s?3\s?,\s?minmax\s?\(\s?90px\s?,\s?1fr\s?\)\s?\)", grid_template_columns):
    return CheckerResult(True, point_value, "")
  return CheckerResult(False, 0, "")

```
