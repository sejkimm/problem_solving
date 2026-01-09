struct Solution;

impl Solution {
    pub fn min_bit_flips(start: i32, goal: i32) -> i32 {
        let bitwise_xor = start ^ goal;

        return bitwise_xor.count_ones() as i32;
    }
}

pub fn run_tests() {
    assert_eq!(3, Solution::min_bit_flips(3, 4));
    assert_eq!(3, Solution::min_bit_flips(10, 7));
}
