// Values

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

/*
FRACTIONS are not precise as JS only has 64 bits to store them, so they are
a close approximation and some values like pi can not be expressed by a finite
number of decimal digits.
*/

// Operators

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