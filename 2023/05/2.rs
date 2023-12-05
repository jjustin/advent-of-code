use std::fs;

fn main() {
    let file_path = "./input";
    let input = fs::read_to_string(file_path).expect("Should have been able to read the file");

    let mut maps = input.split("\n\n");
    let seeds_str = maps.next().unwrap().replace("seeds: ", "");
    let mut seed_ranges = parse_numbers(&seeds_str)
        .chunks(2)
        .map(|c| (c[0], c[0] + c[1] - 1))
        .collect::<Vec<(i64, i64)>>();

    for map in maps {
        let mut new_seeds = Vec::<(i64, i64)>::new();
        for (i, line) in map.lines().enumerate() {
            if i == 0 {
                continue;
            }

            let mapping = parse_numbers(line);
            let destination = mapping[0];
            let origin = mapping[1];
            let delta = mapping[2];
            let destination_last = destination + delta - 1;
            let origin_last = origin + delta - 1;

            seed_ranges.retain_mut(|(seed_start, seed_end)| {
                if *seed_start >= origin && *seed_start <= origin_last {
                    // Contains start -> start will be changed
                    let new_start = destination + (*seed_start - origin);
                    if *seed_end <= origin_last {
                        // Fully contained
                        let new_end = new_start + (*seed_end - *seed_start);

                        new_seeds.push((new_start, new_end));
                        return false;
                    } else {
                        // End not contained

                        let new_end = destination_last;
                        new_seeds.push((new_start, new_end));

                        *seed_start = origin_last + 1;
                        return true;
                    }
                } else if *seed_end >= origin && *seed_end <= origin_last {
                    // Doesn't contain start -> Start wont be changed.

                    let new_end = destination + (*seed_end - origin);
                    new_seeds.push((destination, new_end));

                    *seed_end = origin - 1;
                    return true;
                }

                return true;
            });
        }
        seed_ranges.append(&mut new_seeds);
    }

    println!("{}", seed_ranges.iter().map(|(x, _)| x).min().unwrap())
}

fn parse_numbers(s: &str) -> Vec<i64> {
    s.split_whitespace()
        .map(|x| x.parse().ok().unwrap())
        .collect()
}
