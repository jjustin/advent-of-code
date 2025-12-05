package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	b, err := os.ReadFile("./input")
	if err != nil {
		panic(err)
	}

	solution, err := solve(string(b))
	if err != nil {
		panic(err)
	}

	fmt.Println(solution)
}

func solve(input string) (int, error) {
	input = strings.TrimSpace(input)
	ranges := strings.Split(input, ",")

	sum := 0

	for _, r := range ranges {
		x := strings.Split(r, "-")

		start, err := strconv.Atoi(x[0])  
		if err != nil {
			return 0, err
		}
		end, err := strconv.Atoi(x[1])
		if err != nil {
			return 0, err 
		}

		for i := start; i <= end; i++ {
			if !isValid(i) {
				sum += i
			}
		}
	}

	return sum, nil
}

func isValid(i int) bool {
	x := strconv.Itoa(i)

	if x[:len(x)/2] == x[len(x)/2:] {
		return false
	}
	
	return true
}
