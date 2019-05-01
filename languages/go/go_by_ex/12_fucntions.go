package main

import "fmt"

// Go requires explicit returns
func plus(a int, b int) int {
	return a + b
}

// Can declare the type of like-typed parameters after
// the final parameter
func plusPlus(a, b, c int) int {
	return a + b + c
}

func main() {
	res := plus(1, 2)
	fmt.Println("1+2 = ", res)

	res = plusPlus(1, 2, 3)
	fmt.Println("1+2+3 =", res)
}
