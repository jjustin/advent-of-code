use std::fs;

fn main() {
    let file_path = "./input";
    let input = fs::read_to_string(file_path).expect("Should have been able to read the file");
    let mut res = 0;
    let patterns = input.split("\n\n");

    for pattern in patterns {
        let lines: Vec<&str> = pattern.lines().collect();
        let height = pattern.lines().count().clone();
        let width = pattern.split_once("\n").unwrap().0.len();

        let mut possible = (1..width).collect::<Vec<_>>();
        for line in lines.iter() {
            possible.retain(|&col| {
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
        if possible.len() != 0 {
            res += possible.iter().sum::<usize>();
        }

        possible = (1..height).collect();
        possible.retain(|&row| {
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

        if possible.len() != 0 {
            res += possible.iter().map(|x| x * 100).sum::<usize>();
        }
    }

    println!("{}", res)
}
