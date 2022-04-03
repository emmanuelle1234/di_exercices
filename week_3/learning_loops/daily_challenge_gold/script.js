//Daily Challenge//
//Version 1
const numbers = [5,0,9,1,7,4,2,6,3,8];
console.log(numbers.toString());
console.log(numbers.join("+"));
console.log(numbers.join(" "));
console.log(numbers.join(""));
let temp;
function order([n,m]) {
    if (n<m){
        temp = n;
        n = m;
        m = temp;
    }
    a=[n,m]
    return a;
}
let l = numbers.length;
console.log(l);
let output1 = numbers.slice(0,l-2); 
let output2 = order(numbers.slice(l-2,l)); //sub-part of the array to be re-ordered
let output3 =[] ;
let output = numbers;
//let test =output[0]>output[1] && output[1]>output[2] && output[2]>output[3] && output[3]>output[4] && output[4]>output[5] && output[5]>output[6] && output[6]>output[7] && output[7]>output[8] && output[8]>output[9]
for (let p=l-1; p>-1; p--) {
    for (let k= p; k>-1; k--) {
        for (let j=k; j>-1; j--) {
            for (let i=j; i>-1; i--) { // i : position of the doublet to re-order
                output =  output1.concat(output2).concat(output3);
                output2 = order(output.slice(i, i+2));
                output1 = output.slice(0,i);
                output3 = output.slice(i+2,l);
                console.log(output);
            }
        }
    }
}
output =  output1.concat(output2).concat(output3);
console.log(output);

//don't manage with only two for nested loops

//Version 2
output = numbers;
let suboutput1 = order(numbers.slice(0,2)); 
let suboutput2 = order(numbers.slice(2,4));
let suboutput3 = order(numbers.slice(4,6)); 
let suboutput4 = order(numbers.slice(6,8)); 
let suboutput5 = order(numbers.slice(8,10)); 
let firstoutput = suboutput1.concat(suboutput2).concat(suboutput3).concat(suboutput4).concat(suboutput5);  

for (let i=0;i<l-1;i++) {    
    output = firstoutput.slice(0,10);  
    console.log(output);
 if (i%2==0){
    let suboutput1 = order(output.slice(0,2)); 
    let suboutput2 = order(output.slice(2,4));
    let suboutput3 = order(output.slice(4,6)); 
    let suboutput4 = order(output.slice(6,8)); 
    let suboutput5 = order(output.slice(8,10)); 
    firstoutput = suboutput1.concat(suboutput2).concat(suboutput3).concat(suboutput4).concat(suboutput5);  
    output = firstoutput.slice(0,10);
    console.log(output);
    } else {
    let suboutput1 = output.slice(0,1); 
    let suboutput2 = order(output.slice(1,3));
    let suboutput3 = order(output.slice(3,5)); 
    let suboutput4 = order(output.slice(5,7)); 
    let suboutput5 = order(output.slice(7,9)); 
    let suboutput6 = output.slice(9,10); 
    firstoutput = suboutput1.concat(suboutput2).concat(suboutput3).concat(suboutput4).concat(suboutput5).concat(suboutput6);
    output = firstoutput.slice(0,10);
    console.log(output);
    }
}   
//one if in one for loop
 
//Version 3 soon