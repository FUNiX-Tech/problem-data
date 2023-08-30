### Freecodecamp

Đúng: 

```html

<main>
  
  <p>Things cats love:</p>
  
  <ul>
    <li>cat nip</li>
    <li>laser pointers</li>
    <li>lasagna</li>
  </ul>

  <p>Top 3 things cats hate:</p>

  <ol>
    <li>f</li>
    <li>f</li>
    <li>f</li>
  </ol>

</main>
```

```html

<main>
  
  <p>Things cats love:</p>

  <ul>
    <li>cat nip</li>
    <li>laser pointers</li>
    <li>lasagna</li>
  </ul>

  <p>Top 3 things cats hate:</p>

</main>

<ol>
<li>f</li>
<li>f</li>
<li>f</li>
</ol>
```

---

### DMOJ

Nếu trong bài nộp có ký tự `<!--` hoặc `-->` hoặc không có 2 thẻ p mẫu đã cho thì được cho là sai hết. 

Đáp án đúng: như trên.

```python
from bs4 import BeautifulSoup, Comment
from dmoj.result import CheckerResult

def structure_changed(soup, source):
  return source.count("-->") > 0 or \
    source.count("<!--") > 0 or \
    len(soup.find_all("p", string="Things cats love:")) != 1 or \
    len(soup.find_all("p", string="Top 3 things cats hate:")) != 1
  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  if structure_changed(soup, source):
    return CheckerResult(False, 0, "")
  
  p_love = soup.find("p", string="Things cats love:")
  p_hate = soup.find("p", string="Top 3 things cats hate:")
  
  # criteria 1
  if input == "Có 1 danh sách có thứ tự cho 'Top 3 things cats hate:'":
    if p_hate.find_next_sibling('ol'):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Có 1 danh sách không có thứ tự cho 'Things cats love:'":
    if p_love.find_next_sibling('ul') and not p_hate.find_next_sibling("ul"):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 3
  if input == "Chỉ có 1 phần tử ul":
    if len(soup.find_all("ul")) == 1:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 4
  if input == "Chỉ có một phần tử ol":
    if len(soup.find_all("ol")) == 1:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 5
  if input == "Có 3 phần tử li trong phần tử ul":
    if len(soup.find_all("ul")) != 1:
      return CheckerResult(False, 0, "")
      
    element = soup.ul
    if len(element.find_all("li")) == 3:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")


  # criteria 6
  if input == "Có 3 phần tử li trong phần tử ol":
    if len(soup.find_all("ol")) != 1:
      return CheckerResult(False, 0, "")
      
    element = soup.ol
    if len(element.find_all("li")) == 3:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 7
  if input == "Phần tử ul có thẻ đóng":
    if soup.ul and source.count("</ul>") == len(soup.find_all("ul")):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 8
  if input == "Phần tử ol có thẻ đóng":
    if soup.ol and source.count("</ol>") == len(soup.find_all("ol")):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 9
  if input == "Phần tử li có thẻ đóng":
    if soup.li and source.count("</li>") == len(soup.find_all("li")):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 10
  if input == "Các phần tử li của danh sách không có thứ tự không được trống":
    if len(soup.find_all("ul")) != 1:
      return CheckerResult(False, 0, "")
    
    element = soup.ul

    lis = element.find_all("li")

    if len(lis) == 0:
      return CheckerResult(False, 0, "")

    for li in lis: 
      if li.text.strip() == "":
        return CheckerResult(False, 0, "")
    return CheckerResult(True, point_value, "")
  
  # criteria 11
  if input == "Các phần tử li của danh sách có thứ tự không được trống":
    if len(soup.find_all("ol")) != 1:
      return CheckerResult(False, 0, "")
    
    element = soup.ol

    lis = element.find_all("li")

    if len(lis) == 0:
      return CheckerResult(False, 0, "")

    for li in lis: 
      if li.text.strip() == "":
        return CheckerResult(False, 0, "")
    return CheckerResult(True, point_value, "")
  
  return CheckerResult(False, 0, "Lỗi checker")
```