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

	input := strings.TrimSpace(string(b))
	lines := strings.Split(input, "\n")

	grid := [][]bool{}
	for i, line := range lines {
		grid = append(grid, []bool{})
		for _, ch := range line {
			grid[i] = append(grid[i], ch == '@')
		}
	}

	fmt.Println(solve1(grid))
	fmt.Println(solve2(grid))
}

func solve1(grid [][]bool) int {
	sum := 0
	for i := range grid {
		for j := range grid[i] {
			if grid[i][j] && countAdjacent(i, j, grid) < 4 {
				sum += 1
			}
		}
	}

	return sum
}

func countAdjacent(x, y int, grid [][]bool) int {
	w, h := len(grid), len(grid[0])

	xs := []int{x, x + 1, x - 1}
	ys := []int{y, y + 1, y - 1}

	count := 0
	for _, i := range xs {
		for _, j := range ys {
			if i == x && j == y {
				continue // don't count self
			}

			if j < 0 || j >= h || i < 0 || i >= w {
				continue // don't go out of bounds
			}

			if grid[i][j] {
				count += 1
			}
		}
	}

	return count
}

func solve2(grid [][]bool) int {
	sum := 0
	for {
		sumPre := sum
		for i := range grid {
			for j := range grid[i] {
				if grid[i][j] && countAdjacent(i, j, grid) < 4 {
					sum += 1
					grid[i][j] = false
				}
			}
		}

		if sumPre == sum {
			break
		}
	}

	return sum
}
