from bs4 import BeautifulSoup, Comment
from dmoj.result import CheckerResult
from dmoj.utils.unicode import utf8text
from dmoj.utils.css_parser import parse_css, get_element_css_value, count_element
  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')

  css = parse_css(soup)

  selectors = list(css.keys())
  
  # criteria 1
  if input == "h1 có font-weight 800":
    if count_element(soup, "h1") != 1:
      return CheckerResult(False, 0, "")

    element = soup.h1
    
    font_size = get_element_css_value(soup, element, "font-size")

    if font_size == "800" or font_size == "800 !important":
      return CheckerResult(True, point_value, "")
        
    return CheckerResult(False, 0, "")
    

  # criteria 2
  if input == "h2 có font-weight 600":
    if count_element(soup, "h2") != 1:
      return CheckerResult(False, 0, "")

    element = soup.h2
    
    font_size = get_element_css_value(soup, element, "font-size")

    if font_size == "600" or font_size == "600 !important":
      return CheckerResult(True, point_value, "")
        
    return CheckerResult(False, 0, "")
  
  # criteria 3
  if input == "h3 có font-weight 500":
    if count_element(soup, "h3") != 1:
      return CheckerResult(False, 0, "")

    element = soup.h3
    
    font_size = get_element_css_value(soup, element, "font-size")

    if font_size == "500" or font_size == "500 !important":
      return CheckerResult(True, point_value, "")
        
    return CheckerResult(False, 0, "")
  
  # criteria 4
  if input == "h4 có font-weight 400":
    if count_element(soup, "h4") != 1:
      return CheckerResult(False, 0, "")

    element = soup.h4
    
    font_size = get_element_css_value(soup, element, "font-size")

    if font_size == "400" or font_size == "400 !important":
      return CheckerResult(True, point_value, "")
        
    return CheckerResult(False, 0, "")
  
  # criteria 5
  if input == "h5 có font-weight 300":
    if count_element(soup, "h5") != 1:
      return CheckerResult(False, 0, "")

    element = soup.h5
    
    font_size = get_element_css_value(soup, element, "font-size")

    if font_size == "300" or font_size == "300 !important":
      return CheckerResult(True, point_value, "")
        
    return CheckerResult(False, 0, "")
  
  # criteria 6
  if input == "h6 có font-weight 200":
    if count_element(soup, "h6") != 1:
      return CheckerResult(False, 0, "")

    element = soup.h6
    
    font_size = get_element_css_value(soup, element, "font-size")

    if font_size == "200" or font_size == "200 !important":
      return CheckerResult(True, point_value, "")
        
    return CheckerResult(False, 0, "")
  
  return CheckerResult(False, 0, "Lỗi checker")