struct Solution;

impl Solution {
    pub fn find_complement(num: i32) -> i32 {
        let mut binary_representation: Vec<bool> = Vec::new();
        let mut temp_num: i32 = num;
        let mut complement: i32 = 0;

        while temp_num > 0 {
            binary_representation.push(temp_num & 1 != 0);
            temp_num >>= 1;
        }

        for elem in binary_representation.iter_mut() {
            *elem = !*elem;
        }

        for (idx, &elem) in binary_representation.iter().enumerate() {
            complement += if elem { 2_i32.pow(idx as u32) } else { 0 };
        }

        return complement;
    }
}
pub fn run_tests() {
    assert_eq!(2, Solution::find_complement(5));
    assert_eq!(0, Solution::find_complement(1));
    assert_eq!(0, Solution::find_complement(2147483647)); /* 2^31-1 */
    assert_eq!(2400, Solution::find_complement(2147481247));
}
