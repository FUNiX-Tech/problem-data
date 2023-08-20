const fs = require("fs");

for (i = 2; i <= 44; i++) {
  fileName = `criteria.${i}.in`;
  fs.writeFileSync(fileName, "");
  console.log(`create ${fileName}`);
}
