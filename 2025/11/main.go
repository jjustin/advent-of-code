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

	connections := map[string][]string{}
	for _, line := range strings.Split(input, "\n") {
		parts := strings.Split(line, ": ")

		device := parts[0]
		connections[device] = []string{}
		connections[device] = append(connections[device], strings.Split(parts[1], " ")...)
	}

	fmt.Println(solve1(connections))
	fmt.Println(solve2(connections))
}

func solve1(connections map[string][]string) int {
	return countPaths1("you", "out", connections)
}

func countPaths1(from string, to string, connections map[string][]string) int {
	if from == to {
		return 1
	}

	sum := 0
	for _, dest := range connections[from] {
		sum += countPaths1(dest, to, connections)
	}
	return sum
}

func solve2(connections map[string][]string) int {
	return countPaths2("svr", "out", connections, map[string]*int{}, []string{"fft", "dac"})
}

func countPaths2(from string, to string, connections map[string][]string, memo map[string]*int, required []string) int {
	if i := slices.Index(required, from); i != -1 {
		newRequired := []string{}
		for el := range required {
			if el == i {
				continue
			}
			newRequired = append(newRequired, required[el])
		}
		required = newRequired
	}

	cacheKey := fmt.Sprintf("%s %s %v", from, to, required)

	if c := memo[cacheKey]; c != nil {
		return *c
	}

	if from == to {
		if len(required) != 0 {
			return 0
		}
		return 1
	}

	sum := 0
	for _, dest := range connections[from] {
		sum += countPaths2(dest, to, connections, memo, required)
	}

	memo[cacheKey] = &sum

	return sum
}
