export default function cleanSet(set, startString){
	if (!startString || typeof startString !== 'string'){
		return ""; 
		}
	const arr = [...set]
	const filtre = arr.filter(val => val.startsWith(startString))
	const map =filtre.map(val =>val.slice(startString.length))
	return map.join("-")
}
