```html
<style>
  body {
    background-color: black;
    font-family: monospace;
    color: green;
  }
  #orange-text {
    color: orange;
  }
  .pink-text {
    color: pink;
  }
  .blue-text {
    color: blue;
  }
</style>
<h1 id="orange-text" class="pink-text blue-text" style="color: white"></h1>
```

```html
<style>
  h1 {
    color: white;
  }
</style>
<h1 id="orange-text" class="pink-text blue-text" style="height: 20px"></h1>
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
  if input == "Thẻ h1 có class pink-text":
    if soup.find("h1", attrs={"class": "pink-text"}):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Thẻ h1 có class blue-text":
    if soup.find("h1", attrs={"class": "blue-text"}):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 3
  if input == "Thẻ h1 có id orange-text":
    if soup.find("h1", attrs={"id": "orange-text"}):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 4
  if input == "Thẻ h1 có style inline":
    if soup.find("h1", style=True):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 5
  if input == "Thẻ h1 có chữ màu trắng":
    if len(soup.find_all("h1")) != 1:
        return CheckerResult(False, 0, "")

    driver = get_driver(source)

    element = driver.find_element_by_tag_name("h1")

    css = "" if element is None else driver.get_computed_style(element, 'color')

    driver.quit()

    if css == "rgb(255, 255, 255)":
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  return CheckerResult(False, 0, "Lỗi checker")
```
