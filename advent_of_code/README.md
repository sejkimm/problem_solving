# advent-of-code

## 2023

## 2024

## 2025

### How to run rust code?

```bash
cargo run -- <day> <part> <input_variant>
```

- `<day>`: The specific day of the challenge (e.g., day1).
- `<part>`: The part of the challenge to solve (e.g., part1 or part2).
- `<input_variant>`: The input file variant (input or example).

#### Code Structure

```bash
/{2024,2025}/
  |-- Cargo.toml           # Project configuration
  |-- src/
      |-- main.rs          # Entry point for running the challenges
      |-- solutions/       # Solution modules for each day
          |-- mod.rs       # Module manager
          |-- day1.rs      # Solutions for day1 (part1 and part2)
  |-- day1/
      |-- input_part1.txt  # Main input for part1
      |-- input_part2.txt  # Main input for part2
      |-- example_input_part1.txt  # Example input for part1
      |-- example_input_part2.txt  # Example input for part2
```
