//Exercises XP Ninja//
//Exercise 1//

let Person1 = {
	FullName: "Scarlett O'Hara",
	Mass: 45, // in kg
	Height: 166, // in cm
};
let Person2 = {
	FullName: "Gérard Depardieu",
	Mass: 173, // in kg
	Height: 180, // in cm
};
function bodyMassIndex (m, h) {
	index = m/(h*h*0.0001);
	return index;
};
Person1.BMI=bodyMassIndex(Person1.Mass, Person1.Height).toFixed(2);
Person2.BMI=bodyMassIndex(Person2.Mass, Person2.Height).toFixed(2);
//console.log(Person2);

function bodyMassIndexComparator (index1, index2) {
	let largest ="";
	let person = "";
	if (index1<index2){
		largest=index2; // in case we need it for an other reason
		person=Person2.FullName
	} else if (index1>index2){
		largest=index1; // in case we need it for an other reason
		person=Person1.FullName
	} else {
		largest="BMI are equals"; // in case we need it for an other reason
		person="no one";
	}
	return person;
};
console.log(`The person who has the largest BMI is ${bodyMassIndexComparator(Person1.BMI, Person2.BMI)}`);

//Exercise 2//
//Version1
let	gradesList = [90, 89, 99, 100, 12];
let average;
function findAvg (gradesList) {
	let sum=0;
	for (let i=0;i<gradesList.length; i++){
		sum=sum+gradesList[i];
	}
	average=sum/gradesList.length;
	return average.toFixed(2);
}
console.log(findAvg(gradesList));
if(average<65){
	alert("Sorry but you failed, you should repeat the course.")
} else {
	alert("Congratulations, you passed.")
}
//Improved version
gradesList = []; // already declared in firt version
length = prompt("Please enter the number of grades you have in order to calculate their average");
for(i = 0; i<length; i++) {
	let grade =prompt("Please enter a grade (a number)");//check with isNaN an other time!
	gradesList.push(Number(grade));
}
console.log(gradesList);
average=0;//average already declared in firt version
let list;
function findAvg (list) {
	let sum=0;
	for (i in list){
		sum=sum+list[i];
	}
	average=sum/list.length;
	return average.toFixed(2);
};
function test (average) {
	if(average<65){
	result ="Sorry but you failed, you should repeat the course."
	} else {
	result = "Congratulations, you passed."
	}
	return result;
}

alert(`With your grades (${gradesList}), your average is ${findAvg(gradesList)}. ${test(average)} `)

