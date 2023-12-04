use std::{collections::HashMap, fs};

fn main() {
    let file_path = "./input";
    let input = fs::read_to_string(file_path).expect("Should have been able to read the file");

    let max_game_number = input.lines().count() as i32;
    let mut count_of_tickets: HashMap<i32, i32> = HashMap::new();

    for i in 1..max_game_number + 1 {
        count_of_tickets.insert(i, 1);
    }

    for line in input.lines() {
        let mut split = line.split(":");
        let game_number = split
            .next()
            .unwrap()
            .split_whitespace()
            .last()
            .unwrap()
            .parse::<i32>()
            .ok()
            .unwrap();
        let card_numbers: Vec<&str> = split.last().unwrap().split("|").collect();

        let winning = parse_numbers(card_numbers[0]);
        let drawn = parse_numbers(card_numbers[1]);

        let mut current_draw = 0;

        for drawn_number in drawn {
            if winning.contains(&drawn_number) {
                current_draw += 1;
            }
        }

        for increased_game_number in
            game_number + 1..std::cmp::min(game_number + current_draw + 1, max_game_number + 1)
        {
            count_of_tickets.insert(
                increased_game_number,
                count_of_tickets.get(&increased_game_number).unwrap()
                    + count_of_tickets.get(&game_number).unwrap(),
            );
        }
    }

    println!("{}", count_of_tickets.values().sum::<i32>())
}

fn parse_numbers(s: &str) -> Vec<i32> {
    s.split_whitespace()
        .map(|x| x.parse().ok().unwrap())
        .collect()
}
