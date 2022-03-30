//Exercise 1//
let x = 18;
let y = 613;

if (x>y) {
    console.log(`x is the biggest number`) ;
} else if (x<y) {
    console.log(`y is the biggest number`) ;
} else // In cas I have not seen in the instructions that they ask for different numeric values !
console.log(`x equals y`) ;

//Exercise 2//
let newDog = "Chihuahua";
console.log (newDog.length);
console.log (newDog.toUpperCase(), newDog.toLowerCase());
let bool = newDog ==="Chihuahua" ;
console.log(bool) ;
if (bool) {
    console.log(`I love ${newDog}s, it's my favorite dog breed`) ;
} else
console.log(`I don't care, I prefer cats`) ;

//Exercise 3//
let num = prompt("Please enter a number");
if (!isNaN(num)) {
    if (Number(num) === 0) {
        console.log(`${num} is neither even nor odd`);
    }
    else if (num%2 === 0){
        console.log(`${num} is an even number`)
    } else {
        console.log(`${num} is an odd number`)  
    }
} else {
console.log(`This is not a number`) ;
}

//Exercise 4//
let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
let n = users.length ;
let text ;
switch (n) {
    case 0:
        text="no one is online";     
        break;
    case 1:
        text=users.join("") + " is online";
        break;
    case 2:
        text=users.slice(0,n-1).join(", ") + " and " + users.slice(n-1).join(", ") + " are online";
        break;
    default:
        text=`${users.slice(0,2).join(", ")} and ${n-2} more are online`;
        break; 
}
console.log(text) ;









