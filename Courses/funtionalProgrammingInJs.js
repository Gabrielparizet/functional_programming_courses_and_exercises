// NOT FUNCTIONAL / IMPERATIVE STYLE (instructions after instructions) / We are not thinking in functional, in terms of how we give an input and return an output.
let myName = "Gabriel";
let greeting = "Hi, I am";
console.log(greeting + myName);
// => "Hi, I am Gabriel"

// FUNCTIONAL
function greet(name) {
    return "Hi, I am " + name;
}
greet("Gabriel");
// => "Hi, I am Gabriel"


// NOT PURE
// The greet function does not have an input, it is reading a variable from the global state.
// It is also not returning an output, it is printing something in the console.
let firstName = "Gabriel";
function greet(){
    console.log("Hi, I am" + firstName);
}

// PURE FUNCTION
function greet(name) {
    return "Hi, I am" + name;
}


// Higher-order functions
function makeAdjectifier(adjective){
    return function (string){
        return adjective + " " + string;
    };
}
let coolifier = makeAdjectifier("cool");
console.log(coolifier("conference"));
// => cool conference


// Mutation (bad!):
let rooms = ["H1", "H2", "H3"];
rooms[2] = "H4";
rooms;
// => ["H1", "H2", "H4"]

// No Mutation (good!):
let rooms = ["H1", "H2", "H3"];
let newRooms = rooms.map(function(rm){
    if (rm === "H3"){
        return "H4";
    } else {
        return rm;
    }
});
newRooms; // => ["H1", "H2", "H4"]
rooms; // => ["H1", "H2", "H3"]
