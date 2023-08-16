from bs4 import BeautifulSoup
from dmoj.result import CheckerResult
from dmoj.utils.unicode import utf8text
from dmoj.utils.css_parser import parse_css

def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
    input = judge_input.decode('utf-8').strip()
    
    source = submission_source.decode('utf-8').strip()

    soup = BeautifulSoup(source, 'html.parser')
    
    if len(soup.find_all("a")) != 1:
      
      return CheckerResult(False, 0, "")
    
    a = soup.a

    if a.get("href") != "#":
      
      return CheckerResult(False, 0, "")
    
    return CheckerResult(True, point_value, "")