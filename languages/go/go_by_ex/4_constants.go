package main

import (
	"fmt"
	"math"
)

// Go supports constants of characters, string, boolean and numeric values.

// const declares a constant
const s string = "constant"

func main() {
	fmt.Println(s)

	// const can appear anywhere a var statement can
	const n = 500000000

	// constants can perform arithmetic with arbitrary precision
	const d = 3e20 / n
	fmt.Println(d)

	// numeric constant has no type until it's given one,
	// such as by an explicit cast
	fmt.Println(int64(d))

	// number can be given a type by using it in a context that
	// requires one
	fmt.Println(math.Sin(n))
}
