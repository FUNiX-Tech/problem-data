### Freecodecamp

Đúng:

```html
<style>
  header {
    flex-direction: row;
  }

  footer {
    flex-direction: row;
  }
</style>

<header></header>
<footer></footer>
<p class="follow-btn"></p>
```

```html
<style>
  header {
    flex-direction: row;
  }

  footer {
    flex-direction: row;
  }
</style>

<p class="follow-btn"></p>
```

Sai:

```html
<header style="flex-direction: row;"></header>
<footer style="flex-direction: row;"></footer>
<p class="follow-btn"></p>
```

### DMOJ

Trường hợp không có thẻ header và footer trong code sẽ là sai.

```python
from bs4 import BeautifulSoup
from dmoj.result import CheckerResult
from dmoj.utils.chrome_driver import get_driver

def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()

  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')

  # criteria 1
  if input == ".follow-btn được hiển thị trên trang. Đảm bảm rằng đã tắt các tiện ích mở rộng như ad blockers":
    if len(soup.find_all(attrs={"class": "follow-btn"})) != 1:
      return CheckerResult(False, 0, "")

    driver = get_driver(source)
    element = driver.find_element_by_class_name("follow-btn")
    css = driver.get_computed_style(element, "display")
    driver.quit()

    if css != "none":
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 2
  if input == "header có flex-direction là row":
    if len(soup.find_all("header")) != 1:
      return CheckerResult(False, 0, "")

    driver = get_driver(source)

    element = driver.find_element_by_tag_name("header")

    css = driver.get_computed_style(element, 'flex-direction')

    driver.quit()

    if css == 'row':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 3
  if input == "footer có flex-direction là row":
    if len(soup.find_all("footer")) != 1:
      return CheckerResult(False, 0, "")

    driver = get_driver(source)

    element = driver.find_element_by_tag_name("footer")

    css = driver.get_computed_style(element, 'flex-direction')

    driver.quit()

    if css == 'row':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  return CheckerResult(False, 0, "Lỗi checker")
```
