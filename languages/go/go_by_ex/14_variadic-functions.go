package main

import "fmt"

/* These functions can be called with any number of
trailing arguments. eg: fmt.Println
*/

// This function takes an arbitrary number of ints as arguments
func sum(nums ...int) {
	fmt.Print(nums, " ")
	total := 0
	for _, num := range nums {
		total += num
	}
	fmt.Println(total)
}

func main() {

	// Calling variadic functions
	sum(1, 2)
	sum(1, 2, 3)

	// Can apply multiple args from a slice to a variadic function
	// func(slice...)
	nums := []int{1, 2, 3, 4}
	sum(nums...)
}
