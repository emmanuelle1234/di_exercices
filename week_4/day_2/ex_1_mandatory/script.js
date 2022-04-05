//Exercise 1//
//PART I
function infoAboutMe() {
    console.log("My name is Emmanuelle Berrebi. I think I am 17 years old but they say I am not. Although I have no time to dedicate to it, my real hobby is literature.")
}
infoAboutMe();
//PART II
function infoAboutPerson(personName, personAge, personFavoriteColor) {
    console.log(`Your name is ${personName}, you are ${personAge} old, your favorite color is ${personFavoriteColor}`)
}
infoAboutPerson("David", 45, "blue");
infoAboutPerson("Josh", 12, "yellow");

//Exercise 2//

function calculateTip() {
    let bill = prompt("Dear John, what is the amount of the bill? (in USD)");
    let tip;
    if (bill<50){
        tip=0.2;
    } else if (bill<200){
        tip=0.15;
    } else {
        tip=0.1;
    }
    console.log(`The tip amount is ${(tip*bill).toFixed(2)}$ and the final bill is ${(bill*(1+tip)).toFixed(2)}$`);
}
//variables are local. Could have been defined before the function to be globaL.

calculateTip();

//Exercise 3//
function isDivisible(){
    let sum=0;
    let outcome= "";
    for (let i=0; i<501; i++){
        if (i%23==0) {
            outcome= outcome +" " + i;
            sum=sum+i;
        }
    }
    console.log(`Outcome : ${outcome}`);
    console.log(`Sum : ${sum}`);
}

isDivisible();

//Bonus
function isDivisible2(divisor){
    divisor = prompt("Please enter a divisor");
    let sum=0;
    let outcome= "";
    for (let i=0; i<501; i++){
        if (i%divisor==0) {
            outcome= outcome +" " + i;
            sum=sum+i;
        }
    }
    console.log(`Outcome : ${outcome}`);
    console.log(`Sum : ${sum}`);
}

isDivisible2();

//Exercise 4//

let stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

let prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 

let shoppingList = ["banana","orange","apple"];

function myBill(){
    let bill=0;
    for (i=0; i<shoppingList.length; i++){
        if (stock[shoppingList[i]]!==0);
        bill = bill + prices[shoppingList[i]];
    }
    console.log(`My bill is ${bill}$`);
}
myBill();

//Exercise 5//

function changeEnough(itemPrice, amountOfChange) {
    let afford = false;
    const change = [0.25, 0.1, 0.05, 0.01];
    let amount = 0;
    for (i=0; i<4;i++){
        amount= amount+change[i]*amountOfChange[i]
    }
    //console.log(amount);
    //console.log(itemPrice);
    if (amount>= itemPrice) {
        afford = true;
    } 
    return afford;
}
console.log(changeEnough(4.25, [25, 20, 5, 0]));
console.log(changeEnough(14.11, [2,100,0,0]));
console.log(changeEnough(0.75, [0,0,20,5]));

//Exercise 6//

function hotelCost() {
    let nightsNumber = prompt("Please enter the number of nights you would like to stay in the hotel.");
    if (isNaN(Number(nightsNumber)) || nightsNumber==""){
        nightsNumber = prompt("Please enter the number of nights you would like to stay in the hotel.");
    }
    const price = 140;
    return nightsNumber*price;
}

function planeRideCost(){
    let destination ="";
    destination = prompt("Please enter your destination.");

    if (destination=="" || Number(destination) ){
    destination = prompt("Please enter your destination.");
    }
    
    let destinationPrices = {
        "London": 183,
        "Paris": 220,
        "Other": 300,
    }

    let planePrice;

    switch (destination){

        case Object.keys(destinationPrices)[0]:
        planePrice = Object.values(destinationPrices)[0] ;
        break;
        
        case Object.keys(destinationPrices)[1]:
        planePrice = Object.values(destinationPrices)[1] ;
        break;
        
        case Object.keys(destinationPrices)[2]:
        planePrice = Object.values(destinationPrices)[2] ;
        break;

        default:
        planePrice = "You didn't input an appropriate destination!" ;
   
    }
    return planePrice ;
}

function rentalCarCost() {
    let carDays = prompt("How many days you want to rent a car?");
    if (isNaN(Number(carDays)) || carDays==""){
        carDays = prompt("How many days you want to rent a car? Please enter a number.");
    }
    const carPrice = 40;
    let totalCar;
    if (carDays>=10){
        totalCar = carDays * carPrice * (1- 0.05);
    } else if (carDays>0){
        totalCar = carDays * carPrice;
    } else {
        totalCar = "Don't you want to rent a car?"
    }
    return totalCar;
}

function totalVacationCost() {
    let a = planeRideCost();
    let b =hotelCost();
    let c = rentalCarCost();
    let totalCost = a + b + c;
    console.log(`The total cost of your vacations is $${totalCost}: the plane tickets cost $${a}, the hotel costs $${b} and the car costs $${c}.`);
   
}

totalVacationCost();

//Exercise 6 bonus version//

function hotelCost(nightsNumber) {
    const price = 140;
    return nightsNumber*price;
}

function planeRideCost(destination){
    let destinationPrices = {
        "London": 183,
        "Paris": 220,
        "Other": 300,
    }

    let planePrice;

    switch (destination){

        case Object.keys(destinationPrices)[0]:
        planePrice = Object.values(destinationPrices)[0] ;
        break;
        
        case Object.keys(destinationPrices)[1]:
        planePrice = Object.values(destinationPrices)[1] ;
        break;
        
        case Object.keys(destinationPrices)[2]:
        planePrice = Object.values(destinationPrices)[2] ;
        break;

        default:
        planePrice = "You didn't input an appropriate destination!" ;
   
    }
    return planePrice ;
}

function rentalCarCost(carDays) {
    
    const carPrice = 40;
    let totalCar;
    if (carDays>=10){
        totalCar = carDays * carPrice * (1- 0.05);
    } else if (carDays>0){
        totalCar = carDays * carPrice;
    } else {
        totalCar = "Don't you want to rent a car?"
    }
    return totalCar;
}

function totalVacationCost() {
    
    let destination ="";
    destination = prompt("Please enter your destination.");

    if (destination=="" || Number(destination) ){
    destination = prompt("Please enter your destination.");
    }

    let nightsNumber = prompt("Please enter the number of nights you would like to stay in the hotel.");
    if (isNaN(Number(nightsNumber)) || nightsNumber==""){
        nightsNumber = prompt("Please enter the number of nights you would like to stay in the hotel.");
    }

    let carDays = prompt("How many days you want to rent a car?");
    if (isNaN(Number(carDays)) || carDays==""){
        carDays = prompt("How many days you want to rent a car? Please enter a number.");
    }


    let a = planeRideCost(destination);
    let b =hotelCost(nightsNumber);
    let c = rentalCarCost(carDays);
    let totalCost = a + b + c;
    console.log(`The total cost of your vacations is $${totalCost}: the plane tickets cost $${a}, the hotel costs $${b} and the car costs $${c}.`);
   
}

totalVacationCost();
