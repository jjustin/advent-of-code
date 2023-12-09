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

    let mut lengths = Vec::<i64>::new();

    for starting_node in map.keys().filter(|v| v.ends_with("A")) {
        let mut current_node = starting_node.clone();
        let mut count = 0;

        for way in instruction.chars().cycle() {
            if current_node.ends_with("Z") {
                break;
            }

            count += 1;

            let (left, right) = map.get(&current_node).unwrap();

            current_node = match way {
                'L' => left.clone(),
                'R' => right.clone(),
                _ => panic!("Unknown way {}", way),
            }
        }
        lengths.push(count);
    }

    println!("{}", lcm(&lengths))
}

pub fn lcm(nums: &[i64]) -> i64 {
    if nums.len() == 1 {
        return nums[0];
    }
    let a = nums[0];
    let b = lcm(&nums[1..]);
    a * b / gcd(a, b)
}

fn gcd(a: i64, b: i64) -> i64 {
    if b == 0 {
        return a;
    }
    gcd(b, a % b)
}
