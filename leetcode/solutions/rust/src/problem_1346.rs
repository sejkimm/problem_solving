use std::collections::HashSet;

struct Solution;

impl Solution {
    pub fn check_if_exist(arr: Vec<i32>) -> bool {
        let mut occurrences: HashSet<i32> = HashSet::<i32>::new();

        for elem in arr.into_iter() {
            if occurrences.contains(&elem) {
                return true;
            }

            occurrences.insert(elem * 2);

            if &elem % 2 == 0 {
                occurrences.insert(elem / 2);
            }
        }

        return false;
    }
}

pub fn run_tests() {
    assert_eq!(true, Solution::check_if_exist(vec![10, 2, 5, 3]));
    assert_eq!(false, Solution::check_if_exist(vec![3, 1, 7, 11]));
    assert_eq!(false, Solution::check_if_exist(vec![4, -7, 11, 4, 18]));
}
