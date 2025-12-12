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

	gridsSizes := []int{}

	parts := strings.Split(input, "\n\n")
	for i, grid := range parts[:len(parts)-1] {
		gridsSizes = append(gridsSizes, 0)
		for _, line := range strings.Split(grid[3:], "\n") {
			for _, c := range line {
				if c == '#' {
					gridsSizes[i]++
				}
			}
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

	fmt.Println(solve1(gridsSizes, requirements))
	fmt.Println(solve2())
}

type Req struct {
	h, w   int
	counts []int
}

func solve1(gridSizes []int, requirements []Req) int {
	sum := 0

	// The inputs of the proper solution are either small enough to fit or obviously too big.
	// Filter by wether or not they are too big or not.
	// The example input is a scam.
	for _, req := range requirements {
		innerSum := 0
		for i, s := range gridSizes {
			innerSum += s * req.counts[i]
		}
		if innerSum < req.h*req.w {
			sum += 1
		}
	}
	return sum
}

func solve2() string {
	return "It's not Christmas yet"
}
