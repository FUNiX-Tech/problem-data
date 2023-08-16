from bs4 import BeautifulSoup, Comment
from dmoj.result import CheckerResult
from dmoj.utils.unicode import utf8text
from dmoj.utils.css_parser import parse_css
  
def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  # criteria 1
  if input == "Chỉ có một thẻ a trong trang web":
    
    if len(soup.find_all("a") == 1):
      
      return CheckerResult(True, point_value, "")
    
    else:
      
      return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Chỉ có một thẻ footer trong trang web":
    
    if len(soup.find_all("footer") == 1):
      
      return CheckerResult(True, point_value, "")
    
    else:
      
      return CheckerResult(False, 0, "")
  
  # criteria 3
  if input == "Thẻ a có href attribute với giá trị là '#footer'":
    
      if len(soup.find_all("a") != 1):
        
        return CheckerResult(False, 0, "")
      
      a = soup.a

      if a.get("href") == "#footer":
        
        return CheckerResult(True, point_value, "")
        
      return CheckerResult(False, 0, "")
  
  # criteria 4
  if input == "Thẻ a không có attribute target":
      if len(soup.find_all("a") != 1):
        
        return CheckerResult(False, 0, "")
      
      if soup.a.get("atrget") is None:
      
        return CheckerResult(True, point_value, "")

      return CheckerResult(False, 0, "")
  
  # criteria 5
  if input == "Nội dung thẻ a là 'Jump to Bottom'":
    if len(soup.find_all("a") != 1):
        
      return CheckerResult(False, 0, "")

    if soup.a.text == "Jump to Bottom":
      
      return CheckerResult(True, point_value, "")
    
    return CheckerResult(False, 0, "")
  
  # criteria 6
  if input == "Thẻ footer có id 'footer'":
    if len(soup.find_all("footer") != 1):
      
      return CheckerResult(False, 0, "")
    
    if soup.footer.get("id") == "footer":
      
      return CheckerResult(True, point_value, "")
    
    return CheckerResult(False, 0, "")
  
  return CheckerResult(False, 0, "Lỗi checker")