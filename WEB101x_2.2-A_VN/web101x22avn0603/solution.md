### Freecodecamp

Đúng nếu phần tử đầu tiên có class là blue-box có padding thỏa mãn.

```html
<style>
  .blue-box {
    padding-top: 40px;
    padding-right: 20px;
    padding-bottom: 20px;
    padding-left: 40px;
  }
</style>

<h5 class="blue-box"></h5>
```

```html
<h5
  class="blue-box"
  style="padding-top: 40px;
    padding-right: 20px;
    padding-bottom: 20px;
    padding-left: 40px;"
></h5>
<h5 class="blue-box"></h5>
```

### DMOJ

Như freecodecampe, nhưng nếu số phần tử với class blue-box khác 1 thì cho là sai.

```python
from bs4 import BeautifulSoup
from dmoj.result import CheckerResult
from dmoj.utils.chrome_driver import get_driver

def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()

  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')

  # criteria 1
  if input == "Class blue-box có padding top là 40px":
    if len(soup.find_all(attrs={"class": "blue-box"})) != 1:
      return CheckerResult(False, 0, "")

    driver = get_driver(source)
    element = driver.find_element_by_class_name("blue-box")
    css = driver.get_computed_style(element, 'padding-top')
    driver.quit()

    if css == '40px':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Class blue-box có padding-right là 20px":
    if len(soup.find_all(attrs={"class": "blue-box"})) != 1:
      return CheckerResult(False, 0, "")

    driver = get_driver(source)
    element = driver.find_element_by_class_name("blue-box")
    css = driver.get_computed_style(element, 'padding-right')
    driver.quit()

    if css == '20px':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 3
  if input == "Class blue-box có padding bottom là 20px":
    if len(soup.find_all(attrs={"class": "blue-box"})) != 1:
      return CheckerResult(False, 0, "")

    driver = get_driver(source)
    element = driver.find_element_by_class_name("blue-box")
    css = driver.get_computed_style(element, 'padding-bottom')
    driver.quit()

    if css == '20px':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 4
  if input == "Class blue-box có padding left là 40px":
    if len(soup.find_all(attrs={"class": "blue-box"})) != 1:
      return CheckerResult(False, 0, "")

    driver = get_driver(source)
    element = driver.find_element_by_class_name("blue-box")
    css = driver.get_computed_style(element, 'padding-left')
    driver.quit()

    if css == '40px':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  return CheckerResult(False, 0, "Lỗi checker")
```
