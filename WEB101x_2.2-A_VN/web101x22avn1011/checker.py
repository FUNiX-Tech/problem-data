from bs4 import BeautifulSoup, Comment
from dmoj.result import CheckerResult
from dmoj.utils.unicode import utf8text
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

  justify_items = container.get("justify-items")
  
  if justify_items == 'center':
    return CheckerResult(True, point_value, "")
  return CheckerResult(False, 0, "")
  