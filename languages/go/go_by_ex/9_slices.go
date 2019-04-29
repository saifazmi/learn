package main

import "fmt"

func main() {
	/* Slices are a key data type in Go, provides a more powerful
	interface to sequences than arrays.
	*/

	// Unlike arrays, slices are typed by the elements they contain
	// Create an empty slice with non-zero length use 'make()'
	s := make([]string, 3)
	fmt.Println("emp:", s)

	// Set and get just like arrays
	s[0] = "a"
	s[1] = "b"
	s[2] = "c"
	fmt.Println("set:", s)
	fmt.Println("get:", s[2])

	// len() returns length of the slice
	fmt.Println("len:", len(s))

	// Other rich operations

	// append() returns a slice containing one or more new values
	// need to accept the new slice value
	s = append(s, "d")
	s = append(s, "e", "f")
	fmt.Println("apd:", s)

	// copy() from one slice to another
	c := make([]string, len(s))
	copy(c, s)
	fmt.Println("cpy:", c)

	// Slices support "slice" operator with syntax slice[low:high]
	// s[2], s[3], s[4]
	l := s[2:5]
	fmt.Println("sl1:", l)

	// slice up to but excluding s[5]
	l = s[:5]
	fmt.Println("sl2:", l)

	// slice up from an including s[2]
	l = s[2:]
	fmt.Println("sl3:", l)

	// Declare and initialise a variable for slice in single line
	// notice the empty [] brackets, no initial size needed, unlike arrays
	t := []string{"g", "h", "i"}
	fmt.Println("dcl:", t)

	// Multi-dimensional data structures
	// length of inner slices can vary unlike with multiD arrays
	twoD := make([][]int, 3)
	for i := 0; i < 3; i++ {
		innerLen := i + 1
		twoD[i] = make([]int, innerLen)
		for j := 0; j < innerLen; j++ {
			twoD[i][j] = i + j
		}
	}
	fmt.Println("2d: ", twoD)
}
