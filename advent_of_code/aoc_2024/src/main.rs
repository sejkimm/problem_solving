use std::env;

mod solutions;

fn get_input_file(day: &str, part: &str, variant: &str) -> String {
    match variant {
        "input" | "example" => format!("{}/{}_{}.txt", day, variant, part),
        _ => {
            eprintln!(
                "Invalid input variant: {}. Use 'input' or 'example'.",
                variant
            );
            std::process::exit(1);
        }
    }
}

fn run_solution(day: &str, part: &str, input_file: &str) {
    use solutions::*;

    macro_rules! run_day {
        ($day:ty) => {
            match part {
                "part1" => <$day>::run_part1(input_file),
                "part2" => <$day>::run_part2(input_file),
                _ => {
                    eprintln!("Invalid part: {}. Use 'part1' or 'part2'.", part);
                    std::process::exit(1);
                }
            }
        };
    }

    match day {
        "day1" => run_day!(day1::Day1),
        "day2" => run_day!(day2::Day2),
        "day3" => run_day!(day3::Day3),
        "day4" => run_day!(day4::Day4),
        _ => {
            eprintln!("Day {} is not implemented!", day);
            std::process::exit(1);
        }
    }
}

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() < 3 {
        eprintln!("Usage: cargo run -- <day> <part> <input_variant>");
        std::process::exit(1);
    }

    let day = &args[1];
    let part = &args[2];
    let variant = args.get(3).map_or("input", String::as_str);

    let input_file = get_input_file(day, part, variant);
    run_solution(day, part, &input_file);
}
