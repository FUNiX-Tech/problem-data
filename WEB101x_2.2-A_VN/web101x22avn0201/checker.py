from bs4 import BeautifulSoup
from dmoj.result import CheckerResult
  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  if soup.h1 and soup.h1.text == "Hello World":
    return CheckerResult(True, point_value, "")
  return CheckerResult(False, 0, "")