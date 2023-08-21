from bs4 import BeautifulSoup
from dmoj.result import CheckerResult
from dmoj.utils.chrome_driver import get_driver
  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  # criteria 1
  if input == ".follow-btn được hiển thị trên trang. Hãy đảm bảo rằng bạn đã tắt các tiện ích mở rộng như ad blockers":
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
  if input == "header có display flex":
    if len(soup.find_all("header")) != 1:
      return CheckerResult(False, 0, "")
    
    driver = get_driver(source)
    
    element = driver.find_element_by_tag_name("header")
    
    css = driver.get_computed_style(element, 'display')
    
    driver.quit()

    if css == 'flex':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 3
  if input == "footer có display flex":
    if len(soup.find_all("footer")) != 1:
      return CheckerResult(False, 0, "")

    driver = get_driver(source)
    
    element = driver.find_element_by_tag_name("footer")
    
    css = driver.get_computed_style(element, 'display')
    
    driver.quit()

    if css == 'flex':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 4
  if input == "h3 có display flex":
    if len(soup.find_all("h3")) != 1:
      return CheckerResult(False, 0, "")

    driver = get_driver(source)
    
    element = driver.find_element_by_tag_name("h3")
    
    css = driver.get_computed_style(element, 'display')
    
    driver.quit()

    if css == 'flex':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 5
  if input == "h4 có display flex":
    if len(soup.find_all("h4")) != 1:
      return CheckerResult(False, 0, "")

    driver = get_driver(source)
    
    element = driver.find_element_by_tag_name("h4")
    
    css = driver.get_computed_style(element, 'display')
    
    driver.quit()

    if css == 'flex':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 6
  if input == ".profile-name có display flex":
    if len(soup.find_all(attrs={"class":"profile-name"})) != 1:
      return CheckerResult(False, 0, "")
    
    driver = get_driver(source)
    
    element = driver.find_element_by_class_name("profile-name")
    
    css = driver.get_computed_style(element, 'display')
    
    driver.quit()

    if css == 'flex':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 7
  if input == ".follow-btn có display flex":
    if len(soup.find_all(attrs={"class":"follow-btn"})) != 1:
      return CheckerResult(False, 0, "")
    
    driver = get_driver(source)
    
    element = driver.find_element_by_class_name("follow-btn")
    
    css = driver.get_computed_style(element, 'display')
    
    driver.quit()

    if css == 'flex':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  # criteria 8
  if input == ".stats có display flex":
    if len(soup.find_all(attrs={"class":"stats"})) != 1:
      return CheckerResult(False, 0, "")
    
    driver = get_driver(source)
    
    element = driver.find_element_by_class_name("stats")
    
    css = driver.get_computed_style(element, 'display')
    
    driver.quit()

    if css == 'flex':
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  return CheckerResult(False, 0, "Lỗi checker")