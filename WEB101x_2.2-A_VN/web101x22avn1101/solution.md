```html
<h1 id="title">content</h1>

<p id="description">content</p>

<form id="survey-form">
  <label id="name-label">content</label>
  <label id="email-label">content</label>
  <label id="number-label">content</label>

  <input id="name" type="text" required placeholder="content" />
  <input id="email" type="email" required placeholder="content" />
  <input id="number" type="number" min="1" max="10" placeholder="content" />

  <select id="dropdown">
    <option></option>
    <option></option>
  </select>

  <input type="radio" name="radio-group-1" value="value1" />
  <input type="radio" name="radio-group-1" value="value2" />

  <input type="checkbox" name="radio-group-1" value="value1" />
  <input type="checkbox" name="radio-group-1" value="value2" />

  <textarea></textarea>

  <input type="submit" id="submit" />
</form>
```

```python
from bs4 import BeautifulSoup, Comment
from dmoj.result import CheckerResult
from dmoj.utils.unicode import utf8text
from dmoj.utils.css_parser import parse_css
import re

def is_number(str_to_check):
  str_to_check = str(str_to_check).strip()

  str_to_check = re.sub(" +", "", str_to_check)

  if str_to_check == "":
    return False

  try:
    number = float(str_to_check)
    return True
  except ValueError:
    return False

def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()

  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')

  # criteria 1
  if input == "Có 1 thẻ h1 với id là title":
    if len(soup.find_all("h1", id="title")) == 1:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 2
  if input == "#title không được trống":
    if len(soup.find_all("h1", id="title")) != 1:
      return CheckerResult(False, 0, "")

    element = soup.find("h1", id="title")

    if element.text != "":
      return CheckerResult(True, point_value, "")

    return CheckerResult(False, 0, "")

  # criteria 3
  if input == "Có một phần tử p với id description":
    if len(soup.find_all("p", id="description")) == 1:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 4
  if input == "#description không được trống":
    if len(soup.find_all("p", id="description")) != 1:
      return CheckerResult(False, 0, "")

    element = soup.find("p", id="description")

    if element.text != "":
      return CheckerResult(True, point_value, "")

    return CheckerResult(False, 0, "")

  # criteria 5
  if input == "Có 1 phần tử form với id survey-form":
    if len(soup.find_all("form", id="survey-form")) == 1:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 6
  if input == "Có 1 phần tử input với id name":
    if len(soup.find_all("input", id="name")) == 1:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 7
  if input == "#name có type là text":
    if len(soup.find_all("input", id="name")) != 1:
      return CheckerResult(False, 0, "")

    element = soup.find("input", id="name")

    if element.get("type") == "text":
      return CheckerResult(True, point_value, "")

    return CheckerResult(False, 0, "")

  # criteria 8
  if input == "#name phải là input bắt buộc":
    if len(soup.find_all("input", id="name")) != 1:
      return CheckerResult(False, 0, "")

    element = soup.find("input", id="name")

    if element.get("required") == "":
      return CheckerResult(True, point_value, "")

    return CheckerResult(False, 0, "")

  # criteria 9
  if input == "#name là con của #survey-form":
    if len(soup.find_all("form", id="survey-form")) != 1:
      return CheckerResult(False, 0, "")

    element = soup.find("form", id="survey-form")

    if element.find("input", id="name") is not None:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 10
  if input == "Có 1 phần tử input với id là email":
    if len(soup.find_all("input", id="email")) == 1:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 11
  if input == "#mail có type là email":
    if len(soup.find_all("input", id="email")) != 1:
      return CheckerResult(False, 0, "")

    element = soup.find("input", id="email")

    if element.get("type") == "email":
      return CheckerResult(True, point_value, "")

    return CheckerResult(False, 0, "")

  # criteria 12
  if input == "#email là input bắt buộc":
    if len(soup.find_all("input", id="email")) != 1:
      return CheckerResult(False, 0, "")

    element = soup.find("input", id="email")

    if element.get("required") == "":
      return CheckerResult(True, point_value, "")

    return CheckerResult(False, 0, "")

  # criteria 13
  if input == "#email là con của #survey-form":
    if len(soup.find_all("form", id="survey-form")) != 1:
      return CheckerResult(False, 0, "")

    element = soup.find("form", id="survey-form")

    if element.find("input", id="email") is not None:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 14
  if input == "Có 1 phần tử input với id là number":
    if len(soup.find_all("input", id="number")) == 1:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 15
  if input == "#number là con của #survey-form":
    if len(soup.find_all("form", id="survey-form")) != 1:
      return CheckerResult(False, 0, "")

    element = soup.find("form", id="survey-form")

    if element.find("input", id="number") is not None:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 16
  if input == "#number có type là number":
    if len(soup.find_all("input", id="number")) != 1:
      return CheckerResult(False, 0, "")

    element = soup.find("input", id="number")

    if element.get("type") == "number":
      return CheckerResult(True, point_value, "")

    return CheckerResult(False, 0, "")

  # criteria 17
  if input == "#number có attribute min với giá trị là một số":
    if len(soup.find_all("input", id="number")) != 1:
      return CheckerResult(False, 0, "")

    element = soup.find("input", id="number")

    if element.get("min") and is_number(element.get("min")):
      return CheckerResult(True, point_value, "")

    return CheckerResult(False, 0, "")

  # criteria 18
  if input == "#number có attribute max với giá trị là một số":
    if len(soup.find_all("input", id="number")) != 1:
      return CheckerResult(False, 0, "")

    element = soup.find("input", id="number")

    if element.get("max") and is_number(element.get("min")):
      return CheckerResult(True, point_value, "")

    return CheckerResult(False, 0, "")

  # criteria 19
  if input == "Có 1 phần tử label có id là name-label":
    if len(soup.find_all("label", id="name-label")) == 1:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 20
  if input == "Có 1 phần tử label với id là email-label":
    if len(soup.find_all("label", id="email-label")) == 1:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 21
  if input == "Có 1 phần tử label với id là number-label":
    if len(soup.find_all("label", id="number-label")) == 1:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 22
  if input == "#name-label chứa nội dung chữ mô tả input của nó":
    if len(soup.find_all("label", id="number-label")) != 1:
      return CheckerResult(False, 0, "")

    element = soup.find("label", id="name-label")

    if element.text.strip() != "":
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 23
  if input == "#email-label chứa nội dung chữ mô tả input của nó":
    if len(soup.find_all("label", id="email-label")) != 1:
      return CheckerResult(False, 0, "")

    element = soup.find("label", id="email-label")

    if element.text.strip() != "":
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 24
  if input == "#number-label chứa nội dung chữ mô tả input của nó":
    if len(soup.find_all("label", id="number-label")) != 1:
      return CheckerResult(False, 0, "")

    element = soup.find("label", id="number-label")

    if element.text.strip() != "":
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 25
  if input == "#name-label là con của #survey-form":
    if len(soup.find_all("form", id="survey-form")) != 1:
      return CheckerResult(False, 0, "")

    element = soup.find("form", id="survey-form")

    if element.find("label", id="name-label") is not None:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 26
  if input == "#email-label là con của #survey-form":
    if len(soup.find_all("form", id="survey-form")) != 1:
      return CheckerResult(False, 0, "")

    element = soup.find("form", id="survey-form")

    if element.find("label", id="email-label") is not None:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 27
  if input == "#number-label là con của #survey-form":
    if len(soup.find_all("form", id="survey-form")) != 1:
      return CheckerResult(False, 0, "")

    element = soup.find("form", id="survey-form")

    if element.find("label", id="number-label") is not None:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 28
  if input == "#name có attribute placeholder và placeholder này không được để trống":
    if len(soup.find_all("input", id="name")) != 1:
      return CheckerResult(False, 0, "")

    element = soup.find("input", id="name")

    if element.get('placeholder') is not None and element.get('placeholder').strip() != "":
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 29
  if input == "#email có attribute placeholder và placeholder này không được để trống":
    if len(soup.find_all("input", id="email")) != 1:
      return CheckerResult(False, 0, "")

    element = soup.find("input", id="email")

    if element.get('placeholder') is not None and element.get('placeholder').strip() != "":
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 30
  if input == "#number có attribute placeholder và placeholder này không được để trống":
    if len(soup.find_all("input", id="number")) != 1:
      return CheckerResult(False, 0, "")

    element = soup.find("input", id="number")

    if element.get('placeholder') is not None and element.get('placeholder').strip() != "":
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 31
  if input == "Có 1 phần tử select với id là dropdown":
    if len(soup.find_all("select", id="dropdown")) == 1:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 32
  if input == "#dropdown có ít nhất 2 phần tử option có thể lựa chọn (không bị disabled)":
    if len(soup.find_all("select", id="dropdown")) != 1:
      return CheckerResult(False, 0, "")

    element = soup.find("select", id="dropdown")

    if len(element.find_all("option", disabled=False)) >= 2:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 33
  if input == "#dropdown là con của #survey-form":
    if len(soup.find_all("form", id="survey-form")) != 1:
      return CheckerResult(False, 0, "")

    element = soup.find("form", id="survey-form")

    if element.find("select", id="dropdown") is not None:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 34
  if input == "Có ít nhất 2 phần tử input với type là radio (radio buttons)":
    if len(soup.find_all("input", type="radio")) >= 2:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 35
  if input == "Có ít nhất 2 radio buttons là con của #survey-form":
    if len(soup.find_all("form", id="survey-form")) != 1:
      return CheckerResult(False, 0, "")

    element = soup.find("form", id="survey-form")

    if len(element.find_all("input", type="radio")) >= 2:
        return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 36
  if input == "Tất cả các radio buttons phải có attribute value chứa giá trị của nó":
    elements = soup.find_all("input", type="radio")

    if len(elements) == 0:
        return CheckerResult(False, 0, "")

    for element in elements:
      if element.get("value") is None or element.get("value").strip() == "":
        return CheckerResult(False, 0, "")

    return CheckerResult(True, point_value, "")

  # criteria 37
  if input == "Tất cả các radio buttons có attribute name và giá trị của nó":
    elements = soup.find_all("input", type="radio")

    if len(elements) == 0:
        return CheckerResult(False, 0, "")

    for element in elements:
      if element.get("name") is None or element.get("name").strip() == "":
        return CheckerResult(False, 0, "")

    return CheckerResult(True, point_value, "")

  # criteria 38
  if input == "Mỗi nhóm radio button có ít nhất 2 radio buttons":
    elements = soup.find_all("input", type="radio")

    if len(elements) < 2:
      return CheckerResult(False, 0, "")

    for element in elements:
      element_name = element.get("name")

      if element_name is None or element_name.strip() == "":
        return CheckerResult(False, 0, "")

      if len(soup.find_all("input", type="radio", attrs={"name": element_name})) < 2:
        return CheckerResult(False, 0, "")

    return CheckerResult(True, point_value, "")

  # criteria 39
  if input == "Có ít nhất 2 phần tử input với type là checkbox (checkboxes) là con của #survey-form":
    if len(soup.find_all("form", id="survey-form")) != 1:
      return CheckerResult(False, 0, "")

    element = soup.find("form", id="survey-form")

    if len(element.find_all("input", type="checkbox")) >= 2:
        return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 40
  if input == "Tất cả các checkboxes nằm trong #survey-form phải có attribute value và giá trị của nó":
    if len(soup.find_all("form", id="survey-form")) != 1:
      return CheckerResult(False, 0, "")

    form = soup.find("form", id="survey-form")

    checkboxes = form.find_all("input", type="checkbox")

    if len(checkboxes) == 0:
        return CheckerResult(False, 0, "")

    for checkbox in checkboxes:
      if checkbox.get("value") is None or checkbox.get("value").strip() == "":
        return CheckerResult(False, 0, "")

    return CheckerResult(True, point_value, "")

  # criteria 41
  if input == "Có ít nhất 1 phần tử textarea là con của #survey-form":
    if len(soup.find_all("form", id="survey-form")) != 1:
      return CheckerResult(False, 0, "")

    form = soup.find("form", id="survey-form")

    if len(form.find("textarea")) is not None:
      return CheckerResult(True, point_value, "")

    return CheckerResult(False, 0, "")

  # criteria 42
  if input == "Có 1 phần tử input hoặc button với id là submit":
    if len(soup.find_all("input", id="submit")) == 1 or len(soup.find_all("button", id="submit")) == 1:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 43
  if input == "#submit có type là submit":
    if len(soup.find_all(id="submit")) != 1:
      return CheckerResult(False, 0, "")

    element = soup.find(id="submit")

    if element.get("type") == "submit":
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 44
  if input == "#submit là con của #survey-form":
    if len(soup.find_all("form", id="survey-form")) != 1:
      return CheckerResult(False, 0, "")

    element = soup.find("form", id="survey-form")

    if element.find(id="submit") is not None:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  return CheckerResult(False, 0, "Lỗi checker")
```
