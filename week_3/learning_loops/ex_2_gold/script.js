//Exercises XP Gold//
//Exercise 1//

let numbers = [123, 8409, 100053, 333333333, 7]
let bool = false;
for (let i=0; i<numbers.length; i++){
	if (numbers[i]%3 ==0){
	bool = true;
	} else
	bool = false;
	console.log(bool)
}

//Exercise 2//
let guestList = {
  randy: "Germany",
  karla: "France",
  wendy: "Japan",
  norman: "England",
  sam: "Argentina"
}

let name = prompt("Please enter your name");
let i = name.toLowerCase();
if (i in guestList) {
	console.log(`Hi! I\'m ${i.substring(0,1).toUpperCase()}${i.substring(1)}, and I\'m from ${guestList[i]}`);
} else {
	console.log(`Hi! I\'m a guest`);
}

//Exercise 3//
let age = [20,5,12,43,98,55];
let sum =0; //to be declared before initialization
for (let i=0; i<age.length; i++){
	sum = sum + age[i];
}
age.push(sum);
console.log(age);
age.pop();
console.log(age);
let highest = 0;
for (let i=1; i<age.length; i++){
	if (age[i]>age[i-1]) {
		highest = age[i];
	} else {
		highest = age[i-1]
	}
}
console.log(highest);