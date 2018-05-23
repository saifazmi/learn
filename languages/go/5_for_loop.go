package main

import "fmt"

func main() {

	// Basic, single condition
	i := 1
	for i <= 3 {
		fmt.Println(i)
		i = i + 1
	}

	// Classic structure
	for j := 7; j <= 9; j++ {
		fmt.Println(j)
	}

	// A loop without a condition will loop repeatedly until it hits a
	// break or return statement
	for {
		fmt.Println("loop")
		break
	}

	// continue to the next iteration of the loop
	for n := 0; n <= 5; n++ {
		if n%2 == 0 {
			continue
		}
		fmt.Println(n)
	}
}
