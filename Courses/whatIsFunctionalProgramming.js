// Functions and data are totally separate in functional programming

let score = 456;

function addBonus(){
    score = score + 45;
    return score;
}


// Functional programming equivalent
function addBonus(score){
    return score + 45;
}


// State change ++++++++++++++++++++++++++

// Here we change the state of a variable often, which makes it more tricky to keep track of the state of that variable. 
let gabriel = "hey";
gabriel = "hey there";
gabriel = "hey there, everyone";

// Functional programming equivalent
// Rather than updating the value of toto's variable, we declare new variables with some modifications so it becomes more clear what we're doing.
let toto = "hey";
let totoWednesday = "hey there";
let totoSaturday = "hey there, everyone";


// functions are treated as first class +++++++++++++++++++++++++++++

const h = 45;
const name = "gabriel";

const addScore = function (){}

function sayHello(sayGoodbye(){...}){
    return sayHi(){...}
}