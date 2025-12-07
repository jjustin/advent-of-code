package main

import (
	"fmt"
	"os"
	"slices"
	"strings"
)

func main() {
	b, err := os.ReadFile("./input")
	if err != nil {
		panic(err)
	}

	input := strings.TrimSpace(string(b))

	grid := [][]string{}

	for i, line := range strings.Split(input, "\n") {
		grid = append(grid, []string{})
		for _, c := range line {
			grid[i] = append(grid[i], string(c))
		}
	}

	grid2 := make([][]string, len(grid))
	for i, row := range grid {
		grid2[i] = slices.Clone(row)
	}

	fmt.Println(solve1(grid))
	fmt.Println(solve2(grid2))
}

func solve1(grid [][]string) int {
	return simulate1(0, slices.Index(grid[0], "S"), grid)
}

func simulate1(y, x int, grid [][]string) int {
	for y < len(grid) {
		if grid[y][x] == "^" {
			out := 1
			out += simulate1(y, x-1, grid)
			out += simulate1(y, x+1, grid)
			return out
		}
		if grid[y][x] == "|" {
			return 0
		}

		grid[y][x] = "|"
		y++
	}
	return 0
}

func solve2(grid [][]string) int {
	history := map[int]map[int]int{}
	for i := range grid {
		history[i] = map[int]int{}
	}

	return simulate2(0, slices.Index(grid[0], "S"), grid, history)
}

func simulate2(y, x int, grid [][]string, history map[int]map[int]int) int {
	for y < len(grid) {
		if history[y][x] != 0 {
			return history[y][x]
		}

		if grid[y][x] == "^" {
			out := 0
			out += simulate2(y, x-1, grid, history)
			out += simulate2(y, x+1, grid, history)
			history[y][x] = out
			return out
		}

		y++
	}
	return 1
}
