package main

import (
	"fmt"
	"math"
	"os"
	"slices"
	"strconv"
	"strings"
)

func main() {
	b, err := os.ReadFile("./input")
	if err != nil {
		panic(err)
	}

	input := strings.TrimSpace(string(b))

	points := []Point{}

	for _, line := range strings.Split(input, "\n") {
		parts := strings.Split(line, ",")
		x, err := strconv.Atoi(parts[0])
		if err != nil {
			panic(err)
		}

		y, err := strconv.Atoi(parts[1])
		if err != nil {
			panic(err)
		}

		points = append(points, Point{x: x, y: y})
	}

	fmt.Println(solve1(points))
	fmt.Println(solve2(points))
}

type Point struct {
	x, y int
}

func (p Point) area(p2 Point) int {
	x1 := float64(p.x)
	x2 := float64(p2.x)
	y1 := float64(p.y)
	y2 := float64(p2.y)
	return int(math.Max(x1, x2)+1-math.Min(x1, x2)) * int(math.Max(y1, y2)+1-math.Min(y1, y2))
}

func (p Point) String() string {
	return fmt.Sprintf("(%d, %d)", p.x, p.y)
}

type Pair struct {
	a, b Point
	area int
}

func NewPair(a, b Point) Pair {
	return Pair{
		a:    a,
		b:    b,
		area: a.area(b),
	}
}

func solve1(points []Point) int {
	pairs := []Pair{}

	for i, p1 := range points {
		for _, p2 := range points[:i] {
			pairs = append(pairs, NewPair(p1, p2))
		}
	}

	slices.SortFunc(pairs, func(a Pair, b Pair) int { return b.area - a.area })

	return pairs[0].area
}

func solve2(points []Point) int {
	pairs := []Pair{}

	for i, p1 := range points {
		for _, p2 := range points[:i] {
			pairs = append(pairs, NewPair(p1, p2))
		}
	}

	gridByX := map[int][]int{}
	gridByY := map[int][]int{}

	// Calculate the bounds of the red/green zone.
	for i := range points {
		p1 := points[i]
		j := i + 1
		if j == len(points) {
			j = 0
		}
		p2 := points[j]

		x1 := min(p1.x, p2.x)
		x2 := max(p1.x, p2.x)
		y1 := min(p1.y, p2.y)
		y2 := max(p1.y, p2.y)

		for x := x1; x <= x2; x++ {
			if gridByX[x] == nil {
				gridByX[x] = []int{}
			}

			for y := y1; y <= y2; y++ {
				if gridByY[y] == nil {
					gridByY[y] = []int{}
				}

				gridByX[x] = append(gridByX[x], y)
				gridByY[y] = append(gridByY[y], x)
			}
		}
	}

	// Sort slices at given x and y for quicker access later on
	for k := range gridByX {
		slices.Sort(gridByX[k])
	}
	for k := range gridByY {
		slices.Sort(gridByY[k])
	}

	// Sort the pairs to first iterate over the biggest pairs
	slices.SortFunc(pairs, func(a Pair, b Pair) int { return b.area - a.area })

pairs_loop:
	for _, pair := range pairs {
		x1 := min(pair.a.x, pair.b.x)
		x2 := max(pair.a.x, pair.b.x)
		y1 := min(pair.a.y, pair.b.y)
		y2 := max(pair.a.y, pair.b.y)

		// First check the corners to trim away any pairs that might have one corner outside of red/green zone.
		if isntInside(x1, y1, gridByX, gridByY) ||
			isntInside(x1, y2, gridByX, gridByY) ||
			isntInside(x2, y1, gridByX, gridByY) ||
			isntInside(x2, y2, gridByX, gridByY) {
			continue pairs_loop
		}

		// Check if edges of the rectangles are contained inside of the red/green zone
		for y := y1; y <= y2; y++ {
			if isntInside(x1, y, gridByX, gridByY) {
				continue pairs_loop
			}
			if isntInside(x2, y, gridByX, gridByY) {
				continue pairs_loop
			}
		}

		for x := x1; x <= x2; x++ {
			if isntInside(x, y1, gridByX, gridByY) {
				continue pairs_loop
			}
			if isntInside(x, y2, gridByX, gridByY) {
				continue pairs_loop
			}
		}

		return pair.area
	}

	return -1
}

func isntInside(x, y int, gridByX, gridByY map[int][]int) bool {
	// Check if point is bound by red/green zone in any direction.
	// That is achieved by checking if the point is bound by at least one red/green point in all directions (up, down, left, right).

	if isOutside(y, gridByX[x]) {
		return true
	}

	if isOutside(x, gridByY[y]) {
		return true
	}

	return false
}

func isOutside(i int, grid []int) bool {
	// if i is not bound by the grid then it's outside of the green/red zone.
	return i < grid[0] || i > grid[len(grid)-1]
}
