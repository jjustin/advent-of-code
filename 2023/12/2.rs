use std::{collections::HashMap, fs};

fn main() {
    let file_path = "./input";
    let input = fs::read_to_string(file_path).expect("Should have been able to read the file");
    let inputs = input
        .lines()
        .map(|l| {
            let mut ll = l.split(" ");

            let mut springs = (ll.next().unwrap().to_string() + "?").repeat(5);
            springs.pop();
            let base_l = parse_numbers(ll.next().unwrap());
            let mut ls = Vec::<i32>::new();
            for _ in 0..5 {
                for l in &base_l {
                    ls.push(l.clone());
                }
            }

            return (springs, ls);
        })
        .collect::<Vec<_>>();

    println!(
        "{}",
        inputs
            .iter()
            .map(|(s, l)| possibilities(s, l, 0, &mut HashMap::new()))
            .sum::<i64>()
    )
}

fn possibilities(map: &str, l: &[i32], d: i32, cache: &mut HashMap<String, i64>) -> i64 {
    let key = format!("{map}{l:?}");
    if cache.contains_key(&key) {
        return cache.get(&key).unwrap().clone();
    }

    if l.len() == 0 {
        if !map.contains("#") {
            return 1;
        }
        return 0;
    }
    let spring_len = l.first().unwrap().clone() as usize;

    let mut possible: i64 = 0;

    let mut check_replaces = vec!["#", "."];
    if !map.contains("?") {
        check_replaces = vec!["$"];
    }

    for try_char in check_replaces {
        let s = map.replacen("?", try_char, 1);
        let st = s.trim_start_matches(".");

        // Not enough springs
        if l.iter().sum::<i32>() > st.matches(['#', '?']).count() as i32 {
            continue;
        }

        let prefix = st.split_once(".").unwrap_or_else(|| (st, "")).0;
        if prefix.contains("?") {
            possible += possibilities(st, l, d + 1, cache);
        } else if prefix == "#".repeat(spring_len) {
            possible += possibilities(&st[spring_len..], &l[1..], d + 1, cache);
        }
    }

    cache.insert(key, possible);

    return possible;
}

fn parse_numbers(s: &str) -> Vec<i32> {
    s.split(',').map(|x| x.parse().ok().unwrap()).collect()
}
