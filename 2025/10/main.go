package main

import (
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"

	"github.com/draffensperger/golp"
)

func main() {
	b, err := os.ReadFile("./input")
	if err != nil {
		panic(err)
	}

	input := strings.TrimSpace(string(b))

	machines := []Machine{}
	for i, line := range strings.Split(input, "\n") {
		parts := strings.Split(line, " ")

		m := Machine{id: i}

		for _, x := range parts[0][1 : len(parts[0])-1] {
			m.wantedStatusLights = append(m.wantedStatusLights, x == '#')
			m.statusLights = append(m.statusLights, false)
		}

		for _, wiring := range parts[1 : len(parts)-1] {
			w := []int{}
			for _, x := range strings.Split(wiring[1:len(wiring)-1], ",") {
				i, err := strconv.Atoi(x)
				if err != nil {
					panic(err)
				}
				w = append(w, i)
			}
			m.buttons = append(m.buttons, w)
		}

		r := parts[len(parts)-1]
		for _, req := range strings.Split(r[1:len(r)-1], ",") {
			i, err := strconv.Atoi(req)
			if err != nil {
				panic(err)
			}
			m.wantedJoltage = append(m.wantedJoltage, i)
		}

		machines = append(machines, m)
	}

	fmt.Println(solve1(machines))
	fmt.Println(solve2(machines))
}

type Machine struct {
	id int

	buttons [][]int

	statusLights       []bool
	wantedStatusLights []bool

	wantedJoltage []int

	steps int
}

func (m Machine) clone() Machine {
	out := m
	out.statusLights = make([]bool, len(m.statusLights))
	copy(out.statusLights, m.statusLights)

	return out
}

func statusHash(s []bool) string {
	out := ""
	for _, x := range s {
		if x {
			out += "#"
		} else {
			out += "."
		}
	}
	return out
}

func solve1(machines []Machine) int {
	sum := 0
	for _, m := range machines {
		sum += bfs1(m)
	}
	return sum
}

func bfs1(m Machine) int {
	history := map[string]bool{}
	toProcess := []Machine{m}

	for {
		machine := toProcess[0]

		toProcess = toProcess[1:]

		if history[statusHash(machine.statusLights)] {
			continue
		}

		for _, button := range m.buttons {
			innerMachine := machine.clone()
			history[statusHash(innerMachine.statusLights)] = true

			for _, change := range button {
				innerMachine.statusLights[change] = !innerMachine.statusLights[change]
			}
			innerMachine.steps++

			if slices.Equal(innerMachine.statusLights, innerMachine.wantedStatusLights) {
				return innerMachine.steps
			}

			toProcess = append(toProcess, innerMachine)
		}
	}
}

func solve2(machines []Machine) int {
	sum := 0
	for _, m := range machines {
		sum += lpMagic(m)
	}
	return sum
}

func lpMagic(m Machine) int {
	lp := golp.NewLP(0, len(m.buttons))

	for i := range m.wantedJoltage {
		row := []float64{}
		for _, b := range m.buttons {
			if slices.Contains(b, i) {
				row = append(row, 1)
			} else {
				row = append(row, 0)
			}
		}

		err := lp.AddConstraint(row, golp.EQ, float64(m.wantedJoltage[i]))
		if err != nil {
			panic(err)
		}
	}

	objFn := []float64{}
	for i := range m.buttons {
		lp.SetInt(i, true)
		objFn = append(objFn, 1.0)
	}
	lp.SetObjFn(objFn)

	lp.Solve()

	sum := 0
	for _, x := range lp.Variables() {
		sum += int(x)
	}

	return int(sum)
}
