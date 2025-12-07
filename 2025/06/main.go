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
	input := strings.TrimSpace(string(b))
	lines := strings.Split(input, "\n")

	operators := strings.Fields(lines[len(lines)-1])

	fmt.Println(solve(parse1(strings.Join(lines[:len(lines)-1], "\n")), operators))
	fmt.Println(solve(parse2(strings.Join(lines[:len(lines)-1], "\n")), operators))
}

func parse1(input string) [][]int {
	lines := strings.Split(input, "\n")

	numbers := [][]int{}

	for i, line := range lines[:len(lines)-1] {
		for j, num := range strings.Fields(line) {
			if i == 0 {
				numbers = append(numbers, []int{})
			}

			n, err := strconv.Atoi(num)
			if err != nil {
				panic(err)
			}

			numbers[j] = append(numbers[j], n)
		}
	}

	return numbers
}

func parse2(input string) [][]int {
	s := transposeString(input)
	s = strings.TrimSpace(s)

	numbers := [][]int{{}}

	i := 0
	for _, line := range strings.Split(s, "\n") {
		line = strings.TrimSpace(line)
		if line == "" {
			numbers = append(numbers, []int{})
			i++
			continue
		}
		num, err := strconv.Atoi(line)
		if err != nil {
			panic(err)
		}
		numbers[i] = append(numbers[i], num)
	}

	return numbers
}

func solve(numbers [][]int, operators []string) int {
	sum := 0
	for i, nums := range numbers {
		res := 0
		op := operators[i]
		if op == "*" {
			res = 1
		}

		for _, num := range nums {
			if op == "+" {
				res += num
			} else {
				res *= num
			}
		}

		sum += res
	}
	return sum
}

func transposeString(s string) string {
	out := ""
	lines := strings.Split(s, "\n")

	grid := [][]rune{}
	for j, line := range lines {
		for i, char := range line {
			if j == 0 {
				grid = append(grid, []rune{})
			}
			grid[i] = append(grid[i], char)
		}
	}

	for _, line := range grid {
		out += string(line)
		out += "\n"
	}

	return out
}
