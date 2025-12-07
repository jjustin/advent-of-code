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
	sections := strings.Split(input, "\n\n")

	ranges := []*Range{}
	for _, l := range strings.Split(sections[0], "\n") {
		fromTo := strings.Split(l, "-")
		from, err := strconv.Atoi(fromTo[0])
		if err != nil {
			panic(err)
		}
		to, err := strconv.Atoi(fromTo[1])
		if err != nil {
			panic(err)
		}

		ranges = append(ranges, &Range{from: from, to: to})
	}

	lookFor := []int{}
	for _, l := range strings.Split(sections[1], "\n") {
		el, err := strconv.Atoi(l)
		if err != nil {
			panic(err)
		}
		lookFor = append(lookFor, el)
	}

	fmt.Println(solve1(ranges, lookFor))
	fmt.Println(solve2(ranges))
}

type Range struct {
	from int
	to   int
}

func (r Range) len() int {
	if r.to < r.from {
		return 0
	}
	return r.to - r.from + 1
}

func (r *Range) contains(i int) bool {
	return r.from <= i && i <= r.to
}

func solve1(freshRanges []*Range, lookFor []int) int {
	sum := 0

	for _, el := range lookFor {
		for _, freshRange := range freshRanges {
			if freshRange.contains(el) {
				sum += 1
				break
			}
		}
	}

	return sum
}

func solve2(freshRanges []*Range) int {
	for i, incoming := range freshRanges {
		for _, current := range freshRanges[:i] {
			// current shadows incoming
			if incoming.from >= current.from && incoming.to <= current.to {
				// -2 to adjust for difference in calculation of range.len()
				incoming.to = -2
				incoming.from = -1
				continue
			}

			// incoming shadows current
			if current.from >= incoming.from && current.to <= incoming.to {
				// -2 to adjust for difference in calculation of range.len()
				current.to = -2
				current.from = -1
				continue
			}

			// Overlaps the current's beginning
			if incoming.from >= current.from && incoming.from <= current.to && incoming.to >= current.to {
				incoming.from = current.to + 1
			}

			// Overlaps the current's end
			if incoming.from <= current.from && incoming.to >= current.from && incoming.to <= current.to {
				incoming.to = current.from - 1
			}
		}
	}

	sum := 0
	for _, freshRange := range freshRanges {
		sum += freshRange.len()
	}

	return sum
}
