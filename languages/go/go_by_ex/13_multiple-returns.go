package main

import "fmt"

/* Go has built-in support for multiple return values
Is used often in idiomatic Go, eg: returning both the result
and error value from a function
*/

// The (int, int) signature shows that the function returns 2 ints
func vals() (int, int) {
	return 3, 7
}

func main() {
	// Using two values returned
	a, b := vals()
	fmt.Println(a)
	fmt.Println(b)

	// Using only a subset of returned values, using blank identifier
	_, c := vals()
	fmt.Println(c)
}
