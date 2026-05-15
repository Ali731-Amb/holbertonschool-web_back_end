import fs from 'fs';

function readDatabase(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf8', (err, data) => {
      if (err) {
        reject(err);
        return;
      }
      
      const lines = data.split('\n');
      const students = lines.slice(1);
      const newTab = students.filter((line) => line.trim());
      
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
      
      resolve(obj);
    });
  });
}

export default readDatabase;