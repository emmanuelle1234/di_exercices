//Exercise 1//

let food = "avocado";
let meal = "dinner" ;
console.log("I eat " + food + " at every " + meal);

//Exercise 2//

let myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];
let myWatchedSeriesLength = myWatchedSeries.length ;
let myWatchedSeriesSentence = myWatchedSeries[0] + ", " + myWatchedSeries[1] + ", and " + myWatchedSeries[2];
console.log("I watched "+ myWatchedSeriesLength + " series : " + myWatchedSeriesSentence) ; 

myWatchedSeries[2]="friends";
myWatchedSeries.push("teheran");
myWatchedSeries.unshift("shtisel", "blacklist");
myWatchedSeries.splice(2, 1);
console.log( myWatchedSeries[2].charAt(2));
console.log(myWatchedSeries);

//Exercise 3//
let temperatureC = 27;
let temperatureF = (temperatureC / 5 * 9)+32;
console.log(temperatureC + "°C is " + temperatureF + "°F");

//Exercise 4//
let c;
let a = 34;
let b = 21;
console.log(a+b) //first expression
    // Prediction: It will output 55, because 34 and 21 are numbers
    // Actual: 55

a = 2;

console.log(a+b) //second expression
// Prediction: It will output 23, because 2 and 21 are numbers
// Actual: 23

console.log(c) //third expression
// Prediction: It will output undefined because c is not defined
// Actual: undefined

console.log(3 + 4 + '5'); //fourth expression
// Prediction: It will output 75 because 3 and 4 are numbers and '5' is a string
// Actual: undefined

//Exercise 5//
typeof(15)
// Prediction: number because 15 is a number
// Actual: number

typeof(5.5)
// Prediction: number because 1.5 is a number
// Actual: number

typeof(NaN)
// Prediction: string because NaN is a string
// Actual: number because NaN is a quantity which is not a number

typeof("hello")
// Prediction: string because hello is a string
// Actual: string

typeof(true)
// Prediction: boolean because true is a boolean
// Actual: boolean

typeof(1 != 2)
// Prediction: boolean because this is a boolean (false)
// Actual: boolean

"hamburger" + "s"
// Prediction: hamburgers because it concatenates 2 strings
// Actual: hamburgers

"hamburgers" - "s"
// Prediction: NaN because the result of a substraction is a quantity but this quantity is not a number hamburger and s being strings
// Actual: NaN

"1" + "3"
// Prediction: 13 because 1 and 3 are strings
// Actual 13

"1" - "3" 
// Prediction: NaN because the result of a substraction is a quantity but this quantity is not a number 1 and 3 being strings
// Actual: -2 

"johnny" + 5
// Prediction: johnny5 because the + operator acts as a concatenator with a string
// Actual: johnny5

"johnny" - 5
// Prediction: NaN because the substration of strings (5 becomes a string) results in a quantity which is not a number
// Actual: NaN

99 * "hello"
// Prediction: NaN because multiplication by a string gives a quantity which is not a number
// Actual: NaN

1 != 1
// Prediction: false because 1 equals 1
// Actual: false

1 == "1"
// Prediction: true because the value is the same
// Actual: true

1 === "1"
// Prediction: false because the type is not the same
// Actual: false


//Exercise 6//
5 + "34"
// Prediction: 534 because the + operator acts as a concatenator with a string
// Actual: 534

5 - "4"
// Prediction: 1 because the 4 becomes a number
// Actual: 1

10 % 5
// Prediction: 0 because nothing remains when dividing 10 by 5
// Actual: 0

5 % 10
// Prediction: 5 because 5 remains when dividing it by 10
// Actual: 5

"Java" + "Script"
// Prediction: JavaScript because both strings are concatenated
// Actual: JavaScript

" " + " "
// Prediction: '  ' because the two spaces are concatenated
// Actual: '  '

" " + 0
// Prediction: ' 0' because the space (string) is concatenated with the O
// Actual: ' 0'

true + true
// Prediction: 2 because the operator will make an addition and true is evaluated as the number 1
// Actual: 2

true + false
// Prediction: 1 (cf beyond) because 1+0=1
// Actual: 1

false + true
// Prediction: 1 because 1+0=1
// Actual: 1

false - true
// Prediction: -1 because 0-1=-1
// Actual: -1

!true
// Prediction: false because non true is false
// Actual: false

3 - 4
// Prediction: -1 because it is a substratction with two numbers
// Actual: -1

"Bob" - "bill"
// Prediction: NaN because the substraction with two strings results in a quantity which is not a number
// Actual: NaN
