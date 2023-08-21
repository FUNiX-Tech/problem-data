from bs4 import BeautifulSoup
from dmoj.result import CheckerResult
from dmoj.utils.css_parser import parse_css
from dmoj.utils.chrome_driver import get_driver
from selenium.webdriver.common.action_chains import ActionChains
  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  if len(soup.find_all("a")) != 1:
    return CheckerResult(False, 0, "")
  
  # criteria 1
  if input == "Thẻ a giữ nguyên màu đen, chỉ thêm CSS cho trạng thái :hover":
    driver = get_driver(source)

    element = driver.find_element_by_tag_name("a")

    css = "" if element is None else driver.get_computed_style(element,"color")

    if css == "rgb(0, 0, 0)":
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Thẻ a có chữ màu xanh (blue) khi hover":
    driver = get_driver(source)

    element = driver.find_element_by_tag_name("a")

    if element is None: 
      return CheckerResult(False, 0, "")

    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

    css = driver.get_computed_style(element, "color")

    driver.quit()

    if css == "rgb(0, 0, 255)":
      return CheckerResult(True, point_value, "")
    return CheckerResult(False, 0, "")
  
  return CheckerResult(False, 0, "Lỗi checker")