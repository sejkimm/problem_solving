use std::collections::HashMap;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

pub struct Day1;

impl super::Solution for Day1 {
    fn run_part1(input_file: &str) {
        println!("Reading Part 1 from file: {}", input_file);
        let numbers = load_numbers_from_file(input_file);
        let result = solve_part1(numbers);
        println!("Part 1 Result: {}", result);
    }

    fn run_part2(input_file: &str) {
        println!("Reading Part 2 from file: {}", input_file);
        let numbers = load_numbers_from_file(input_file);
        let result = solve_part2(numbers);
        println!("Part 2 Result: {}", result);
    }
}

fn load_numbers_from_file(input_file: &str) -> (Vec<i32>, Vec<i32>) {
    let lines = read_lines(input_file).expect("Could not read input file");
    let mut left_numbers = Vec::new();
    let mut right_numbers = Vec::new();

    for line in lines {
        if let Ok(value) = line {
            let nums: Vec<i32> = value
                .split_whitespace()
                .filter_map(|x| x.parse().ok())
                .collect();
            if nums.len() == 2 {
                left_numbers.push(nums[0]);
                right_numbers.push(nums[1]);
            }
        }
    }

    return (left_numbers, right_numbers);
}

fn solve_part1(mut numbers: (Vec<i32>, Vec<i32>)) -> i32 {
    let mut distance: i32 = 0;

    numbers.0.sort();
    numbers.1.sort();

    for (a, b) in numbers.0.iter().zip(numbers.1.iter()) {
        distance += (a - b).abs();
    }

    return distance;
}

fn solve_part2(numbers: (Vec<i32>, Vec<i32>)) -> i32 {
    let mut similarity: i32 = 0;

    let mut right_occurrences: HashMap<i32, i32> = HashMap::<i32, i32>::new();

    for &number in numbers.1.iter() {
        *right_occurrences.entry(number).or_insert(0) += 1;
    }

    for &number in numbers.0.iter() {
        similarity += number * (right_occurrences.get(&number).unwrap_or(&0));
    }

    return similarity;
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
