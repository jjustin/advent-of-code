use core::panic;
use std::{collections::HashMap, fs};

type From = char;

const FROM_UP: From = 'U';
const FROM_LEFT: From = 'L';
const FROM_RIGHT: From = 'R';
const FROM_DOWN: From = 'D';

fn opposite_direction(direction: From) -> From {
    return match direction {
        FROM_UP => FROM_DOWN,
        FROM_DOWN => FROM_UP,
        FROM_LEFT => FROM_RIGHT,
        FROM_RIGHT => FROM_LEFT,
        _ => panic!("Bad direction {}", direction),
    };
}
fn main() {
    let file_path = "./input";
    let input = fs::read_to_string(file_path).expect("Should have been able to read the file");

    let mut map = HashMap::<((i32, i32), From), ((i32, i32), From)>::new();

    let mut map_raw: Vec<Vec<char>> = input
        .lines()
        .into_iter()
        .map(|line| line.chars().collect())
        .collect();

    let mut start_point: (i32, i32) = (0, 0);

    let height = input.lines().collect::<Vec<&str>>().len() as i32;
    let length = input.lines().next().unwrap().len() as i32;

    // Populate map
    for (row, line) in input.lines().enumerate() {
        for (column, c) in line.chars().enumerate() {
            if c == '.' {
                continue;
            }
            if c == 'S' {
                start_point = (column as i32, row as i32);
                continue;
            }

            let mappings: Vec<((i32, i32), From, From)> = match c {
                '|' => vec![((0, 1), FROM_UP, FROM_UP), ((0, -1), FROM_DOWN, FROM_DOWN)],
                '-' => vec![
                    ((1, 0), FROM_LEFT, FROM_LEFT),
                    ((-1, 0), FROM_RIGHT, FROM_RIGHT),
                ],
                'L' => vec![
                    ((1, 0), FROM_UP, FROM_LEFT),
                    ((0, -1), FROM_RIGHT, FROM_DOWN),
                ],
                'J' => vec![
                    ((0, -1), FROM_LEFT, FROM_DOWN),
                    ((-1, 0), FROM_UP, FROM_RIGHT),
                ],
                '7' => vec![
                    ((0, 1), FROM_LEFT, FROM_UP),
                    ((-1, 0), FROM_DOWN, FROM_RIGHT),
                ],
                'F' => vec![
                    ((1, 0), FROM_DOWN, FROM_LEFT),
                    ((0, 1), FROM_RIGHT, FROM_UP),
                ],
                x => panic!("Char {} found bot not mapped", x),
            };

            for ((xdiff, ydiff), origin, destination) in mappings {
                let k = ((column as i32, row as i32), origin);
                let v = ((column as i32 + xdiff, row as i32 + ydiff), destination);
                map.insert(k, v);
            }
        }
    }

    // Add start point mappings to map
    let clone_map = map.clone();
    let start_mappings: Vec<(&((i32, i32), char), &((i32, i32), char))> = clone_map
        .iter()
        .filter(|(_, (point, _))| point == &start_point)
        .collect();

    let start_neigh1 = start_mappings[0].0.clone();
    let start1 = start_mappings[0].1.clone();
    let start_neigh2 = start_mappings[1].0.clone();
    let start2 = start_mappings[1].1.clone();
    map.insert(start1, (start_neigh2.0, opposite_direction(start2.1)));
    map.insert(start2, (start_neigh1.0, opposite_direction(start1.1)));

    // Update start point in raw map
    let start_mappings_directions = start_mappings
        .iter()
        .map(|(_, (_, d))| d.clone())
        .collect::<Vec<char>>();

    map_raw[start_point.1 as usize][start_point.0 as usize] =
        match start_mappings_directions.as_slice() {
            [FROM_DOWN, FROM_UP] | [FROM_UP, FROM_DOWN] => '|',
            [FROM_RIGHT, FROM_LEFT] | [FROM_LEFT, FROM_RIGHT] => '-',
            [FROM_DOWN, FROM_LEFT] | [FROM_LEFT, FROM_DOWN] => '7',
            [FROM_DOWN, FROM_RIGHT] | [FROM_RIGHT, FROM_DOWN] => 'F',
            [FROM_UP, FROM_RIGHT] | [FROM_RIGHT, FROM_UP] => 'L',
            [FROM_UP, FROM_LEFT] | [FROM_LEFT, FROM_UP] => 'j',
            _ => 'S',
        };

    let mut destination = FROM_DOWN;
    if !map.contains_key(&(start_point, destination)) {
        destination = FROM_UP;
    }
    if !map.contains_key(&(start_point, destination)) {
        destination = FROM_LEFT;
    } else if !map.contains_key(&(start_point, destination)) {
        panic!("No start destination found")
    }

    // Get points that are part of the pipe
    let mut loop_points = Vec::<(i32, i32)>::new();
    let mut current_point = start_point.clone();
    loop {
        loop_points.push(current_point);

        (current_point, destination) = map
            .get(&(current_point, destination))
            .expect(&format!("not found: {:?} {}", current_point, destination))
            .clone();

        if current_point == start_point {
            break;
        }
    }

    // Check each row how many "inloop" points the map has
    let mut count = 0;
    for y in 0..height {
        let mut inloop = false;
        let mut onpipe: char = 0 as char;

        for x in 0..length {
            if loop_points.contains(&(x, y)) {
                let t = map_raw[y as usize][x as usize];

                if onpipe == 0 as char {
                    if vec!['L', '7', 'J', 'F'].contains(&t) {
                        onpipe = t;
                    } else if t == '|' {
                        inloop = !inloop;
                    }
                } else if onpipe != 0 as char {
                    inloop = match (onpipe, t) {
                        (_, '-') | ('-', _) => inloop,
                        ('L', '7') | ('7', 'L') => !inloop,
                        ('L', 'J') | ('J', 'L') => inloop,
                        ('F', 'J') | ('J', 'F') => !inloop,
                        ('F', '7') | ('7', 'F') => inloop,
                        pair => panic!("got pair: {pair:?}"),
                    };
                    if onpipe != '-' && t != '-' {
                        onpipe = 0 as char;
                    };
                } else {
                    panic!("unhandled {t}");
                }
            } else if inloop {
                count += 1;
            }
        }
    }

    println!("{}", count)
}
