use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

pub struct Day2;

impl super::Solution for Day2 {
    fn run_part1(input_file: &str) {
        println!("Reading Part 1 from file: {}", input_file);
        let reports = load_numbers_from_file(input_file);
        let result = solve_part1(reports);
        println!("Part 1 Result: {}", result);
    }

    fn run_part2(input_file: &str) {
        println!("Reading Part 2 from file: {}", input_file);
        let reports = load_numbers_from_file(input_file);
        let result = solve_part2(reports);
        println!("Part 2 Result: {}", result);
    }
}

fn load_numbers_from_file(input_file: &str) -> Vec<Vec<i32>> {
    let lines = read_lines(input_file).expect("Could not read input file");
    let mut reports: Vec<Vec<i32>> = Vec::new();

    for line in lines {
        if let Ok(value) = line {
            let report: Vec<i32> = value
                .split_whitespace()
                .filter_map(|x| x.parse().ok())
                .collect();
            reports.push(report);
        }
    }

    return reports;
}

fn is_safe_report(report: Vec<i32>) -> bool {
    let mut is_increasing: Option<bool> = None;
    let mut prev_report_elem: i32 = match report.get(0) {
        Some(&value) => value,
        None => return false,
    };

    for &report_elem in report.iter().skip(1) {
        if report_elem == prev_report_elem {
            return false;
        }

        if !(1 <= (report_elem - prev_report_elem).abs()
            && (report_elem - prev_report_elem).abs() <= 3)
        {
            return false;
        }

        match is_increasing {
            Some(value) => {
                if value != (prev_report_elem < report_elem) {
                    return false;
                }
            }
            None => is_increasing = Some(prev_report_elem < report_elem),
        };

        prev_report_elem = report_elem;
    }

    return true;
}

fn solve_part1(reports: Vec<Vec<i32>>) -> i32 {
    let mut safe_report_count: i32 = 0;

    for report in reports.into_iter() {
        if is_safe_report(report) {
            safe_report_count += 1;
        }
    }

    return safe_report_count;
}

fn solve_part2(reports: Vec<Vec<i32>>) -> i32 {
    let mut safe_report_count: i32 = 0;

    for report in reports.into_iter() {
        for skip_idx in 0..report.len() {
            let filtered_report: Vec<i32> = report
                .iter()
                .enumerate()
                .filter(|(i, _)| *i != skip_idx)
                .map(|(_, &v)| v)
                .collect();

            if is_safe_report(filtered_report) {
                safe_report_count += 1;
                break;
            }
        }
    }

    return safe_report_count;
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
