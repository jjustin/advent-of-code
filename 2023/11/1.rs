use std::fs;

fn main() {
    let file_path = "./input";
    let input = fs::read_to_string(file_path).expect("Should have been able to read the file");

    let map = input
        .lines()
        .map(|l| l.chars().collect::<Vec<_>>())
        .collect::<Vec<_>>();

    let empty_rows = map
        .iter()
        .enumerate()
        .filter(|(_, l)| l.iter().all(|&c| c == '.'))
        .map(|(i, _)| i)
        .collect::<Vec<_>>();
    let mut empty_columns = Vec::new();

    for column_ix in 0..map[0].len() {
        if map.iter().all(|row| row[column_ix] == '.') {
            empty_columns.push(column_ix);
        }
    }

    let galaxyies = map
        .iter()
        .enumerate()
        .flat_map(|(i, v)| {
            v.iter()
                .enumerate()
                .filter(|(_, &c)| c == '#')
                .map(|(j, _)| (i, j))
                .collect::<Vec<_>>()
        })
        .collect::<Vec<_>>();

    let mut galaxy_pairs: Vec<((usize, usize), (usize, usize))> = vec![];
    for i in 0..galaxyies.len() {
        for j in i + 1..galaxyies.len() {
            galaxy_pairs.push((galaxyies[i], galaxyies[j]));
        }
    }

    let distances_sum = galaxy_pairs
        .iter()
        .map(|(g1, g2)| {
            let ymin = std::cmp::min(g1.0, g2.0);
            let ymax = std::cmp::max(g1.0, g2.0);
            let xmin = std::cmp::min(g1.1, g2.1);
            let xmax = std::cmp::max(g1.1, g2.1);

            let y_expansions = empty_rows.iter().filter(|&&v| ymin < v && v < ymax).count() as i32;
            let x_expansions = empty_columns
                .iter()
                .filter(|&&v| xmin < v && v < xmax)
                .count() as i32;

            return (g1.0 as i32 - g2.0 as i32).abs()
                + y_expansions
                + (g1.1 as i32 - g2.1 as i32).abs()
                + x_expansions;
        })
        .sum::<i32>();

    println!("{:?}", distances_sum);
}
