package main

import "fmt"

/* Go supports anonymous functions, which can form closures */

// Returns another function, which is defined anonymously in the
// body of this function
// The returned function "closes over" the variable "i"
func intSeq() func() int {
	i := 0
	return func() int {
		i++
		return i
	}
}

func main() {

	// Calling intSeq() assigns the result value (a function) to nextInt
	// nextInt captures its own "i" value
	nextInt := intSeq()

	fmt.Println(nextInt()) // nextInt i = 1
	fmt.Println(nextInt()) // nextInt i = 2
	fmt.Println(nextInt()) // nextInt i = 3

	newInts := intSeq()    // captures its own i
	fmt.Println(newInts()) // newInts i = 1
}
