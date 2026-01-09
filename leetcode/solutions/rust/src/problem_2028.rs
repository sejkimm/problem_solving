struct Solution;

impl Solution {
    pub fn missing_rolls(rolls: Vec<i32>, mean: i32, n: i32) -> Vec<i32> {
        let rolls_len: i32 = rolls.len().try_into().unwrap();
        let mut missing_value_sum: i32 = mean * (n + rolls_len) - rolls.iter().sum::<i32>();
        let mut missing_dice: Vec<i32> = Vec::<i32>::new();

        for iteration in (0..n).rev() {
            match missing_value_sum - iteration {
                x if x >= 6 => {
                    missing_dice.push(6);
                    missing_value_sum -= 6;
                }
                x if x >= 1 => {
                    missing_dice.push(x);
                    missing_value_sum -= x;
                }
                _ => {
                    missing_dice.push(1);
                    missing_value_sum -= 1;
                }
            }
        }

        if missing_value_sum != 0 {
            return Vec::<i32>::new();
        }

        return missing_dice;
    }
}

pub fn run_tests() {
    assert_eq!(vec![6, 6], Solution::missing_rolls(vec![3, 2, 4, 3], 4, 2));
    assert_eq!(
        vec![] as Vec::<i32>,
        Solution::missing_rolls(vec![1, 2, 3, 4], 6, 4)
    );
    assert_eq!(
        vec![] as Vec::<i32>,
        Solution::missing_rolls(vec![6, 3, 4, 3, 5, 3], 1, 6)
    );
}
