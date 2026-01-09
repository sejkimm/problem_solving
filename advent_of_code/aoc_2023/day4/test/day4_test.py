from solution.part1_solution import main as part1_main
from solution.part2_solution import main as part2_main


def test_part1_solution_with_example_input():
    answer: int = part1_main(input_file_name="example_input.txt")

    assert answer == 13


def test_part2_solution_with_example_input():
    answer: int = part2_main(input_file_name="example_input.txt")

    assert answer == 30
