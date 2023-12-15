use std::fs;

fn main() {
    let file_path = "./input";
    let input = fs::read_to_string(file_path).expect("Should have been able to read the file");
    let inputs = input
        .lines()
        .map(|l| {
            let mut ll = l.split(" ");
            return (ll.next().unwrap(), parse_numbers(ll.next().unwrap()));
        })
        .collect::<Vec<_>>();

    println!(
        "{}",
        inputs.iter().map(|(s, l)| possibilities(s, l)).sum::<i32>()
    )
}

fn possibilities(map: &str, l: &[i32]) -> i32 {
    if l.len() == 0 {
        if !map.contains("#") {
            return 1;
        }
        return 0;
    }
    let spring_len = l.first().unwrap().clone() as usize;

    let mut possible = 0;

    let mut check_replaces = vec!["#", "."];
    if !map.contains("?") {
        check_replaces = vec!["$"];
    }

    for try_char in check_replaces {
        let s = map.replacen("?", try_char, 1);
        let st = s.trim_start_matches(".");

        if l.iter().sum::<i32>() > st.matches(['#', '?']).count() as i32 {
            continue;
        }

        let prefix = st.split_once(".").unwrap_or_else(|| (st, "")).0;
        if prefix.contains("?") {
            possible += possibilities(st, l);
        } else if prefix == "#".repeat(spring_len) {
            possible += possibilities(&st[spring_len..], &l[1..]);
        }
    }

    return possible;
}

fn parse_numbers(s: &str) -> Vec<i32> {
    s.split(',').map(|x| x.parse().ok().unwrap()).collect()
}
