use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

pub struct Day1;

impl super::Solution for Day1 {
    fn run_part1(input_file: &str) {
        println!("Reading Part 1 from file: {}", input_file);
        let input = if let Ok(input) = parse_input(input_file) {
            input
        } else {
            eprintln!("Error parsing input file: {}", input_file);
            return;
        };
        let result = solve_part1(input);
        println!("Part 1 Result: {}", result);
    }

    fn run_part2(input_file: &str) {
        println!("Reading Part 2 from file: {}", input_file);
        let input = if let Ok(input) = parse_input(input_file) {
            input
        } else {
            eprintln!("Error parsing input file: {}", input_file);
            return;
        };
        let result = solve_part2(input);
        println!("Part 2 Result: {}", result);
    }
}

fn parse_input(input_file: &str) -> Result<(Vec<char>, Vec<i32>), io::Error> {
    let lines = read_lines(input_file)?;
    let mut rotations = Vec::<char>::new();
    let mut numbers = Vec::<i32>::new();

    for line in lines {
        if let Ok(value) = line {
            let (rotation, number) = value.split_at(1);
            let rotation_char = rotation.chars().next().unwrap();
            let number_int = number.parse::<i32>().unwrap();

            rotations.push(rotation_char);
            numbers.push(number_int);
        }
    }

    return Ok((rotations, numbers));
}

fn solve_part1(input: (Vec<char>, Vec<i32>)) -> u32 {
    let mut cursor: i32 = 50;
    let mut zero_count: u32 = 0;
    let (rotations, numbers) = input;

    for (rotation, number) in rotations.iter().zip(numbers.iter()) {
        match rotation {
            'R' => {
                cursor += number;
                cursor %= 100;
            }
            'L' => {
                cursor -= number % 100;
                if cursor < 0 {
                    cursor += 100;
                } else {
                    cursor %= 100;
                }
            }
            _ => {
                return 0;
            }
        }

        if cursor == 0 {
            zero_count += 1;
        }
    }

    return zero_count;
}

fn solve_part2(input: (Vec<char>, Vec<i32>)) -> u32 {
    let mut cursor: i32 = 50;
    let mut zero_count: u32 = 0;
    let (rotations, numbers) = input;

    for (rotation, number) in rotations.iter().zip(numbers.iter()) {
        match rotation {
            'R' => {
                cursor += number;
                zero_count += (cursor / 100) as u32;
                cursor %= 100;
            }
            'L' => {
                if cursor == 0 {
                    zero_count += (number / 100) as u32;
                    cursor = 100 - (number % 100);
                } else {
                    cursor -= number;
                    if cursor <= 0 {
                        zero_count += ((cursor * (-1) / 100) + 1) as u32;
                        cursor = 100 - (cursor * (-1) % 100);
                    }
                }

                cursor %= 100;
            }
            _ => {
                return 0;
            }
        }

        print!("cursor: {}, zero_count: {}\n", cursor, zero_count);
    }

    return zero_count;
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
