const fs = require('fs');
let data;

function countStudents(path) {
  try {
data = fs.readFileSync(path, 'utf8');
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
obj[field].push(firstname);});
Object.keys(obj).forEach((field) => {
  console.log(`Number of students in ${field}: ${obj[field].length}. List: ${obj[field].join(',')}`)
});
} catch (err) {
throw new Error('Cannot load the database');
}
}

module.exports = countStudents;