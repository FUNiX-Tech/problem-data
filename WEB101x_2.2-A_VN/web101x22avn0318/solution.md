### Freecodecamp

```html
<label
  ><input value="indoor" type="radio" name="indoor-outdoor" /> Indoor</label
>
<label
  ><input value="outdoor" type="radio" name="indoor-outdoor" /> Outdoor</label
>
<label
  ><input value="loving" type="checkbox" name="personality" /> Loving</label
>
<label
  ><input id="lazy" value="lazy" type="checkbox" name="personality" />
  Lazy</label
>
<label
  ><input value="energetic" type="checkbox" name="personality" />
  Energetic</label
>
```

### DMOJ

```html
<input id="indoor" value="indoor" type="radio" name="indoor-outdoor" />
<input id="outdoor" value="outdoor" type="radio" name="indoor-outdoor" />
<input id="loving" value="loving" type="checkbox" name="personality" />
<input id="lazy" value="lazy" type="checkbox" name="personality" />
<input id="energetic" value="energetic" type="checkbox" name="personality" />
```

```python
from bs4 import BeautifulSoup, Comment
from dmoj.result import CheckerResult

def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()

  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')

  # criteria 1
  if input == "Một trong các radio buttons có value là indoor":
    if soup.find("input", attrs={"type": "radio", "value": "indoor", "name":"indoor-outdoor", "id": "indoor"}):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Một trong các radio buttons có value là outdoor":
    if soup.find("input", attrs={"type": "radio", "value": "outdoor", "name":"indoor-outdoor", "id": "outdoor"}):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 3
  if input == "Một trong các checkbox có value là loving":
    if soup.find("input", attrs={"type": "checkbox", "value": "loving", "name":"personality", "id": "loving"}):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 4
  if input == "Một trong các checkbox có value là lazy":
    if soup.find("input", attrs={"type": "checkbox", "value": "lazy", "name":"personality", "id": "lazy"}):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 5
  if input == "Một trong các checkbox có value là energetic":
    if soup.find("input", attrs={"type": "checkbox", "value": "energetic", "name":"personality", "id": "energetic"}):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  return CheckerResult(False, 0, "Lỗi checker")
```
