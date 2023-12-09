use std::{collections::HashMap, fs};

fn main() {
    let file_path = "./input";
    let input = fs::read_to_string(file_path).expect("Should have been able to read the file");

    let mut input_lines = input.lines();
    let instruction = input_lines.next().unwrap();
    input_lines.next();

    let mut map = HashMap::<String, (String, String)>::new();

    for section in input_lines {
        let mut parts = section.split(" = ");
        let node_name = parts.next().unwrap().to_string();
        let destinations: Vec<String> = parts
            .next()
            .unwrap()
            .split(", ")
            .map(|x| x.replace(&['(', ')'], ""))
            .collect();

        map.insert(
            node_name,
            (destinations[0].clone(), destinations[1].clone()),
        );
    }

    let mut current_node = "AAA";
    let mut count = 0;
    for way in instruction.chars().cycle() {
        if current_node == "ZZZ" {
            break;
        }

        count += 1;

        let (left, right) = map.get(current_node).unwrap();

        current_node = match way {
            'L' => left,
            'R' => right,
            _ => panic!("Unknown way {}", way),
        }
    }

    println!("{}", count)
}
