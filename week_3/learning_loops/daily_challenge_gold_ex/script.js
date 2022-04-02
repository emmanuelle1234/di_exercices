//Daily Challenge//
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
let output2 = order(numbers.slice(l-2,l));
let output3 =[] ;

for (let i=l-3; i>0; i--) {
    output =  output1.concat(output2).concat(output3);
    console.log(output);
    if(output[i]<output[i+1]){
    output1 = output.slice(0,i);    
    output2 = order(output.slice(i,i+2));
    
    output3 = output.slice(i+2,l);
    } else {
    output1 = output.slice(0,i-1);    
    output2 = order(output.slice(i-1,i-3));
    output3 = output.slice(i+1,l);
    };
}

    
   /* for (let k=i;k>l;k--){
        output1 = output.slice(0,k);
        output2 = order(output.slice(k,k+2));
        output3 = output.slice(k+2,l);
        output = output1.concat(output2).concat(output3);
        console.log(output);*/
    

   /* console.log(output1);
    for(j=2;j>0;j--){
        let output2 = numbers;
        console.log(output2);
        if (output2[j]<output2[j-1]){
            let temp = output2[j-1]
            output2[j] = output2[j-1];
            output2[j-1]=temp;
            console.log(output2)
            }*/
   
    





