from bs4 import BeautifulSoup
from dmoj.result import CheckerResult
from dmoj.utils.chrome_driver import get_driver
  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')

  # criteria 1
  if input == "Tạo 1 thẻ h1":
    if len(soup.find_all("h1")) == 1:
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Thẻ h1 có nội dung Hello World":
    if soup.find("h1", string="Hello World"):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 3
  if input == "Thẻ h1 có thẻ đóng":
    if soup.h1 and len(soup.find_all("h1")) == source.count("</h1>"):
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 4
  if input == "Thẻ body có color là green":
    driver = get_driver(source)
    element = driver.find_element_by_tag_name("body")
    css = driver.get_computed_style(element, 'color')
    driver.quit()

    if css == "rgb(0, 128, 0)":
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 5
  if input == "Thẻ body có font-family là monospace":
    driver = get_driver(source)
    element = driver.find_element_by_tag_name("body")
    css = driver.get_computed_style(element, 'font-family')
    driver.quit()
    
    if css == "monospace":
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 6
  if input == "Thẻ h1 thừa kế font monospace từ thẻ body":
    if len(soup.find_all("h1")) != 1:
      return CheckerResult(False, 0, "")

    driver = get_driver(source)
    element = driver.find_element_by_tag_name("h1")
    css = driver.get_computed_style(element, 'font-family')
    driver.quit()
    
    if css == "monospace":
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 7
  if input == "Thẻ h1 thừa kế màu chữ là màu xanh (green) từ thẻ body":
    if len(soup.find_all("h1")) != 1:
      return CheckerResult(False, 0, "")
      
    driver = get_driver(source)
    element = driver.find_element_by_tag_name("h1")
    css = driver.get_computed_style(element, 'color')
    driver.quit()
    
    if css == "rgb(0, 128, 0)":
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  return CheckerResult(False, 0, "Lỗi checker")