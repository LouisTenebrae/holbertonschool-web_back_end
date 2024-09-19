const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');

    const lines = data.split('\n').filter((line) => line.trim() !== '');

    const studentRows = lines.slice(1);

    const students = {};
    let totalStudents = 0;

    studentRows.forEach((row) => {
      const [firstname, lastname, age, field] = row.split(',');

      if (firstname && lastname && age && field) {
        if (!students[field]) {
          students[field] = [];
        }

        students[field].push(firstname.trim());
        totalStudents += 1;
      }
    });

    console.log(`Number of students: ${totalStudents}`);

    for (const [field, names] of Object.entries(students)) {
      console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
    }
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
