struct Solution;

impl Solution {
    pub fn hamming_distance(x: i32, y: i32) -> i32 {
        return (x ^ y).count_ones() as i32;
    }
}

pub fn run_tests() {
    assert_eq!(2, Solution::hamming_distance(1, 4));
    assert_eq!(1, Solution::hamming_distance(3, 1));
}
