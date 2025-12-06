package main

import (
	"fmt"
	"os"
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
	banksString := strings.Split(input, "\n")

	banks := make([][]int, len(banksString))
	for i, bank := range banksString {
		banks[i] = make([]int, len(bank))
		for j, battery := range bank {
			banks[i][j] = int(battery - '0')
		}
	}

	sum := 0

	for _, bank := range banks {
		sum += findHighest(bank)
	}

	return sum, nil
}

func findHighest(in []int) int {
	best := 0
	for ix, i := range in[:len(in)-1] {
		for _, j := range in[ix+1:] {
			c := i*10 + j
			if best < c {
				best = c
			}
		}
	}

	return best
}
