use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

pub struct Day4;

impl super::Solution for Day4 {
    fn run_part1(input_file: &str) {
        println!("Reading from file: {}", input_file);
        let words: Vec<String> = load_lines_from_file(input_file);
        let result = solve_part1(words);
        println!("Result: {}", result);
    }

    fn run_part2(input_file: &str) {
        println!("Reading from file: {}", input_file);
        let words: Vec<String> = load_lines_from_file(input_file);
        let result = solve_part2(words);
        println!("Result: {}", result);
    }
}

fn load_lines_from_file(input_file: &str) -> Vec<String> {
    let lines = read_lines(input_file).expect("Could not read input file");
    let mut output_lines: Vec<String> = Vec::<String>::new();

    for line in lines {
        if let Ok(value) = line {
            output_lines.push(value);
        }
    }

    return output_lines;
}

fn solve_part1(words: Vec<String>) -> i32 {
    let mut occurrences: i32 = 0;
    let x_len: usize = words.get(0).unwrap().len();
    let y_len: usize = words.len();
    let words_clone: Vec<String> = words.clone();
    let target_words = ["XMAS", "SAMX"];

    for (y_idx, word) in words.iter().enumerate() {
        for (x_idx, _) in word.chars().into_iter().enumerate() {
            if x_len - x_idx >= 4 {
                let cursor_word = &word[x_idx..x_idx + 4];
                if target_words.contains(&cursor_word) {
                    occurrences += 1;
                }
            }

            if y_len - y_idx >= 4 {
                let cursor_word: String = (0..4)
                    .map(|i| char_at(&words_clone, y_idx + i, x_idx))
                    .collect();
                if target_words.contains(&cursor_word.as_str()) {
                    occurrences += 1;
                }
            }

            if (y_len - y_idx >= 4) && (x_len - x_idx >= 4) {
                let cursor_word: String = (0..4)
                    .map(|i| char_at(&words_clone, y_idx + i, x_idx + i))
                    .collect();
                if target_words.contains(&cursor_word.as_str()) {
                    occurrences += 1;
                }
            }

            if (y_len - y_idx >= 4) && (x_idx >= 3) {
                let cursor_word: String = (0..4)
                    .map(|i| char_at(&words_clone, y_idx + i, x_idx - i))
                    .collect();
                if target_words.contains(&cursor_word.as_str()) {
                    occurrences += 1;
                }
            }
        }
    }

    return occurrences;
}

fn solve_part2(words: Vec<String>) -> i32 {
    let mut occurrences: i32 = 0;
    let x_len: usize = words.get(0).unwrap().len();
    let y_len: usize = words.len();

    for y_idx in 0..(y_len - 2) {
        for x_idx in 0..(x_len - 2) {
            let top_left: char = char_at(&words, y_idx, x_idx);
            let top_right: char = char_at(&words, y_idx, x_idx + 2);
            let mid: char = char_at(&words, y_idx + 1, x_idx + 1);
            let bottom_left: char = char_at(&words, y_idx + 2, x_idx);
            let bottom_right: char = char_at(&words, y_idx + 2, x_idx + 2);

            if mid == 'A' {
                if (top_left == 'M')
                    && (top_right == 'M')
                    && (bottom_left == 'S')
                    && (bottom_right == 'S')
                {
                    occurrences = occurrences + 1;
                }

                if (top_left == 'S')
                    && (top_right == 'S')
                    && (bottom_left == 'M')
                    && (bottom_right == 'M')
                {
                    occurrences = occurrences + 1;
                }

                if (top_left == 'S')
                    && (top_right == 'M')
                    && (bottom_left == 'S')
                    && (bottom_right == 'M')
                {
                    occurrences = occurrences + 1;
                }

                if (top_left == 'M')
                    && (top_right == 'S')
                    && (bottom_left == 'M')
                    && (bottom_right == 'S')
                {
                    occurrences = occurrences + 1;
                }
            }
        }
    }

    return occurrences;
}

fn char_at(words: &Vec<String>, y: usize, x: usize) -> char {
    words[y].chars().nth(x).unwrap()
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
