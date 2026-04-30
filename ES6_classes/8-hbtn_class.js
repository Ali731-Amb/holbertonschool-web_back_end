class HolbertonClass{
	constructor(size, location){
		if (typeof size !== 'number') throw new TypeError('Size must be a number')
		if (typeof location !== 'string') throw new TypeError('Location must be a string')
			this._size = size
			this._location = location
	}
	get [Symbol.toPrimitive]() {
    return (hint) => {
        if (hint === 'number') return this._sizesize
        if (hint === 'string') return this._location
    }
}
}