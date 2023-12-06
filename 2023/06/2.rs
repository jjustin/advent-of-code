use std::{fs, iter::zip};

fn main() {
    let file_path = "./input";
    let input = fs::read_to_string(file_path).expect("Should have been able to read the file");
    let mut input_lines = input.lines();

    let mut res = 1;

    let times = parse_numbers(input_lines.next().unwrap().split(":").last().unwrap());
    let distances = parse_numbers(input_lines.next().unwrap().split(":").last().unwrap());

    for (time, distance) in zip(times, distances) {
        let a = 1.0 / distance as f64;
        let b = -time as f64 / distance as f64;
        let c = 1.0;

        let sq = (b * b - 4.0 * a * c).sqrt();

        let mut x1 = (-b - sq) / (2.0 * a);
        if x1.fract() == 0.0 {
            x1 += 1.0;
        }

        let mut x2 = (-b + sq) / (2.0 * a);
        if x2.fract() == 0.0 {
            x2 -= 1.0;
        }

        let possibilities = x2.floor() as i64 - x1.ceil() as i64 + 1; // +1 because it's inclusive
        res *= possibilities;
    }

    println!("{}", res)
}

fn parse_numbers(s: &str) -> Vec<i64> {
    s.replace(" ", "")
        .split_whitespace()
        .map(|x| x.parse().ok().unwrap())
        .collect()
}
