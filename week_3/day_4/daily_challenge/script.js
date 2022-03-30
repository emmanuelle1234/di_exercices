//Daily Challenge//
let sentence = "This dinner is not so bad ! It's surprising.";
let wordNot = sentence.indexOf("not") ;
//console.log(wordNot);
let wordBad = sentence.indexOf("bad");
//console.log(wordBad);
if (wordBad>wordNot && wordNot>=0){
    console.log(`${sentence.substring(0,wordNot-1)} good${sentence.substring(wordBad+3, sentence.length)}`);
    } else {
    console.log(sentence);
    }

