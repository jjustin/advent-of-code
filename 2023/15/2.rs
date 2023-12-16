use std::fs;

fn main() {
    let file_path = "./input";
    let input = fs::read_to_string(file_path).expect("Should have been able to read the file");
    let mut boxes: Vec<Vec<(&str, i32)>> = vec![vec![]; 256];
    let mut res = 0;

    for instruction in input.trim().split(',') {
        if instruction.ends_with('-') {
            let label = &instruction[..instruction.len() - 1];
            let r = hash(label) as usize;
            let ix = boxes[r].iter().position(|&(x, _)| x == label);
            match ix {
                Some(i) => {
                    boxes[r].remove(i);
                }
                None => (),
            }
        }

        if instruction.contains('=') {
            let (label, val) = instruction.split_once("=").unwrap();
            let i: i32 = val.parse().unwrap();
            let r = hash(label) as usize;
            let b = &mut boxes[r];
            let ix = b.iter().position(|&(x, _)| x == label);
            match ix {
                Some(idx) => b[idx] = (label, i),
                None => b.push((label, i)),
            }
        }
    }

    for (box_ix, b) in boxes.iter().enumerate() {
        for (slot_ix, &(_, focal_len)) in b.iter().enumerate() {
            res += (box_ix + 1) * (slot_ix + 1) * (focal_len as usize)
        }
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
