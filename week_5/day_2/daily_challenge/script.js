//Week 5 Day 2 Daily Challenge//

//1. Get the value of each of the inputs in the HTML file when the button is clicked.
//2. Make sure the values are not empty
//3. Write a story that uses each of the values.
//4. Make sure you check the console for errors when playing the game.
//5. Bonus: Add a “shuffle” button to the HTML file, when clicked the button 
//should change the story currently displayed (but keep the values entered by the user). 
//The user could click the button at least three times and get a new story. Display the stories randomly.
const button = document.querySelector('button');

let nounInput = document.querySelector('#noun');
let adjectiveInput = document.querySelector('#adjective');
let personInput = document.querySelector('#person');
let verbInput = document.querySelector('#verb');
let placeInput = document.querySelector('#place');
let answersInput = [nounInput, adjectiveInput, personInput, verbInput, placeInput];
let answersInputValue =[];
let generatedStory="";

let span = document.querySelector('span');
let newPara = document.createElement('p');
span.appendChild(newPara);

function storydefine(n){ 
//sorry but I have no more courage to re-invent stories
let story0=`Ha ha ${answersInputValue[0]} ${answersInputValue[1]} ${answersInputValue[2]} together with the girl ${answersInputValue[3]} ${answersInputValue[4]}`;
let story1=`Yes ${answersInputValue[1]} ${answersInputValue[1]} ${answersInputValue[3]} along with ${answersInputValue[2]} at ${answersInputValue[4]}`;
let story2=`Lorem ${answersInputValue[4]} if ${answersInputValue[3]} ${answersInputValue[2]} or ${answersInputValue[1]} ${answersInputValue[0]}`;
let story3=`Ipsum ${answersInputValue[3]} ${answersInputValue[2]} hello ${answersInputValue[4]} because of ${answersInputValue[1]} ${answersInputValue[0]}`;
let story4=`This mad story ${answersInputValue[2]} very much ${answersInputValue[4]} around ${answersInputValue[3]} in ${answersInputValue[0]} tomorrow${answersInputValue[1]}`;
let list = [story0, story1, story2, story3, story4];
return list[n];
}

function check2(array){
 	if (array.includes("")) {
 		return false
 		}  return true
}

function check(x){

 if (x.value==""){
 	x.placeholder="Please enter something"
 } 
 getInput(x)
}

function getInput(y){
	answersInputValue.push(y.value);

}

function getInputs(){
	answersInput.forEach(x => check(x))

}

function storygenerate(n){
	getInputs();
	console.log(answersInputValue)
	storydefine(n);
	return storydefine(n);
}

function display(){
	answersInputValue=[]
	generatedStory=""
	generatedStory=storygenerate(0);
	if (check2(answersInputValue)){
	newPara.textContent=generatedStory;
	} else{
	newPara.textContent="";
	}
}

button.addEventListener("click", display);

//Bonus

let button2 ;
button2 = document.createElement('button');
let newPara2 = document.createElement('p');
span.appendChild(newPara2);
newPara2.appendChild(button2);
const button2Text=document.createTextNode("Shuffle!");
button2.appendChild(button2Text);

button2.addEventListener("click", display2);

function display2(){		
	answersInputValue=[]
	generatedStory=""
	generatedStory=storygenerate(randomstory());
	if (check2(answersInputValue)){
	newPara.textContent=generatedStory;
	} else{
	newPara.textContent="";
	}
}

function randomstory(){
	return Math.floor(Math.random() * (4 - 1) ) + 1;
}
