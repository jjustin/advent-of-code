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

		z, err := strconv.Atoi(parts[2])
		if err != nil {
			panic(err)
		}

		points = append(points, Point{x: x, y: y, z: z})
	}

	fmt.Println(solve1(points, 1000))
	fmt.Println(solve2(points))
}

type Point struct {
	x, y, z int
	cluster *[]*Point
}

func (p1 *Point) distance(p2 *Point) float64 {
	return math.Sqrt(
		math.Pow(float64(p1.x-p2.x), 2) +
			math.Pow(float64(p1.y-p2.y), 2) +
			math.Pow(float64(p1.z-p2.z), 2),
	)
}

func (p1 *Point) connect(p2 *Point) {
	for _, p := range *p2.cluster {
		*p1.cluster = append(*p1.cluster, p)
	}
	for _, p := range *p1.cluster {
		if p == p1 {
			continue
		}
		p.cluster = p1.cluster
	}
}

type Pair struct {
	a, b     *Point
	distance float64
}

func NewPair(a, b *Point) Pair {
	return Pair{
		a:        a,
		b:        b,
		distance: a.distance(b),
	}
}

func preparePoints(pointsOriginal []Point) ([]*Point, []Pair) {
	points := []*Point{}

	for _, p := range pointsOriginal {
		p.cluster = &[]*Point{&p}
		points = append(points, &p)
	}

	pairs := []Pair{}

	for i, a := range points {
		for _, b := range points[:i] {
			if a == b {
				continue
			}

			pairs = append(pairs, NewPair(a, b))
		}
	}

	slices.SortStableFunc(pairs, func(a Pair, b Pair) int {
		if a.distance < b.distance {
			return -1
		}
		if a.distance == b.distance {
			return 0
		}
		return 1
	})

	return points, pairs
}

func solve1(pointsOriginal []Point, moves int) int {
	points, pairs := preparePoints(pointsOriginal)

	for _, pair := range pairs[:moves] {
		if pair.a.cluster == pair.b.cluster {
			continue
		}
		pair.a.connect(pair.b)
	}

	lengths := []int{}
	for _, p := range points {
		l := len(*p.cluster)
		if slices.Contains(lengths, l) {
			continue
		}
		lengths = append(lengths, l)
	}

	slices.SortFunc(lengths, func(a int, b int) int { return b - a })

	return lengths[0] * lengths[1] * lengths[2]
}

func solve2(pointsOriginal []Point) int {
	points, pairs := preparePoints(pointsOriginal)

	for _, pair := range pairs {
		if pair.a.cluster == pair.b.cluster {
			continue
		}
		pair.a.connect(pair.b)
		if len(*pair.a.cluster) == len(points) {
			return pair.a.x * pair.b.x
		}
	}

	return -1
}

// Unused helper
func printClusters(points []*Point) {
	alreadyPrinted := [](*[]*Point){}

	for _, p := range points {
		if slices.Contains(alreadyPrinted, p.cluster) {
			continue
		}

		for _, pi := range *p.cluster {
			fmt.Print(pi)
		}
		fmt.Println()

		alreadyPrinted = append(alreadyPrinted, p.cluster)
	}
	fmt.Println()
}
