package main

import "fmt"
import "math"

// declare a constant value
const s string = "constant"

func main() {
    // prints the type of the variable which is "constant"
    fmt.Println(s)

    // const can be used anywhere we can use a var
    const n = 500000

    // constants perform arithmetic with arbitrary precision
    const d = 3e20 / n
    fmt.Println(d)

    // constants have no type until they are explicitly given one
    fmt.Println(int64(d))

    // a "number" can be given a type by using it in a context
    // that requires one, eg: variable assignment or function call
    fmt.Println(math.Sin(n))
}