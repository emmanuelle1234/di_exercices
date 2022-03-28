//Exercise 1//

let sentence = ["my","favorite","color","is","blue"];
let sentenceJoined = sentence.join();
console.log(sentenceJoined);

//Exercise 2//

let str1 = "mix";
let str2 = "pod";
let str3 = str2.substring(0,2)+str1.substring(2)+ " " +str1.substring(0,2)+str2.substring(2);
console.log(str3);



//Exercise 3//
let num1 = prompt("Please enter the first number");
let num2 = prompt("Please enter the second number");
let sum = Number(num1) + Number(num2);
alert("The sum " + num1 + " + " +num2 + " is " + sum);

let num3 = prompt("Please enter the first number");
let num4 = prompt("Please enter the second number");
let substract = Number(num1) - Number(num2);
alert("The substraction " + num1 + " - " +num2 + " is " + substract);
