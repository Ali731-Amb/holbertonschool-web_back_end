export default function getStudentIdsSum(listStudents){
	return listStudents.reduce((acc, val) => acc + val.id, 0)
}
