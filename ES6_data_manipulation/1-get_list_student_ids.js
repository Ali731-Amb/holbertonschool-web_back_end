export default function getListStudentsIds(StudentsList){
	if (!Array.isArray(StudentsList))
		return []
	const ids = StudentsList.map(u => u.id)
	return ids
}
