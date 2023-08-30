```html
<input type="text" />
```

```python
from bs4 import BeautifulSoup
from dmoj.result import CheckerResult

def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()

  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')

  if soup.find("input", type="text"):
    return CheckerResult(True, point_value, "")
  return CheckerResult(False, 0, "")
```
