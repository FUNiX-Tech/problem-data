```html
<form id="cat-photo-form"></form>
```

```html
<form></form>
<form id="cat-photo-form"></form>
```

```python
from bs4 import BeautifulSoup
from dmoj.result import CheckerResult

def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')

  if soup.find("form", id="cat-photo-form"):
    return CheckerResult(True, point_value, "")
  return CheckerResult(False, 0, "")
```
