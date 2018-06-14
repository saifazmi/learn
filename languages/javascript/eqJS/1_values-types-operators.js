// VALUES

/*
== Numbers ==
- are 64 bits, this means that it can store 2^64 different numbers
- approx. 18 quintillion numbers i.e. 18 with 18 zeros after it
- in reality JS stores 9 quadrillion (15 zeros) WHOLE numbers because:
-- 1 bit used for the sign of the number +ve or -ve
-- some more bits used for storing the position of the decimal point 
*/

console.log("Integer:", 13); // integer
console.log("Fraction:", 9.81); // fraction
// -> 2.998 x 10^8 = 299,800,000
console.log("Exponent (2.998e8):", 2.998e8); // scientific exponent

// Special Numbers: considered to be numbers but don't behave like one
console.log(Infinity);
console.log(-Infinity);
console.log(Infinity - 1); // still Infinity
/* Infinity based computation isn't mathematically sound and can quickly lead
to NaN */

console.log(NaN); // not a number
console.log(0 / 0);
console.log(Infinity - Infinity);
/* this is a result of numeric operations that don't yield a meaningful result
eg: 0/0 or Infinity - Infinity */

/* FRACTIONS are not precise as JS only has 64 bits to store them, so they are
a close approximation and some values like pi can not be expressed by a finite
number of decimal digits */


/*
== Strings ==
- are also modelled as a series of bits
- based on Unicode standard, assigns a number to virtually every character
- includes characters from: Greek, Arabic, Japanese, Armenian, etc.
- this enables a string to be described by a sequence of numbers

Complication:
- JS uses 16 bits to represent a single string element
- this means 2^16 different characters
- BUT Unicode defines about twice as many characters
- so some characters like emojis take two "character positions" in JS strings
*/

console.log(`Down on the sea`); // backtick
console.log("Lie on the ocean"); // double quote
console.log('Float on the ocean'); // single quote

console.log('Hello there, I\'m Saif'); // character escaping
console.log("This is a backslash \"\\\"");
console.log("Line one\nLine two"); // new line
console.log("Here is some\tIndentation") // tab

console.log("con" + "cat" + "e" + "nate"); // concatenation

console.log(`half of 100 is ${100 / 2}`);
/* backtick strings are also called template literals and have few tricks, they
can span lines and can also embed other values. Anything written inside ${} in
a template literal will get its result computed, converted to a string, and
included at that position */

/*
== Boolean ==
Strings are roughly alphabetically ordered but not exactly like a Dictionary,
uppercase letters are always "less" than lowercase letters i.e. "Z" < "a" and
non-alpha characters (!, -, etc) are also included in ordering. The comparison
is carried out from left to right, comparing the Unicode values one by one.
*/
console.log(3 > 2); // true
console.log(3 < 2); // false

console.log("Aardvark" < "Zoroaster"); // true

/*
== NaN ==
There is only one value in Javascript that is not equal to itself: NaN
NaN is supposed to denote the result of nonsensical computation.
*/
console.log(NaN == NaN);

/*
== Empty Values ==
There are two special values, 'null' and 'undefined' that denote the absence of
a meaningful value, i.e. they carry no information.

Operations that don't produce a meaningful value yield 'undefined', simply
because they have to yield some value.

Difference in the meaning b/w null and undefined is an accident of JS design,
and doesn't matter most of the time, so can be treated as interchangeable.
*/
console.log(null);
console.log(undefined);


// OPERATORS

/*
== Arithmetic ==
application of operators is determined by precedence (/ & *) > (+ & -) and
+ == - & * == / == %. In case of equal precedence they are applied left to right.

parentheses can be used to override precedence.
*/
console.log(100 + 4 * 11);
console.log((100 + 4) * 11);
console.log(1 - 2 / 3);
console.log(1 - 2 % 3);

/*
== Unary Operators ==
operate on only value, eg: typeof which returns a string value naming the type
type of the value. 
The minus operator can be used as both a binary and unary operator
*/
console.log(typeof 4.5);
console.log(typeof "x");
console.log(- (10 - 2));

/*
Comparison operators: <,>,<=,>=,==,!=
*/
console.log("Itchy" != "Scratchy");
console.log("Apple" == "Orange");

/*
Logical Operators: && (AND) || (OR) ! (NOT, unary operator, flips the value)

When combining these operators with comparison operators, || has the lowest
precedence, then comes &&, then comparison, and then the rest.
*/
console.log(true && false); // false
console.log(true && true); // true

console.log(false || true); // true
console.log(false || false); // false

console.log(!false); // true
console.log(!true); // false

console.log(1 + 1 == 2 && 10 * 10 > 50); // true

/*
Ternary or conditional operator: (condition) ? :
*/
console.log(true ? 1 : 2); // 1
console.log(false ? 1 : 2); // 2