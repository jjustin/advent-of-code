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

	solution, err := solve(string(b))
	if err != nil {
		panic(err)
	}

	fmt.Println(solution)
}

func solve(input string) (int, error) {
	lines := strings.Split(input, "\n")

	pos := 50

	was0 := 0

	for _, line := range lines {
		if line == "" {
			continue
		}

		direction := 1
		if line[0] == 'L' {
			direction = -1
		}
		
		moveFor,err := strconv.Atoi(line[1:])
		if err != nil {
			return 0, err
		}

		pos = (pos + (direction * moveFor) + 100) % 100

		if pos == 0 {
			was0++
		}
	}
	
	return was0, nil
}
