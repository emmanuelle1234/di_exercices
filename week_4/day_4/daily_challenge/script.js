//Daily Challenge//


// console.log one stanza
function stanza(getNumber, counter) {
	if (getNumber-counter===1){
	text = `${getNumber} bottles of beer on the wall\n${getNumber} bottles of beer\nTake ${counter} down, pass it around\n${getNumber-counter} bottle of beer on the wall`
	console.log(text) ;
	} else {
	text = `${getNumber} bottles of beer on the wall\n${getNumber} bottles of beer\nTake ${counter} down, pass it around\n${getNumber-counter} bottles of beer on the wall`
	console.log(text) ;
	}
	return 
}

function loopTest(getNumber, counter){
	 if (getNumber > counter) {
	 	stanza (getNumber, counter);
	 	return true;
	 } else {
		return false
	 }
}
// Loop and manage specific cases : 1 at the start and others at the end of the loop
function loop(getNumber, counter, text){
	
	do {
	getNumber=getNumber-counter;
	counter++;
	} while (loopTest(getNumber, counter)===true)


	//while (loopTest(getNumber, counter)===true){
	//	getNumber=getNumber-counter;
	//	counter++;
	//}

	if (loopTest(getNumber, counter)===false){
		if (getNumber===1 && counter===1){
		text = `${getNumber} bottle of beer on the wall\n${getNumber} bottle of beer\nTake ${counter} down, pass it around\n${getNumber-counter} bottle of beer on the wall`
		console.log(text)
		}else if (getNumber===counter && getNumber === 1){
		text = `${getNumber} bottle of beer on the wall\n${getNumber} bottle of beer\nTake ${counter} down, pass it around ??\n${getNumber-counter} bottle of beer on the wall!!`
		console.log(text)
		} else if (getNumber===counter && getNumber != 1) {
		text = `${getNumber} bottles of beer on the wall\n${getNumber} bottles of beer\nTake ${counter} down, pass it around\n${getNumber-counter} bottle of beer on the wall`
		console.log(text) ;
		} else if (getNumber < counter && getNumber === 1){
		text = `${getNumber} bottle of beer on the wall\n${getNumber} bottle of beer\nTake ${counter} down, pass it around ??\nNo bottle of beer on the wall!!`
		console.log(text)
		} else if (getNumber < counter && getNumber != 1) {
		text = `${getNumber} bottles of beer on the wall\n${getNumber} bottles of beer\nTake ${counter} down, pass it around ??\nNo bottle of beer on the wall!!`
		console.log(text)	
		}
	}
}

// console log the whole song
function song() {
	let getNumber = prompt("Let\'s sing. Please enter a number to start the song with.");
	let counter = 0 ;
	let text ="";
	loop(getNumber, counter, text);
	
}
song()


