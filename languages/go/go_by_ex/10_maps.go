package main

import "fmt"

func main() {
	/* Maps are Go's built-in associative data type,
	also called hashes and dicts in other languages
	*/

	// Create a map using built-in 'make()'
	// make(map[key-type]val-type)
	m := make(map[string]int)

	// Set value, using typical 'name[key] = val' syntax
	m["k1"] = 7
	m["k2"] = 13

	// Printing with fmt.Println will show all key/value pairs
	fmt.Println("map:", m)

	// Get value 'name[key]'
	v1 := m["k1"]
	fmt.Println("v1: ", v1)

	// Length
	fmt.Println("len:", len(m))

	// Delete key/value pairs using the built-in delete
	delete(m, "k2")
	fmt.Println("map:", m)

	// The optional second return value indicates if they key was present
	// in the map.
	// Can be used to disambiguate between missing keys and keys
	// with zero value.

	// Can also ignore the value by using a blank identifier '_'
	_, prs := m["k2"]
	fmt.Println("prs:", prs)

	// Declare and initialise in the same line
	n := map[string]int{"foo": 1, "bar": 2}
	fmt.Println("map:", n)
}
