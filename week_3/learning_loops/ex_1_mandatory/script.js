alert("Enter numbers superior to 10 if you want to avoid a mess (see exercise3)");
//Exercise 1//
//Part I
let people = ["Greg", "Mary", "Devon", "James"];
let n = people.indexOf("Greg") ; // otherwise directly people.shift();
people.splice(n,1);
console.log(people);
let m = people.indexOf("James") ;
people.splice(m, 1, "Jason");
console.log(people);
people.push("Emmanuelle");
console.log(people);
console.log(people.indexOf("Mary"));
console.log(people.indexOf("Emmanuelle"));
console.log(people.slice(1,3)); // neither "Mary" nor "Emmanuelle" (or is confusing)
console.log(people);//should be different from above as slice created a new array
console.log(people.indexOf("Foo")); //should be -1 because Foo is not an element of the array
let last = people.slice(people.length-1,people.length);
console.log(last);
last = last.toString() ; // not sure if they wanted an array (above) or a string
console.log(last);
//Part II

for(let i=0; i<people.length; i++){
    console.log (people[i]);
}

for(let i=0; i<people.length; i++){
    console.log (people[i]);
    if (people[i]=="Jason") {
        break;
    } 
}

//Exercise 2//
let colors = ["Blue", "Light blue", "Turquoise", "Aqua", "Aquamarine"];
let l = colors.length
for(let i=0; i<l; i++){
    console.log (`My #${i+1} choice is ${colors[i]}`);
}
//if there are more than 3 colors in the array
let firstSuffixes =["st", "nd", "rd"];
let otherSuffixes=[];
for (i=0; i<l-3; i++) {
    otherSuffixes.push("th");}
console.log(otherSuffixes);
let suffixes=firstSuffixes.concat(otherSuffixes);
console.log(suffixes);
for(let i=0; i<l; i++){
    console.log (`My ${i+1}${suffixes[i]} choice is ${colors[i]}`);
}

//Exercise 3//
//version 1
let num=prompt("Please enter a number");
console.log (typeof num);//not understood the interest of this method because prompt always fives a string
//let's assume below the guy will finish by understand that a number is required (to avoid an index on the number of tempatives with a NaN !) :
while ((isNaN(num)) || (num<10)) { 
    num=prompt("Please enter a new number");
    }
//version 2 : less lines but only one question
//let num; as a comment because already declared in version 1
do {
num=prompt("Please enter a number");
console.log (typeof num);//still not understood the interest but as it is asked, I do obey...
}
while ((isNaN(num)) || (num<10));

//Exercise 4//
let building = {
    numberOfFloors : 4,
    numberOfAptByFloor : {
        firstFloor : 3,
        secondFloor : 4,
        thirdFloor : 9,
        fourthFloor : 2,
    },
    nameOfTenants : ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan :  [4, 1000],
        david : [1, 500],
    },
}
console.log(building.numberOfFloors);
console.log(`There are ${building.numberOfAptByFloor.firstFloor} apartments in the first floor and ${building.numberOfAptByFloor.thirdFloor} apartments in the third one`);

//to be able to generalize beyond what is asked for Dan
function numberOfRoomsOrRentFunction (n,m) {
    let a =building.nameOfTenants[n];
    a =a.toLowerCase();
    b=building.numberOfRoomsAndRent[a];
    c=b[m];
    return c;
}
console.log(`${building.nameOfTenants[1]} has ${numberOfRoomsOrRentFunction(1,0)} rooms in his/her apartment.`) ;

//here again to be able to generalize later on beyond what is asked for Dan
if (numberOfRoomsOrRentFunction(0,1)+numberOfRoomsOrRentFunction(2,1)>numberOfRoomsOrRentFunction(1,1)){
   building.numberOfRoomsAndRent[building.nameOfTenants[1].toLowerCase()][1]=1200;
}
console.log(building.numberOfRoomsAndRent[building.nameOfTenants[1].toLowerCase()][1]);

//Exercise 5//

let family = {
    father : "John",
    mother : "Jane",
    son : "John Jr",
    daughter : "Jane Jr",
    }

//will count in addition the number of keys in the object
let count = 0;
for (i in family){
    if (family.hasOwnProperty(i)){
    console.log(i);
    ++count;
    }
};
console.log(count);

for (i in family){
    if (family.hasOwnProperty(i)){
    console.log(family[i]);
    }
};

//Exercise 6//

let details = {
  my: 'name',
  is: 'Rudolf',
  the: 'raindeer'
}
let text =""; //otherwise it's undefined
for (i in details){
    if (details.hasOwnProperty(i)){ 
    text = text + i + " " + details[i] + " ";
    };
}
console.log(text.substring(0, text.length-1)); // don't want to have the last space

//Exercise 7//
let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
let sortedNames = names.sort();
console.log(sortedNames);
console.log (names.length) ;
let secret="";
for(i=0; i<names.length; i++) {
    secret=secret+sortedNames[i].substring(0,1);
}
console.log(secret);