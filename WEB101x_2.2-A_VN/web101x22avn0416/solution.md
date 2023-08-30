### Freecodecamp

```html
<style>
  .red-text {
    color: rgb(255, 0, 0);
  }
  .orchid-text {
    color: rgb(218, 112, 214);
  }
  .sienna-text {
    color: rgb(160, 82, 45);
  }
  .blue-text {
    color: rgb(0, 0, 255);
  }
</style>

<h1 class="red-text"></h1>
<h1 class="orchid-text"></h1>
<h1 class="sienna-text"></h1>
<h1 class="blue-text"></h1>
```

### DMOJ

```html
<style>
  .red-text {
    color: rgb(255, 0, 0);
  }
  .orchid-text {
    color: rgb(218, 112, 214);
  }
  .sienna-text {
    color: rgb(160, 82, 45);
  }
  .blue-text {
    color: rgb(0, 0, 255);
  }
</style>

<h1 class="red-text">I am red!</h1>
<h1 class="orchid-text">I am orchid!</h1>
<h1 class="sienna-text">I am sienna!</h1>
<h1 class="blue-text">I am blue!</h1>
```

```python
from bs4 import BeautifulSoup
from dmoj.result import CheckerResult
from dmoj.utils.css_parser import  get_element_css_value
from dmoj.utils.chrome_driver import get_driver
import re

red = [
  "red",
"#ff0000",
"#f00",
"rgb(255,0,0)",
"rgb(100%,0%,0%)",
"hsl(0,100%,50%)",
"hsl(0,100%,50%)",
"hsla(0,100%,50%,1)",
"hsla(0,100%,50%,1)"
]

orchid = [
  "orchid",
  "#DA70D6",
  "#9932CC",
  "rgb(218,112,214)",
  "rgb(85%,44%,85%)",
  "hsl(302,59%,65%)",
  "hsla(302,59%,65%,1)"
]

blue = [
  "blue",
  "#0000FF",
  "#00F",
  "rgb(0,0,255)",
  "rgb(0%,0%,100%)",
  "hsl(240,100%,50%)",
  "hsla(240,100%,50%,1)"
]

sienna = [
  "sienna",
  "#A0522D",
  "#F40",
  "rgb(160,82,45)",
  "rgb(63%,32%,18%)",
  "hsl(19,56%,40%)",
  "hsla(19,56%,40%,1)"
]

def tidy_color_value(color):
  color = re.sub(" !important", "", color)
  color = re.sub(" +", "", color)
  return color

def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()

  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')

  # criteria 1
  if input == "Thẻ h1 với nội dung I am red! có màu red":
    if  len(soup.find_all('h1', attrs={"class": "red-text"}, string='I am red!')) != 1:
      return CheckerResult(False, 0, "")

    if  len(soup.find_all('h1', attrs={"class": "red-text"})) != 1:
      return CheckerResult(False, 0, "")

    driver = get_driver(source)

    element = driver.find_element_by_class_name("red-text")

    css = "" if element is None else driver.get_computed_style(element, "color")

    driver.quit()

    if css == "rgb(255, 0, 0)":
      return CheckerResult(True, point_value, "")

    return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Sử dụng rgb cho màu red":
    if  len(soup.find_all('h1', attrs={"class": "red-text"}, string='I am red!')) != 1:
      return CheckerResult(False, 0, "")

    if  len(soup.find_all('h1', attrs={"class": "red-text"})) != 1:
      return CheckerResult(False, 0, "")

    h1 = soup.find("h1", attrs={"class": "red-text"}, string='I am red!')

    color = get_element_css_value(soup, h1, "color")

    color = tidy_color_value(color)

    if color in ["rgb(255,0,0)", "rgb(100%,0%,0%)"]:
      return CheckerResult(True, point_value, "")

    return CheckerResult(False, 0, "")

  # criteria 3
  if input == "Thẻ h1 có nội dung I am orchid! có màu orchid":
    if  len(soup.find_all('h1', attrs={"class": "orchid-text"}, string='I am orchid!')) != 1:
      return CheckerResult(False, 0, "")

    if  len(soup.find_all('h1', attrs={"class": "orchid-text"})) != 1:
      return CheckerResult(False, 0, "")

    driver = get_driver(source)

    element = driver.find_element_by_class_name("orchid-text")

    css = "" if element is None else driver.get_computed_style(element, "color")

    driver.quit()

    if css == "rgb(218, 112, 214)":
      return CheckerResult(True, point_value, "")

    return CheckerResult(False, 0, "")

  # criteria 4
  if input == "Sử dụng rgb cho màu orchid":
    if  len(soup.find_all('h1', attrs={"class": "orchid-text"}, string='I am orchid!')) != 1:
      return CheckerResult(False, 0, "")

    if  len(soup.find_all('h1', attrs={"class": "orchid-text"})) != 1:
      return CheckerResult(False, 0, "")

    h1 = soup.find("h1",  attrs={"class": "orchid-text"}, string='I am orchid!')

    color = get_element_css_value(soup, h1, "color")

    color = tidy_color_value(color)

    if color in ["rgb(218,112,214)", "rgb(85%,44%,85%)"]:
      return CheckerResult(True, point_value, "")

    return CheckerResult(False, 0, "")

  # criteria 5
  if input == "Thẻ h1 có nội dung I am blue! có màu blue":
    if  len(soup.find_all('h1', attrs={"class": "blue-text"}, string='I am blue!')) != 1:
      return CheckerResult(False, 0, "")

    if  len(soup.find_all('h1', attrs={"class": "blue-text"})) != 1:
      return CheckerResult(False, 0, "")

    driver = get_driver(source)

    element = driver.find_element_by_class_name("blue-text")

    css = "" if element is None else driver.get_computed_style(element, "color")

    driver.quit()

    if css == "rgb(0, 0, 255)":
      return CheckerResult(True, point_value, "")

    return CheckerResult(False, 0, "")

  # criteria 6
  if input == "Sử dụng rgb cho màu blue":
    if  len(soup.find_all('h1', attrs={"class": "blue-text"}, string='I am blue!')) != 1:
      return CheckerResult(False, 0, "")

    if  len(soup.find_all('h1', attrs={"class": "blue-text"})) != 1:
      return CheckerResult(False, 0, "")

    h1 = soup.find("h1", attrs={"class": "blue-text"}, string='I am blue!')

    color = get_element_css_value(soup, h1, "color")

    color = tidy_color_value(color)

    if color in ["rgb(0,0,255)", "rgb(0%,0%,100%)"]:
      return CheckerResult(True, point_value, "")

    return CheckerResult(False, 0, "")

  # criteria 7
  if input == "Thẻ h1 có nội dung I am sienna! có chữ màu sienna":
    if  len(soup.find_all('h1', attrs={"class": "sienna-text"}, string='I am sienna!')) != 1:
      return CheckerResult(False, 0, "")

    if  len(soup.find_all('h1', attrs={"class": "sienna-text"})) != 1:
      return CheckerResult(False, 0, "")

    driver = get_driver(source)

    element = driver.find_element_by_class_name("sienna-text")

    css = "" if element is None else driver.get_computed_style(element, "color")

    driver.quit()

    if css == "rgb(160, 82, 45)":
      return CheckerResult(True, point_value, "")

    return CheckerResult(False, 0, "")

  # criteria 8
  if input == "Sử dụng rgb cho màu sienna":
    if  len(soup.find_all('h1', attrs={"class": "sienna-text"}, string='I am sienna!')) != 1:
      return CheckerResult(False, 0, "")

    if  len(soup.find_all('h1', attrs={"class": "sienna-text"})) != 1:
      return CheckerResult(False, 0, "")

    h1 = soup.find("h1", attrs={"class": "sienna-text"}, string='I am sienna!')

    color = get_element_css_value(soup, h1, "color")

    color = tidy_color_value(color)

    if color in ["rgb(160,82,45)", "rgb(63%,32%,18%)"]:
      return CheckerResult(True, point_value, "")

    return CheckerResult(False, 0, "")

  return CheckerResult(False, 0, "Lỗi checker")

```
