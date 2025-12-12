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

	grids := [][][][]bool{}

	parts := strings.Split(input, "\n\n")
	for i, grid := range parts[:len(parts)-1] {
		grids = append(grids, [][][]bool{[][]bool{}})
		for y, line := range strings.Split(grid[3:], "\n") {
			grids[i][0] = append(grids[i][0], []bool{})
			for _, c := range line {
				grids[i][0][y] = append(grids[i][0][y], c == '#')
			}
		}
	}

	rotate90 := func(grid [][]bool) [][]bool {
		out := [][]bool{}
		for _, row := range grid {
			out = append(out, make([]bool, len(row)))
		}
		for x := range grid[0] {
			for y := range grid {
				out[len(grid)-x-1][y] = grid[y][x]
			}
		}

		return out
	}

	for i := range grids {
		for j := range 3 {
			grids[i] = append(grids[i], rotate90(grids[i][j]))
		}
	}

	requirements := []Req{}

	for _, line := range strings.Split(parts[len(parts)-1], "\n") {
		req := Req{}
		lineParts := strings.Split(line, " ")
		size := strings.TrimSuffix(lineParts[0], ":")
		sizeParts := strings.Split(size, "x")

		req.h, err = strconv.Atoi(sizeParts[0])
		if err != nil {
			panic(err)
		}

		req.w, err = strconv.Atoi(sizeParts[1])
		if err != nil {
			panic(err)
		}

		for _, count := range lineParts[1:] {
			c, err := strconv.Atoi(count)
			if err != nil {
				panic(err)
			}
			req.counts = append(req.counts, c)
		}

		requirements = append(requirements, req)
	}

	fmt.Println(solve1(grids, requirements))
	fmt.Println(solve2())
}

type Req struct {
	h, w   int
	counts []int
}

func solve1(grids [][][][]bool, requirements []Req) int {
	sum := 0
	for _, req := range requirements {
		bigGrid := [][]bool{}
		for range req.w {
			bigGrid = append(bigGrid, make([]bool, req.h))
		}

		if canPositionRec(bigGrid, grids, req.counts, map[string]bool{}) {
			sum += 1
		}
	}
	return sum
}

func cacheKey(bigGrid [][]bool, remaining []int) string {
	return fmt.Sprintf("%v\n%v", bigGrid, remaining)
}

func canPositionRec(bigGrid [][]bool, grids [][][][]bool, remaining []int, memo map[string]bool) bool {
	// fmt.Println(remaining)
	// printGrid(bigGrid)
	all0 := true
	for _, r := range remaining {
		if r != 0 {
			all0 = false
			break
		}
	}
	if all0 {
		return true
	}

	cacheKey := cacheKey(bigGrid, remaining)
	if memo[cacheKey] {
		return false
	}

	for i := range remaining {

		if remaining[i] == 0 {
			continue
		}

		smallGrids := grids[i]

		// smallGrid is a different rotation of current block
		for _, smallGrid := range smallGrids {
			for y, row := range bigGrid {
				for x := range row {
					if overlaps(bigGrid, smallGrid, x, y) {
						continue
					}

					cloned := cloneGrid(bigGrid)
					for sy, row := range smallGrid {
						for sx, v := range row {
							if v {
								cloned[y+sy][x+sx] = true
							}
						}
					}

					if canPositionRec(
						cloned,
						grids,
						reduceRemaining(remaining, i),
						memo,
					) {
						return true
					}
				}
			}
		}
	}

	memo[cacheKey] = true

	return false
}

func overlaps(bigGrid, smallGrid [][]bool, x, y int) bool {
	if y > len(bigGrid)-len(smallGrid) {
		return true
	}

	if x > len(bigGrid[y])-len(smallGrid[0]) {
		return true
	}

	for i, row := range smallGrid {
		for j, v := range row {
			if v && bigGrid[y+i][x+j] {
				return true
			}
		}
	}
	return false
}

func reduceRemaining(remaining []int, i int) []int {
	out := make([]int, len(remaining))
	copy(out, remaining)
	out[i] -= 1

	return out
}

func cloneGrid(grid [][]bool) [][]bool {
	out := [][]bool{}
	for i := range grid {
		out = append(out, []bool{})
		for j := range grid[i] {
			out[i] = append(out[i], grid[i][j])
		}
	}
	return out
}

func printGrid(grid [][]bool) {
	for _, row := range grid {
		for _, v := range row {
			if v {
				print("#")
			} else {
				print(".")
			}
		}
		println()
	}
	println()
}

func solve2() int {
	return 0
}
