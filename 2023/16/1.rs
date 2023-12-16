use std::{collections::HashMap, fs, vec};

type Map = Vec<Vec<char>>;

const L: char = 'L';
const U: char = 'U';
const D: char = 'D';
const R: char = 'R';

fn main() {
    let file_path = "./input";
    let input = fs::read_to_string(file_path).expect("Should have been able to read the file");

    let map: Map = input.lines().map(|l| l.chars().collect()).collect();
    let h = map.len();
    let w = map[0].len();
    let mut history: Map = vec![vec!['.'; w]; h];

    simulate(
        &map,
        0 as i32,
        0 as i32,
        R,
        &mut history,
        &mut HashMap::new(),
    );

    println!(
        "{:?}",
        history.iter().flatten().filter(|&&c| c == '#').count()
    )
}

fn simulate(
    map: &Map,
    x: i32,
    y: i32,
    direction: char,
    history: &mut Map,
    cache: &mut HashMap<String, bool>,
) {
    let h = map.len() as i32;
    let w = map[0].len() as i32;

    if y < 0 || y >= h || x < 0 || x >= w {
        return;
    }

    let key = format!("{} {} {}", x, y, direction);
    if cache.contains_key(&key) {
        return;
    }
    cache.insert(key, true);

    history[y as usize][x as usize] = '#';

    match map[y as usize][x as usize] {
        '.' => match direction {
            U => simulate(map, x, y - 1, direction, history, cache),
            D => simulate(map, x, y + 1, direction, history, cache),
            L => simulate(map, x - 1, y, direction, history, cache),
            R => simulate(map, x + 1, y, direction, history, cache),
            _ => unreachable!(),
        },
        '|' => match direction {
            U => simulate(map, x, y - 1, direction, history, cache),
            D => simulate(map, x, y + 1, direction, history, cache),
            L | R => {
                simulate(map, x, y + 1, D, history, cache);
                simulate(map, x, y - 1, U, history, cache);
            }
            _ => unreachable!(),
        },
        '-' => match direction {
            L => simulate(map, x - 1, y, direction, history, cache),
            R => simulate(map, x + 1, y, direction, history, cache),
            U | D => {
                simulate(map, x - 1, y, L, history, cache);
                simulate(map, x + 1, y, R, history, cache);
            }
            _ => unreachable!(),
        },
        '\\' => match direction {
            L => simulate(map, x, y - 1, U, history, cache),
            R => simulate(map, x, y + 1, D, history, cache),
            D => simulate(map, x + 1, y, R, history, cache),
            U => simulate(map, x - 1, y, L, history, cache),
            _ => unreachable!(),
        },
        '/' => match direction {
            L => simulate(map, x, y + 1, D, history, cache),
            R => simulate(map, x, y - 1, U, history, cache),
            D => simulate(map, x - 1, y, L, history, cache),
            U => simulate(map, x + 1, y, R, history, cache),
            _ => unreachable!(),
        },
        _ => unreachable!(),
    }
}
