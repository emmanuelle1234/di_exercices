//Exercise 1


//1. In the <div> above, change the value of the id attribute from navBar to 
//socialNetworkNavigation, using the setAttribute method.

let newDiv = document.getElementById("navBar");
newDiv.setAttribute("id","socialNetworkNavigation");
console.log(newDiv);

//2. We are going to add a new <li> to the <ul>.
//a. First, create a new <li> tag (use the createElement method)
let newLi = document.createElement('li');
//b. Create a new text node with “Logout” as its specified text.
let newTextNode = document.createTextNode('Logout');
//c. Append the text node to the newly created list node (li).
newLi.appendChild(newTextNode);
//d. Finally, append this updated list node to the
// unordered list above, using the appendChild method.
let Ul = document.getElementsByTagName('ul')[0];
console.log(Ul); // just to check
Ul.appendChild(newLi);
console.log(document); // just to check

//3. Bonus : use the firstElementChild and the lastElementChild properties to retrieve the first
//and last li elements from their parent element (ul). Display the text of each link. 
//Hint: use the textContent property).
console.log(Ul.firstElementChild.textContent);
console.log(Ul.lastElementChild.textContent);

//Exercise 2

//1. In the HTML above change the name “Pete” to “Richard”.
let nameList1 = document.getElementsByClassName('list')[0];
nameList1.lastElementChild.textContent = "Richard";
console.log(nameList1.lastElementChild.textContent); // just to check

//2. Change each first name of the two <ul>'s to your name.
let nameList = document.getElementsByClassName('list'); // ul collection

for(value of nameList){
	value.firstElementChild.textContent = "Emmanuelle";
}

//3. At the end of each <ul> add a <li> that says “Hey students”.
	

for(value of nameList){
	let newLi2 = document.createElement('li'); // creates new li
	let newText2 = document.createTextNode('Hey students'); // creates new text
	newLi2.appendChild(newText2); // inputs the text in the li
	value.appendChild(newLi2); // inputs the li in each ul
}

//4. Delete the name Sarah from the second <ul>.
nameList[1].removeChild(nameList[1].getElementsByTagName('li')[1]); //removes the 2nd li of the 2nd ul

//5. Bonus
//    Add a class called student_list to both of the <ul>'s.
for(value of nameList){
	value.setAttribute('class','list student_list');
}

//    Add the classes university and attendance to the first <ul>.
nameList[1].setAttribute('class','list student_list university attendance');

console.log(nameList[0]);
console.log(nameList[1]);

//Exercise 3

//Add a “light blue” background color and some padding to the <div>.
document.getElementById('ex3').setAttribute('style', 'background:lightblue; padding:10px')

//Do not display the first name (John) in the list.
document.getElementById('ex3').nextElementSibling.firstElementChild.setAttribute('style', "display:none");
//Add a border to the second name (Pete).
document.getElementById('ex3').nextElementSibling.lastElementChild.setAttribute('style', 'border:3px solid');
//Change the font size of the whole body
document.body.setAttribute('style', 'font-size:10px'); 

//Bonus: If the background color of the div is “light blue”, 
//alert “Hello x and y” (x and y are the users in the div).
if (document.getElementById('ex3').style.background==='lightblue'){
	alert (`Hello ${document.getElementById('ex3').nextElementSibling.firstElementChild.textContent} and ${document.getElementById('ex3').nextElementSibling.lastElementChild.textContent}`)
}
//Why it doesn't work with background-color:lightblue ??
