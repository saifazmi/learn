package main

import "fmt"

func main() {

    // var can declare one or more variables
    var a = "initial"
    fmt.Println(a)

    // multiple declarations
    var b, c int = 1, 2
    fmt.Println(b, c)

    // Go will infer the type when not explicit
    var d = true
    fmt.Println(d)

    // When not initialised a variable defaults to zero-valued
    // for int it's a zero
    var e int
    fmt.Println(e)

    // := is a syntax shorthand for declaring and initialising
    f := "short"
    fmt.Println(f)
}