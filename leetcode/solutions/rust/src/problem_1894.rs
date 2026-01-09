struct Solution;

impl Solution {
    pub fn chalk_replacer(chalk: Vec<i32>, k: i32) -> i32 {
        let remainder: i64 = (k as i64).rem_euclid(chalk.iter().map(|&x| x as i64).sum::<i64>());
        let mut partial_sum: i64 = 0;

        for (idx, &ith_chalk) in chalk.iter().enumerate() {
            if partial_sum + (ith_chalk as i64) > remainder {
                return idx.try_into().unwrap();
            }

            partial_sum += (ith_chalk as i64);
        }

        unreachable!()
    }
}

pub fn run_tests() {
    assert_eq!(0, Solution::chalk_replacer(vec![5, 1, 5], 22));
    assert_eq!(1, Solution::chalk_replacer(vec![3, 4, 1, 2], 25));
}
