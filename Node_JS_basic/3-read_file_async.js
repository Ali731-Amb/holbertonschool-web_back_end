const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {          // 1. ouvre Promise

    fs.readFile(path, 'utf8', (err, data) => {         // 2. ouvre callback

      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n');
      const students = lines.slice(1);
      const newTab = students.filter((line) => line.trim());

      console.log(`Number of students: ${newTab.length}`);

      const obj = {};
      newTab.forEach((line) => {
        const student = line.split(',');
        const firstname = student[0];
        const field = student[3];
        if (!obj[field]) {
          obj[field] = [];
        }
        obj[field].push(firstname);
      });                                                    // 3. ferme forEach

      Object.keys(obj).forEach((field) => {
        console.log(`Number of students in ${field}: ${obj[field].length}. List: ${obj[field].join(', ')}`);
      });                                                    // 4. ferme forEach

      resolve();                                           // ✅ après les forEach

    });                                                      // 5. ferme callback readFile
  });                                                        // 6. ferme Promise
}

module.exports = countStudents;