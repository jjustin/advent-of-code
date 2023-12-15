use std::{collections::HashMap, fs};

const EMPTY: char = '.';
const MOVE: char = 'O';

type Map = Vec<Vec<char>>;

fn main() {
    let file_path = "./input";
    let input = fs::read_to_string(file_path).expect("Should have been able to read the file");

    let mut map: Map = input.lines().map(|l| l.chars().collect()).collect();
    let mut cache: HashMap<String, i32> = HashMap::new();

    const wanted_cycles: i32 = 1000000000;
    for i in 1..wanted_cycles {
        cycle(&mut map);
        let key = map_string(&map);
        if cache.contains_key(&key) {
            let cycle_start = cache.get(&key).unwrap();
            let diff = i - cycle_start;
            let needed_cycles = (wanted_cycles - cycle_start) % diff;
            for j in 0..needed_cycles {
                cycle(&mut map);
            }
            break;
        }
        cache.insert(key, i);
    }

    println!(
        "{}",
        map.iter()
            .rev()
            .enumerate()
            .map(|(score, col)| (score + 1) * col.iter().filter(|&&c| c == MOVE).count())
            .sum::<usize>()
    )
}

fn cycle(map: &mut Map) {
    north(map);
    rotate90(map);
    north(map);
    rotate90(map);
    north(map);
    rotate90(map);
    north(map);
    rotate90(map);
}

fn north(map: &mut Map) {
    let w = map[0].len();
    let h = map.len();

    for col in 0..w {
        let mut prev = map[0][col];
        let mut move_to: usize = 0;

        for row in 1..h {
            let mut curr = map[row][col];
            if prev != EMPTY {
                move_to = row;
            }
            if curr == MOVE {
                map[row][col] = EMPTY;
                map[move_to][col] = MOVE;
                curr = map[row][col];
                move_to += 1;
            }

            prev = curr;
        }
    }
}

fn rotate90(map: &mut Map) {
    let w = map[0].len();
    let h = map.len();

    for j in 0..w {
        let mut newc: Vec<char> = vec![];
        for i in (0..h).rev() {
            newc.push(map[i][j]);
        }

        map.push(newc);
    }

    map.drain(0..h);
}

fn map_string(map: &Map) -> String {
    return map.iter().flat_map(|x| x.iter()).collect();
}
