from bs4 import BeautifulSoup
from dmoj.result import CheckerResult
from dmoj.utils.css_parser import parse_css
import re

def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  css = parse_css(soup)  
  
  container = css.get(".container")
  
  if container is None: 
    return CheckerResult(False, 0, "")

  grid_template_columns = container.get("grid-template-columns")
  
  if grid_template_columns is None:
    return CheckerResult(False, 0, "")

  if re.fullmatch(r"\s?repeat\s?\(\s?3\s?,\s?1fr\s?\)\s?", grid_template_columns):
    return CheckerResult(True, point_value, "")
  return CheckerResult(False, 0, "")
  