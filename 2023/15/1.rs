use std::fs;

fn main() {
    let file_path = "./input";
    let input = fs::read_to_string(file_path).expect("Should have been able to read the file");

    let mut res = 0;

    for instruction in input.trim().split(',') {
        let r = hash(instruction);
        res += r;
    }

    println!("{}", res)
}

fn hash(s: &str) -> i32 {
    let mut i = 0;
    for c in s.chars() {
        i += c as i32;
        i *= 17;
        i %= 256;
    }

    return i;
}
