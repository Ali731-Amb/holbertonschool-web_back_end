const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }
      const lines = data.split('\n');
      const students = lines.slice(1);
      const newTab = students.filter((line) => line.trim());
      let output = '';
      output += `Number of students: ${newTab.length}\n`;
      const obj = {};
      newTab.forEach((line) => {
        const student = line.split(',');
        const firstname = student[0];
        const field = student[3];
        if (!obj[field]) {
          obj[field] = [];
        }
        obj[field].push(firstname);
      });
      Object.keys(obj).forEach((field) => {
        output += `Number of students in ${field}: ${obj[field].length}. List: ${obj[field].join(', ')}\n`;
      });
      resolve(output.trim);
    });
  });
}

module.exports = countStudents;
