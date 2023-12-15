use std::fs;

fn main() {
    let file_path = "./input";
    let input = fs::read_to_string(file_path).expect("Should have been able to read the file");
    let mut res = 0;
    let patterns = input.split("\n\n");

    for original_pattern in patterns {
        let _original = reflections(original_pattern).unwrap();
        let original = &_original[..];

        for i in 0..original_pattern.len() {
            let mut pattern = original_pattern.to_string();
            let replacing_char = pattern.as_bytes()[i] as char;
            if replacing_char == '\n' {
                continue;
            }

            pattern.replace_range(
                i..i + 1,
                match replacing_char {
                    '#' => ".",
                    '.' => "#",
                    _ => unreachable!(),
                },
            );

            let mut done = false;

            let possible = reflections(pattern.as_str());
            match &possible {
                None => (),
                Some(x) => match x {
                    org if org == original => (),
                    different => {
                        println!("Diff: {:?}", different);
                        for score in different {
                            if !original.contains(score) {
                                res += score;
                                done = true;
                            }
                        }
                    }
                },
            }

            if done {
                break;
            }
        }
    }

    println!("{}", res)
}

fn reflections(pattern: &str) -> Option<Vec<usize>> {
    let height: usize = pattern.lines().count().clone();
    let width = pattern.split_once("\n").unwrap().0.len();
    let lines: Vec<&str> = pattern.lines().collect();

    let mut possible1 = (1..width).collect::<Vec<_>>();
    for line in lines.iter() {
        possible1.retain(|&col| {
            let mut s1 = &line[0..col];
            let mut s2 = &line[col..width];

            if s1.len() < s2.len() {
                s2 = &s2[0..s1.len()];
            }
            if s2.len() < s1.len() {
                s1 = &s1[s1.len() - s2.len()..s1.len()]
            }

            let s2reversed = s2.chars().rev().collect::<String>();
            s2 = s2reversed.as_str();

            s1 == s2
        });
    }

    let mut possible2 = (1..height).collect::<Vec<_>>();
    possible2.retain(|&row| {
        let mut above = &lines[0..row];
        let mut below = &lines[row..lines.len()];

        if above.len() < below.len() {
            below = &below[0..above.len()];
        }
        if below.len() < above.len() {
            above = &above[above.len() - below.len()..above.len()];
        }
        let tmp = below.iter().rev().cloned().collect::<Vec<_>>();
        below = &tmp[..];

        below == above
    });

    let mut possible = Vec::<usize>::new();

    if possible1.len() != 0 {
        possible.append(&mut possible1);
    }
    if possible2.len() != 0 {
        let mut tmp: Vec<usize> = possible2.iter().map(|x| x * 100).collect();
        possible.append(&mut tmp)
    }

    if possible.len() > 0 {
        return Some(possible);
    }

    return None;
}
