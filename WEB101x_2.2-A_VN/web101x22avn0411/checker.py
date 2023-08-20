from bs4 import BeautifulSoup
from dmoj.result import CheckerResult
from dmoj.utils.chrome_driver import get_driver
  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  # criteria 1
  if input == "Phần tử form có id cat-photo-form":
    if soup.find("form", id="cat-photo-form"):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Phần tử form có background-color là green":
    if len(soup.find_all("form")) != 1:
      return CheckerResult(False, 0, "")
      
    driver = get_driver(source)
    
    element = driver.find_element_by_tag_name("form")

    css = driver.get_computed_style(element, 'background-color') if element is not None else None

    driver.quit()
    
    if css == "rgb(0, 128, 0)":
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 3
  if input == "Phần tử form được đặt attribute id":
    if soup.find("form", id=True):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 4
  if input == "Không đặt class hoặc style attribute cho phần tử form":
    if len(soup.find_all("form")) != 1:
      return CheckerResult(False, 0, "")
    
    form = soup.form
    
    if form.get("class") is not None or form.get("style") is not None:
      return CheckerResult(False, 0, "")
      
    return CheckerResult(True, point_value, "")
  
  return CheckerResult(False, 0, "Lỗi checker")