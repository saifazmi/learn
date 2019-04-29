package main

import "fmt"

func main() {

	/* Go variables are explicitly declared and used by the compiler to
	e.g. check type-correctness of function calls.
	*/

	// var declares 1 or more variables
	var a = "initial"
	fmt.Println(a)

	// declaring multiple variables
	var b, c int = 1, 2
	fmt.Println(b, c)

	// Go will infer the type of initialised variables
	var d = true
	fmt.Println(d)

	// Variables without initialisation are 'zero-valued'
	// Zero value for int is 0
	var e int
	fmt.Println(e)

	// := syntax is shorthand for declaring and initialising a variable
	// eg: var f string = "short"
	f := "short"
	fmt.Println(f)
}
