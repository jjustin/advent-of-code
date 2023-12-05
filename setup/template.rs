use std::fs;

fn main() {
    let file_path = "./input";
    let input = fs::read_to_string(file_path).expect("Should have been able to read the file");

    let mut res = 0;

    for line in input.lines() {}

    println!("{}", res)
}

fn parse_numbers(s: &str) -> Vec<i32> {
    s.split_whitespace()
        .map(|x| x.parse().ok().unwrap())
        .collect()
}
