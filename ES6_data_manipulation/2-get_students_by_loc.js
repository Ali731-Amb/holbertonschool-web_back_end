export default function getStudentsByLocation(ListStudents, city){
	const locations = ListStudents.filter(u => u.location == city)
	return locations
}
