package main

import (
	"fmt"
	"math"
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
		sum += findHighest(bank, 12)
	}

	return sum, nil
}

func findHighest(in []int, elements int) int {
	if elements == 0 {
		return 0
	}

	lookIn := in[:len(in)-elements+1]

	maxIx := 0
	for i := range lookIn {
		if lookIn[i] > lookIn[maxIx] {
			maxIx = i
		}
	}

	return int(math.Pow10(elements-1))*lookIn[maxIx] + findHighest(in[maxIx+1:], elements-1)
}
