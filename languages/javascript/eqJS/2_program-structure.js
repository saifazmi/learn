// EXPRESSIONS AND STATEMENTS

/*
== Expression ==
A fragment of code that produces a value is called an expression.
An expression between parentheses is also an expression, as is a
binary operator applied to two expressions or a unary operator applied to one.
eg: 22 or "psychoanalysis"
*/

/*
== Statement ==
If an expression corresponds to a sentence fragment, a JavaScript statement
corresponds to a full sentence. A program is a list of statements.
*/
1;
!false;

/*
== Bindings ==
To catch and hold values, JS provides a thing called a binding, or variable.
After a binding has been defined, its name can be used as an expression.

A binding / variable is not tied down to a value and can be reassigned a value
by using '=' operator.

Imagine bindings/variables as tentacles rather than boxes, which grasp on to
values and do not contain them.

When asking for the value of an empty variable, we get 'undefined'.
*/

// let
let caught = 5 * 5;

let ten = 10;
console.log(ten * ten); // 100

let mood = "light";
console.log(mood); // light
mood = "dark";
console.log(mood); // dark

let one = 1, two = 2; // defining multiple bindings, with a single 'let'
console.log(one + two); // 3

// var: pre-2015 JS, similar to let, with some confusing properties [Chapter 3]
var name = "Saif";
// const: defines a constant binding, pointing at the same value till it lives
const greeting = "Hello ";
console.log(greeting + name); // Hello Saif

/*
== Binding Names ==
DON'T
- start with a digit
- use keywords and reserved words as names
- no other punctuations, other than the ones defined below.

DO
- include $ and _

If a binding produces an 'unexpected syntax error', check if a reserved word is
being used.
*/

/*
== The Environment ==
The collection of bindings and their values that exist at a given time is
called the environment.

When a program starts up, this environment is not empty.
It always contains bindings that are part of the language standard,
and most of the time, it also has bindings that provide ways to interact with
the surrounding system.
For example, in a browser, there are functions to
interact with the currently loaded website and to read mouse and keyboard input.
*/

/*
== Functions ==
A function is a piece of program wrapped in a value. This value can be applied
in order to run the wrapped program.

Executing a function is called invoking, calling or applying it. They can be
called by putting a parentheses after an expression that produces a function
value.
eg: prompt("Enter passcode");
*/
let x = 30;
console.log("the value of x is", x);

