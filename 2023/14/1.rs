use std::fs;

const EMPTY: char = '.';
const MOVE: char = 'O';

type Map = Vec<Vec<char>>;

fn main() {
    let file_path = "./input";
    let input = fs::read_to_string(file_path).expect("Should have been able to read the file");

    let mut map: Map = input.lines().map(|l| l.chars().collect()).collect();

    north(&mut map);

    println!(
        "{}",
        map.iter()
            .rev()
            .enumerate()
            .map(|(score, col)| (score + 1) * col.iter().filter(|&&c| c == MOVE).count())
            .sum::<usize>()
    )
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
