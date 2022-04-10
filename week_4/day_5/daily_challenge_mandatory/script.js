//Daily Challenge


//Create an array which value is the planets of the solar system.
const planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'];

//For each planet in the array, create a <div> using createElement.
//This div should have a class named "planet".

let text;
let newDiv;

for (value in planets){
	newDiv = document.createElement('div');
	text = document.createTextNode(planets[value]);
	newDiv.appendChild(text);
	document.getElementsByClassName("listPlanets")[0].appendChild(newDiv);
	newDiv.setAttribute('class', 'planet');
	newDiv.setAttribute('style', 'background');

}

//Each planet should have a different background color.
//(Hint: add a new class to each planet).
const colors = ['gray', 'white', 'blue', 'red', 'beige', 'beige', 'darkblue', 'darkblue']
for (i=0; i<colors.length; i++) {
document.getElementsByClassName("planet")[i].style.background=colors[i];
}
//Finally append each div to the <section> in the HTML (presented below).
//Already done above

//Bonus: Do the same process to create the moons.
//Be careful, each planet has a certain amount of moons. How should you display them?
//Should you still use an array for the planets ? Or an array of objects ?


// Create an array of objects
const moonsNumbers = [0, 0, 1, 2, 6, 6, 4, 3] // instead of [0, 0, 1, 2, 53, 53, 27, 14] of confirmed moons
const planetsObj=[];
for (i=0;i<planets.length;i++){
	planetsObj.push({name: planets[i], color: colors[i], moonsNumber: moonsNumbers[i]})
}
console.log(planetsObj) //just to check

//For each moon of each planet in the array, create a <div> using createElement.
//This div should have a class named "moon".

let text2;
let newDiv2;
let objMoonsNumber;

for (let j=0; j<planetsObj.length;j++){
	objMoonsNumber = planetsObj[j].moonsNumber; //Number of moons of planet in j position in the array
	console.log(objMoonsNumber)
	for(let k=0; k<objMoonsNumber;k++){
	newDiv2 = document.createElement('div');
	document.getElementsByClassName("planet")[j].appendChild(newDiv2);
	newDiv2.setAttribute('class', 'moon');
	}	
	
}

//Display remains to be done : when I find some available time !!!