//Daily Challenge//

//Using one loop
let list = [];
for (let i=0; i <6; i++) {
    list.push("* ") ;
    console.log(list.join(``));
};

//Using nested loops
line ="*";
for(let i=0; i<2; i++) {
    for(let j=0; j<3 ; j++) {
    console.log(line);
    line = line+" *" ;
    }
}
  
