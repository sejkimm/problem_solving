use std::collections::HashSet;

struct Solution;

impl Solution {
    pub fn robot_sim(commands: Vec<i32>, obstacles: Vec<Vec<i32>>) -> i32 {
        let directions: [(i32, i32); 4] = [(0, 1), (1, 0), (0, -1), (-1, 0)];
        let mut direction: usize = 0;
        let mut position: (i32, i32) = (0, 0);
        let mut longest_distance: i32 = 0;

        let obstacles: HashSet<(i32, i32)> = obstacles.into_iter().map(|x| (x[0], x[1])).collect();

        for command in commands {
            match command {
                1..=9 => {
                    for _ in 0..command {
                        let next_position = (
                            position.0 + directions[direction].0,
                            position.1 + directions[direction].1,
                        );

                        if obstacles.contains(&next_position) {
                            break;
                        }

                        position = next_position;
                    }
                    longest_distance = std::cmp::max(
                        longest_distance,
                        position.0 * position.0 + position.1 * position.1,
                    );
                }
                -1 => {
                    direction = (direction + 1) % 4;
                }
                -2 => {
                    direction = (direction + 3) % 4;
                }
                _ => {}
            };
        }

        return longest_distance;
    }
}

pub fn run_tests() {
    assert_eq!(25, Solution::robot_sim(vec![4, -1, 3], vec![]));
    assert_eq!(
        65,
        Solution::robot_sim(vec![4, -1, 4, -2, 4], vec![vec![2, 4]])
    );
    assert_eq!(36, Solution::robot_sim(vec![6, -1, -1, 6], vec![]));
}
