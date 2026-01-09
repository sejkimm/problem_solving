use std::collections::HashSet;

struct Solution;

impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        let mut num_set: HashSet<i32> = HashSet::new();

        for num in nums.iter() {
            if num_set.contains(num) {
                return true;
            }

            num_set.insert(*num);
        }

        return false;
    }
}

pub fn run_tests() {
    assert_eq!(true, Solution::contains_duplicate(vec![1, 2, 3, 1]));
    assert_eq!(false, Solution::contains_duplicate(vec![1, 2, 3, 4]));
    assert_eq!(
        true,
        Solution::contains_duplicate(vec![1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
    );
}
