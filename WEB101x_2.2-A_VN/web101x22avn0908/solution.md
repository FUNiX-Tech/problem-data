### Freecodecamp

Đúng: (thực tế là sai nhưng họ vẫn cho là đúng, họ chỉ check thẻ `<style>`)

```html
<style>
  header .profile-name {
    justify-content: center;
  }
</style>
<div class="profile-name"></div>
<div class="follow-btn"></div>
```

```html
<style>
  header .profile-name {
    justify-content: center;
  }
</style>

<div class="follow-btn"></div>
```

Sai:

```html
<style>
  .profile-name {
    justify-content: center;
  }
</style>
<div class="profile-name"></div>
<div class="follow-btn"></div>
```

```html
<div class="profile-name" style="display: flex;justify-content: center;"></div>
<div class="follow-btn"></div>
```

### DMOJ

Miễn là element có class profile-name có css thỏa mãn

Đúng:

```html
<style>
  div {
    justify-content: center;
  }
</style>
<div class="profile-name"></div>
<div class="follow-btn"></div>
```

```html
<div class="profile-name" style=" justify-content: center;"></div>
<div class="follow-btn"></div>
```

Sai:

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

    css = driver.get_computed_style(element, 'display')

    driver.quit()

    if css != 'none':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 2
  if input == ".profile-name có justify-content được đặt là một trong các giá trị sau: center, flex-start, flex-end, space-between, space-around, space-evenly":
    if len(soup.find_all(attrs={"class": "profile-name"})) != 1:
      return CheckerResult(False, 0, "")

    driver = get_driver(source)

    element = driver.find_element_by_class_name("profile-name")

    css = driver.get_computed_style(element, 'justify-content')

    driver.quit()

    correct_answers = ['center', 'flex-start', 'flex-end', 'space-between', 'space-around', 'space-evenly']

    if css in correct_answers:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  return CheckerResult(False, 0, "Lỗi checker")
```
