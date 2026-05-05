export default function updateStudentGradeByCity(studentList, city, newGrades){
	const locations = studentList.filter(u => u.location == city)
	const grades = locations.map(u => {
		const grade = newGrades.find(g => g.studentId == u.id)
	return {...u, grade : grade ? grade.grade : 'N/A'}})
	return grades
}
