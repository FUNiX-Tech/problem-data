from bs4 import BeautifulSoup, Comment
from dmoj.result import CheckerResult
from dmoj.utils.css_parser import parse_css, parse_inline_css, get_higher_priority_css
  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  if len(soup.find_all("p")) != 1:
    return CheckerResult(False, 0, "")

  css = parse_css(soup)
  

  inline_css = parse_inline_css(soup.p)
  
  
  p_color_css_value = get_higher_priority_css(css.get('p') and css.get('p').get('font-size'), inline_css.get("font-size"))

  if p_color_css_value == "16px" or p_color_css_value == "16px !important":
    return CheckerResult(True, point_value, "")


  return CheckerResult(False, 0, "")