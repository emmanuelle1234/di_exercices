//Exercises XP Gold//
//Exercise 1//

let ask = prompt("Which language do you speak?");
let lang = ask.toLowerCase();
/*Could be in addition (not asked in the instructions)
let space = / /gi;
let lang2 = ask.replace(space,'');
//with lang2 below*/

switch (lang){
	case "english" :
	console.log("Hello");
	break;
	case "french" :
	console.log("Bonjour");
	break;
	case "hebrew" :
	console.log("Shalom");
	break;
	default:
	console.log("01110011 01101111 01110010 01110010 01111001");
	break;
}

//Exercise 2//

let input = prompt("What is your grade?");
let grade = Number(input);
if (grade <70){
	console.log("D");
} else if (grade <= 80) {
	console.log("C");
} else if (grade <=90) {
	console.log("B");
}
else if (grade >90) {
	console.log("A");
}
else {
	console.log("This is not a grade");
}




//Exercise 3//
//impossible de faire des règles, dans un exercice simple, pour couvrir tous les cas de figure des terminaisons
//ex : to dive -> diving mais to be -> being 
//ex : to get -> getting mais to shout -> shouting
//ex : ing is not a termination for the verbe to sing

let verb = prompt("Please enter a verb");
let length = verb.length ;
let last3 = verb.slice(-3) ;
let voyel ="a" || "e" || "i" || "o" || "u" || "y"
let cons = "m"
let last = verb.slice(-1) ;
if (length>=3 && last3!="ing" && last==voyel) {
	console.log(verb+"ing");
	} else if (length>=3 && last3!="ing" && last==cons  ){
	console.log(verb+cons+"ing");
	} else if (length>=3 && last3!="ing"){
	console.log(verb+"ing");
	} else if (length>=3) {
	console.log(verb+"ly");	
	}
	else {
	console.log(verb);	
	}


