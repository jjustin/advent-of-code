use std::fs;

fn main() {
    let file_path = "./input";
    let input = fs::read_to_string(file_path).expect("Should have been able to read the file");

    let mut res = 0;

    for line in input.lines() {
        let l: Vec<&str> = line.split(":").last().unwrap().split("|").collect();

        let winning = parse_numbers(l[0]);
        let drawn = parse_numbers(l[1]);

        let mut current_draw = 0;

        for d in drawn {
            if winning.contains(&d) {
                if current_draw == 0 {
                    current_draw = 1;
                } else {
                    current_draw *= 2;
                }
            }
        }

        res += current_draw
    }

    println!("{}", res)
}

fn parse_numbers(s: &str) -> Vec<i32> {
    s.split_whitespace()
        .map(|x| x.parse().ok().unwrap())
        .collect()
}
