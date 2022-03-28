//Exercise 1//

5 >= 1
  //Prediction : true because the value of the number 5 is superior or equal to 1
  //Actual : true

0 === 1
  //Prediction : false because the value of the number 0 is not equal to 1
  //Actual : false

4 <= 1
    //Prediction : false because the value of the number 4 is not inferior or equal to 1
    //Actual : false

1 != 1
    //Prediction : false because the value of 1 is not different from the value of 1
    //Actual : false

"A" > "B"
    //Prediction : false because 065 (ASCII code of B) is not superior to 066
    //Actual : false

"B" < "C"
    //Prediction : true because 066 is inferior to 067
    //Actual : true

"a" > "A"
   //Prediction : true because 097 is superior to 065
    //Actual : true

"b" < "A"
   //Prediction : false because 098 is not inferior to 065
    //Actual : false

true === false
   //Prediction : false because true is not equal to false in value (1!=0)
    //Actual : false

true != true
   //Prediction : false because true is not different from true in value
    //Actual : false

//Exercise 2//

let a = prompt("Please enter two numbers separated by commas");
let position = a.indexOf(",");
let length = a.length ;
let num1 = a.substring(0,position);
let num2 = a.substring(position+1,length) ;
let sum = Number(num1) + Number(num2);
console.log("The sum is " + sum) ;

//Exercise 3//
let b = prompt("Please enter a sentence containing the word \"JavaScript\"");
let position_b = b.indexOf("JavaScript");
console.log("I found \"JavaScript\"at "+ position_b);

//Exercise 4//
let c = prompt("Please enter a number");
if (c<=2) {
    n = 2;
    }
    else{
    n =c
    };
if (c%2==0) {
    f = "!";
    }
    else{
    f =""
    };
let textCenter ="o".repeat(n);
let text ="B"+ textCenter + "m" + f;
if (c%5==0) {
    textFinal = text.toUpperCase();
    }
    else{
        textFinal = text;
    };
console.log(textFinal);


