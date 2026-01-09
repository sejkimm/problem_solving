use regex::Regex;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
pub struct Day3;

impl super::Solution for Day3 {
    fn run_part1(input_file: &str) {
        println!("Reading from file: {}", input_file);
        let memory: String = load_lines_from_file(input_file);
        let result = solve_part1(memory);
        println!("Result: {}", result);
    }

    fn run_part2(input_file: &str) {
        println!("Reading from file: {}", input_file);
        let memory: String = load_lines_from_file(input_file);
        let result = solve_part2(memory);
        println!("Result: {}", result);
    }
}

fn load_lines_from_file(input_file: &str) -> String {
    let lines = read_lines(input_file).expect("Could not read input file");
    let mut output_lines: String = String::new();

    for line in lines {
        if let Ok(value) = line {
            output_lines.push_str(&value);
        }
    }

    return output_lines;
}

fn solve_part1(memory: String) -> i32 {
    let mul_re = Regex::new(r"mul\([0-9]+,[0-9]+\)").unwrap();
    let value_re = Regex::new(r"[0-9]+").unwrap();

    let mul_patterns: Vec<&str> = mul_re.find_iter(&memory).map(|x| x.as_str()).collect();

    let sum: i32 = mul_patterns
        .iter()
        .map(|&pattern| {
            value_re
                .find_iter(pattern)
                .map(|value| value.as_str().parse::<i32>().unwrap())
                .product::<i32>()
        })
        .sum();

    return sum;
}

fn solve_part2(memory: String) -> i32 {
    let pad_memory: String = String::from("do()") + &memory + "do()";
    let to_remove_re = Regex::new(r"don't\(\).*?do\(\)").unwrap();
    let mul_re = Regex::new(r"mul\([0-9]+,[0-9]+\)").unwrap();
    let value_re = Regex::new(r"[0-9]+").unwrap();

    let memory_filtered: String = to_remove_re.replace_all(&pad_memory, "").to_string();

    let mul_patterns: Vec<&str> = mul_re
        .find_iter(&memory_filtered)
        .map(|x| x.as_str())
        .collect();

    let sum: i32 = mul_patterns
        .iter()
        .map(|&pattern| {
            value_re
                .find_iter(pattern)
                .map(|value| value.as_str().parse::<i32>().unwrap())
                .product::<i32>()
        })
        .sum();

    return sum;
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
