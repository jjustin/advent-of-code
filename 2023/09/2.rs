use std::fs;

fn main() {
    let file_path = "./input";
    let input = fs::read_to_string(file_path).expect("Should have been able to read the file");

    let mut res = 0;

    for line in input.lines() {
        let mut history = Vec::<Vec<i32>>::new();
        let seq = parse_numbers(line);

        history.push(seq.clone());
        while !history.last().unwrap().iter().all(|&x| x == 0) {
            let prev = history.last().expect("no last set");
            let current = prev.windows(2).map(|x| x[1] - x[0]).collect::<Vec<i32>>();

            history.push(current.clone());
        }

        history.reverse();

        let mut prev = 0;
        for seq in history {
            let new = seq.first().unwrap() - prev;
            prev = new;
        }

        // println!("{:?}", history);
        res += prev;
    }

    println!("{}", res)
}

fn parse_numbers(s: &str) -> Vec<i32> {
    s.split_whitespace()
        .map(|x| x.parse().ok().unwrap())
        .collect()
}
