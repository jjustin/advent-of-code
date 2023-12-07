use core::panic;
use std::{collections::HashMap, fs};

fn main() {
    let file_path = "./input";
    let input = fs::read_to_string(file_path).expect("Should have been able to read the file");

    let mut hands: Vec<(&str, i32, i32)> = Vec::new();

    for line in input.lines() {
        let mut split = line.split(" ");

        let hand = split.next().unwrap();
        let hand_value = enumerate_hand(hand);

        let bet = split.next().unwrap().parse::<i32>().unwrap();

        hands.push((hand, hand_value, bet));
    }

    hands.sort_by(|(_, hv1, _), (_, hv2, _)| hv1.cmp(hv2));

    let res: i32 = hands
        .iter()
        .enumerate()
        .map(|(i, (_, _, bet))| (i as i32 + 1) * bet)
        .sum();

    println!("{}", res);
}

// enumerate_hand transform hand to unique number. Think of this function as
// transform from base 13 to base 10.
fn enumerate_hand(hand: &str) -> i32 {
    let mut count_by_card = HashMap::<char, i32>::new();

    for c in hand.chars() {
        *count_by_card.entry(c).or_insert(0) += 1;
    }

    let mut counts = count_by_card.values().collect::<Vec<&i32>>();
    counts.sort_by(|a, b| b.cmp(a));

    let mut value = match counts.get(0).unwrap() {
        5 => 7,
        4 => 6,
        3 => match counts.get(1).unwrap() {
            2 => 5,
            1 => 4,
            x => panic!("Unhandled count 3 -> {}", x),
        },
        2 => match counts.get(1).unwrap() {
            2 => 3,
            1 => 2,
            x => panic!("Unhandled count 2 -> {}", x),
        },
        1 => 1,
        x => panic!("Unhandled count {}", x),
    };

    for card in hand.chars() {
        value *= 13;
        value += card_to_value(card);
    }

    return value;
}

// card_to_value maps card to integer.
fn card_to_value(c: char) -> i32 {
    return match c {
        '2'..='9' => c as i32 - '2' as i32,
        'T' => 8,
        'J' => 9,
        'Q' => 10,
        'K' => 11,
        'A' => 12,
        x => panic!("card to value unhandled {}", x),
    };
}
