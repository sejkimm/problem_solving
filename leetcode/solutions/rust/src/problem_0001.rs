impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        for (first_num_idx, first_num) in nums.iter().enumerate() {
            for (second_num_idx, second_num) in nums.iter().enumerate().skip(first_num_idx + 1) {
                if first_num + second_num == target {
                    return vec![first_num_idx as i32, second_num_idx as i32];
                }
            }
        }

        vec![]
    }
}
