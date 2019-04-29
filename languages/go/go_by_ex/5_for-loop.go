package main

import "fmt"

func main() {
	/* 'for' is Go's only looping construct.
	Here are three basic types of for loops.
	*/

	i := 1

	// Most basic, with single condition
	for i <= 3 {
		fmt.Println(i)
		i = i + 1
	}

	// The classic, initial/condition/after
	for j := 7; j <= 9; j++ {
		fmt.Println(j)
	}

	// Without a condition, the loop will repeat until you 'break'
	// or 'return' from the enclosing function
	for {
		fmt.Println("loop")
		break
	}

	// You can also 'continue' to the next iteration
	for n := 0; n <= 5; n++ {
		if n%2 == 0 {
			continue
		}
		fmt.Println(n)
	}
}
