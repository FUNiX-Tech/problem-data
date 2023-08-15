const fs = require("fs");

const LABS = [
  [2, 8],
  [3, 19],
  [4, 17],
  [5, 8],
  [6, 8],
  [7, 5],
  [8, 2],
  [9, 18],
  [10, 21],
  [11, 1],
];

const COURSE_NAME = "WEB101x_2.2-A_VN";

const PROBLEM_CODE_PREFIX = "web101x22avn";

const TEMPLATE_INIT_YML = `checker: checker.py
archive: criterias.zip
test_cases:
  - { in: criteria.1.in, points: 50 }
  - { in: criteria.2.in, points: 50 }`;

const TEMPLATE_DESC = `

  ---
  
  
  
  ---
  
  \`\`\`html
  
  \`\`\`
  `;

const TEMPLATE_CHECKER = `from bs4 import BeautifulSoup
  from dmoj.result import CheckerResult
  from dmoj.utils.unicode import utf8text
  from dmoj.utils.css_parser import parse_css
  
  def check(process_output, judge_output, judge_input, point_value, submission_source, **kwargs):
      input = judge_input.decode('utf-8').strip()
      
      source = submission_source.decode('utf-8').strip()
  
      soup = BeautifulSoup(source, 'html.parser')
      
      css = parse_css(soup)
          
      return CheckerResult(False, 0, "Lỗi checker")`;

function createSubfix(num1, num2) {
  const first = num1 < 10 ? "0" + String(num1) : String(num1);

  const last = num2 < 10 ? "0" + String(num2) : String(num2);

  return first + last;
}

LABS.forEach(([lessonNumber, totalLabs]) => {
  for (let i = 1; i <= totalLabs; i++) {
    const problemCode = PROBLEM_CODE_PREFIX + createSubfix(lessonNumber, i);

    fs.mkdirSync(problemCode);

    fs.writeFileSync(`${problemCode}/init.yml`, TEMPLATE_INIT_YML);

    fs.writeFileSync(`${problemCode}/description.md`, TEMPLATE_DESC);

    fs.writeFileSync(`${problemCode}/criteria.1.in`, "");

    fs.writeFileSync(`${problemCode}/checker.py`, TEMPLATE_CHECKER);

    fs.writeFileSync(`${problemCode}/name.txt`, "");
  }
});
