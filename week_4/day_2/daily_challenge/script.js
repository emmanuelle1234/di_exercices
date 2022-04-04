//Exercise 1//
let sentence = prompt("Please enter several words separated by commas")
let array = sentence.split(',');

function longestLength () {
	let arrayLongestLength=0;
	let arrayLongestWord;
	for (i=0;i<array.length;i++){
		if (arrayLongestLength<array[i].length){
			arrayLongestLength=array[i].length;
			arrayLongestWord=array[i];
		} 
	}
	return arrayLongestLength;
}
let lineLength = longestLength()+4;


let starLine ="*";
for (i=0;i<lineLength-1;i++){
	starLine= starLine+"*";
}


//Required space after the word

function spaceLength(a){
	return lineLength - array[a].length - 3;
	}


//Display
console.log(starLine);
for (let j = 0; j<array.length; j++){
	console.log(`* ${array[j]}${" ".repeat(spaceLength(j))}*`);
} 
console.log(starLine);

