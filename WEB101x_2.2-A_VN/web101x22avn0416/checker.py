from bs4 import BeautifulSoup
from dmoj.result import CheckerResult
from dmoj.utils.css_parser import get_element_css_value
import re

red = [
  "red",
"#ff0000",
"#f00",
"rgb(255,0,0)",
"rgb(100%,0%,0%)",
"hsl(0,100%,50%)",
"hsl(0,100%,50%)",
"hsla(0,100%,50%,1)",
"hsla(0,100%,50%,1)"
]

orchid = [
  "orchid",
  "#DA70D6",
  "rgb(218,112,214)",
  "rgb(85%,44%,85%)",
  "hsl(302,59%,65%)",
  "hsla(302,59%,65%,1)"
]

blue = [
  "blue",
  "#0000FF",
  "#00F",
  "rgb(0,0,255)",
  "rgb(0%,0%,100%)",
  "hsl(240,100%,50%)",
  "hsla(240,100%,50%,1)"
]

sienna = [
  "sienna",
  "#A0522D",
  "rgb(160,82,45)",
  "rgb(63%,32%,18%)",
  "hsl(19,56%,40%)",
  "hsla(19,56%,40%,1)"
]

def tidy_color_value(color):
  color = re.sub(" !important", "", color)
  color = re.sub(" +", " ", color)
  return color

def structure_changed(soup):
  return \
    len(soup.find_all('h1', attrs={"class": "red-text"}, string='I am red!')) != 1 or \
    len(soup.find_all('h1', attrs={"class": "orchid-text"}, string='I am orchid!')) != 1 or \
    len(soup.find_all('h1', attrs={"class": "sienna-text"}, string='I am sienna!')) != 1 or \
    len(soup.find_all('h1', attrs={"class": "blue-text"}, string='I am blue!')) != 1

def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
  input = judge_input.decode('utf-8').strip()
  
  source = submission_source.decode('utf-8').strip()

  soup = BeautifulSoup(source, 'html.parser')
  
  if structure_changed(soup):
    return CheckerResult(False, 0, "")
  
  # criteria 1
  if input == "Thẻ h1 với nội dung I am red có màu red":
    
    h1 = soup.find("h1", string="I am red!")

    color = get_element_css_value(soup, h1, "color")

    color = tidy_color_value(color)

    print(color)
    if color in red:
      return CheckerResult(True, point_value, "")
    
    return CheckerResult(False, 0, "")

  # criteria 2
  if input == "Sử dụng rgb cho màu red":
    
    h1 = soup.find("h1", string="I am red!")

    color = get_element_css_value(soup, h1, "color")

    color = tidy_color_value(color)

    if color in ["rgb(255,0,0)", "rgb(100%,0%,0%)"]:
      return CheckerResult(True, point_value, "")
    
    return CheckerResult(False, 0, "")
  
  # criteria 3
  if input == "Thẻ h1 có nội dung I am orchid! có màu orchid":
    
    h1 = soup.find("h1", string="I am orchid!")

    color = get_element_css_value(soup, h1, "color")

    color = tidy_color_value(color)

    if color in orchid:
      return CheckerResult(True, point_value, "")
    
    return CheckerResult(False, 0, "")
  
  # criteria 4
  if input == "Sử dụng rgb cho màu orchid":
    
    h1 = soup.find("h1", string="I am orchid!")

    color = get_element_css_value(soup, h1, "color")

    color = tidy_color_value(color)

    if color in ["rgb(218,112,214)", "rgb(85%,44%,85%)"]:
      return CheckerResult(True, point_value, "")
    
    return CheckerResult(False, 0, "")
  
  # criteria 5
  if input == "Thẻ h1 có nội dung I am blue! có màu blue":
    
    h1 = soup.find("h1", string="I am blue!")

    color = get_element_css_value(soup, h1, "color")

    color = tidy_color_value(color)

    if color in blue:
      return CheckerResult(True, point_value, "")
    
    return CheckerResult(False, 0, "")

  # criteria 6
  if input == "Sử dụng rgb cho màu blue":
    h1 = soup.find("h1", string="I am blue!")

    color = get_element_css_value(soup, h1, "color")

    color = tidy_color_value(color)

    if color in ["rgb(0,0,255)", "rgb(0%,0%,100%)"]:
      return CheckerResult(True, point_value, "")
    
    return CheckerResult(False, 0, "")
  
  # criteria 7
  if input == "Thẻ h1 có nội dung I am sienna! có chữ màu sienna":
    
    h1 = soup.find("h1", string="I am sienna!")

    color = get_element_css_value(soup, h1, "color")

    color = tidy_color_value(color)

    if color in sienna:
      return CheckerResult(True, point_value, "")
    
    return CheckerResult(False, 0, "")
  
  # criteria 8
  if input == "Sử dụng rgb cho màu sienna":
    h1 = soup.find("h1", string="I am sienna!")

    color = get_element_css_value(soup, h1, "color")

    color = tidy_color_value(color)

    if color in ["rgb(160,82,45)", "rgb(63%,32%,18%)"]:
      return CheckerResult(True, point_value, "")
    
    return CheckerResult(False, 0, "")
  
  return CheckerResult(False, 0, "Lỗi checker")