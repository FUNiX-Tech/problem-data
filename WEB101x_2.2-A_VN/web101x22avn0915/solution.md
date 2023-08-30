### Freecodecamp:

Đúng:

```html
<style>
  #box-1 {
    flex-basis: 10em;
  }

  #box-2 {
    flex-basis: 20em;
  }
</style>
```

```html
<style>
  sdfsdfs#box-1 {
    flex-basis: 10em;
  }

  disdfsfsv#box-2 {
    flex-basis: 20em;
  }
</style>
```

Sai:

```html
<div id="box-1" style="flex-basis: 10em;"></div>
<div id="box-2" style="flex-basis: 20em;"></div>
```

```html
<style>
  #box-1 {
    flex-basis: 10em !important;
  }

  #box-2 {
    flex-basis: 20em;
  }
</style>
```

---

### DMOJ

Đúng:

```html
<style>
  #box-1 {
    flex-basis: 10em;
  }

  #box-2 {
    flex-basis: 20em;
  }
</style>
```

Sai: Như Freecodecamp và:

```html
<style>
  sdfsdfs#box-1 {
    flex-basis: 10em;
  }

  disdfsfsv#box-2 {
    flex-basis: 20em;
  }
</style>
```

```python
from bs4 import BeautifulSoup
from dmoj.result import CheckerResult
from dmoj.utils.css_parser import parse_css

def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()

  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')

  css = parse_css(soup)

  css_box1 = css.get("#box-1")
  css_box2 = css.get("#box-2")

  # criteria 1
  if input == "#box-1 có property flex-basis":
    if css_box1 and css_box1.get("flex-basis") is not None:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 2
  if input == "#box-1 có flex-basis là 10em":
    if css_box1 and css_box1.get("flex-basis") == "10em":
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 3
  if input == "#box-2 có property flex-basis":
    if css_box2 and css_box2.get("flex-basis") is not None:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 4
  if input == "#box-2 có flex-basis là 20em":
    if css_box2 and css_box2.get("flex-basis") == "20em":
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  return CheckerResult(False, 0, "Lỗi checker")
```
