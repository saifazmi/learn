package main

import "fmt"

func main() {
	/* An array in Go is a numbered sequence of elements of
	a specific length
	*/

	// Creating an array that will hold exactly 5 ints
	// type of elements and length are part of the array's type
	// By default an array is zero-valued
	var a [5]int
	fmt.Println("emp:", a)

	// Set a value at an index
	a[4] = 100

	// Get the value
	fmt.Println("set:", a)
	fmt.Println("get:", a[4])

	// Length of the array
	fmt.Println("len:", len(a))

	// Declare and initialise in one line
	b := [5]int{1, 2, 3, 4, 5}
	fmt.Println("dcl:", b)

	// Arrays are one dimensional, but can be compose types
	// to build multi-dimensional data structures
	var twoD [2][3]int
	for i := 0; i < 2; i++ {
		for j := 0; j < 3; j++ {
			twoD[i][j] = i + j
		}
	}

	// Printed as [v1, v2, v3 ...]
	fmt.Println("2d: ", twoD)

	// In typical Go there are more "Slices" than arrays
}
