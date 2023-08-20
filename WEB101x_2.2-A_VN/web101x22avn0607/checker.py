from bs4 import BeautifulSoup, Comment
from dmoj.result import CheckerResult
from dmoj.utils.unicode import utf8text
from dmoj.utils.css_parser import parse_css, get_element_css_value
from dmoj.utils.chrome_driver import get_driver
  
def structure_changed(soup):
  return soup.find_all("img", alt="A cute orange cat lying on its back.", src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg" ) != 1

  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  if structure_changed(soup):
    return CheckerResult(False, 0, "")
  
  # criteria 1
  if input == "Phần tử img có class smaller-image":
    img = soup.img
    if "smaller-image" in img.get("class"):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Phần tử img rộng 100 pixels":
    driver = get_driver(source)
    
    blue_box = driver.get_element_by_tag_name("img")
    
    css = driver.get_computed_style(blue_box, 'width')
    
    driver.quit()

    if css == '100px':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  return CheckerResult(False, 0, "Lỗi checker")