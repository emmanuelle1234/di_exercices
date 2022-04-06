//Checks the validity of the input by the user
let checkValidity = (num) => {
    if (isNaN(num)) {
        return 'Sorry it\'s not a number, GoodBye'; //typeof num = "string"
    } else if (num <0 || num >10) {
        return 'Sorry it\'s not a good number, GoodBye';//typeof num = "string"
    }
        return num; //typeof num = "number"
}

//Asks the user for a number, check it is a valid number and enter the guess loop
let checkNumber = (computerNumber, numberOfGuess) => {
    console.log(computerNumber);
    let getNumber = Number(prompt("Please enter a number between 0 and 10"));
    let checkValidityResult = checkValidity(getNumber);
    if (typeof checkValidityResult ==="string") {
        alert(checkValidityResult);
        //return false;
    } else {
        //continue
        let comparison = compareNumbers(getNumber, computerNumber);
        if (numberOfGuess !=0) {
        guessLoop(comparison, numberOfGuess, computerNumber);}
        //return true;
    }
}

// Manages the number of guesses
let guessLoop = (checkValidityResult, numberOfGuess, computerNumber) =>{
        if (compareNumbers === "WINNER"){
            alert("You won !") ;
            return ;
         } else {
            console.log(compareNumbers,numberOfGuess);
            if (numberOfGuess<3) {
                numberOfGuess++;
                checkNumber(computerNumber, numberOfGuess);
        } else {
            alert ("Out of chances!");
        }
          
    }
}

// Compares the number provided by the user and the random value
let compareNumbers = (getNumber, computerNumber) =>{
    if (getNumber === computerNumber) {
        return "WINNER"
    } else if (getNumber > computerNumber){
        return "Your number is bigger then the computer’s, guess again" ;
    } else
        return "Your number is smaller then the computer’s, guess again";
}


//The function which calls all other functions
let playTheGame = () => {
    let wouldLikeToPlay = confirm("Would you like to play the game?");

    let numberOfGuess = 1; // cf. guessLoop 

    if (wouldLikeToPlay) {
        let computerNumber = Math.round(Math.random()*(10-0)+ 0);
        checkNumber(computerNumber, numberOfGuess) ;
        } else {
        alert("No problem, Goodbye") ;
    }
}