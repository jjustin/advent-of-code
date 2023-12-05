use std::{collections::HashMap, fs};

fn main() {
    let file_path = "./input";
    let input = fs::read_to_string(file_path).expect("Should have been able to read the file");

    let mut maps = input.split("\n\n");
    let seeds_str = &maps.next().unwrap().replace("seeds: ", "");
    let mut seeds = parse_numbers(&seeds_str);

    for map in maps {
        let mut mapped_seeds = HashMap::<i64, i64>::new();

        for (i, line) in map.lines().enumerate() {
            if i == 0 {
                continue;
            }

            let mapping = parse_numbers(line);
            let destination = mapping[0];
            let origin = mapping[1];
            let delta = mapping[2];

            for seed in &seeds {
                if origin <= *seed && seed < &(origin + delta) {
                    let diff = seed - origin;
                    mapped_seeds.insert(*seed, destination + diff);
                }
            }
        }

        let mut new_seeds = Vec::<i64>::new();
        for seed in &seeds {
            let mut new_seed = seed;
            match mapped_seeds.get(&seed) {
                Some(x) => new_seed = x,
                None => (),
            }
            new_seeds.push(*new_seed);
        }

        seeds = new_seeds;
    }

    println!("{}", seeds.iter().min().unwrap())
}

fn parse_numbers(s: &str) -> Vec<i64> {
    s.split_whitespace()
        .map(|x| x.parse().ok().unwrap())
        .collect()
}
