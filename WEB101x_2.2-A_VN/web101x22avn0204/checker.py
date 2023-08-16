from bs4 import BeautifulSoup
from dmoj.result import CheckerResult
  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  if soup.p and soup.p.text == "Kitty ipsum dolor sit amet, shed everywhere shed everywhere stretching attack your ankles chase the red dot, hairball run catnip eat the grass sniff.":
    return CheckerResult(True, point_value, "")
  else:
    return CheckerResult(False, 0, "")
  