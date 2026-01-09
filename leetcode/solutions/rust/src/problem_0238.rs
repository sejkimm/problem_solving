impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let nums_len: usize = nums.len();

        let mut mul_from_left: Vec<i32> = vec![0; nums_len];
        let mut mul_from_right: Vec<i32> = vec![0; nums_len];
        let mut mul_except_myself: Vec<i32> = vec![0; nums_len];

        mul_from_left[0] = nums[0];
        mul_from_right[nums_len - 1] = nums[nums_len - 1];

        for idx in 1..nums_len {
            mul_from_left[idx] = mul_from_left[idx - 1] * nums[idx];
        }

        for idx in (0..(nums_len - 1)).rev() {
            mul_from_right[idx] = mul_from_right[idx + 1] * nums[idx];
        }

        mul_except_myself[0] = mul_from_right[1];
        mul_except_myself[nums_len - 1] = mul_from_left[nums_len - 2];

        for idx in 1..(nums_len - 1) {
            mul_except_myself[idx] = mul_from_left[idx - 1] * mul_from_right[idx + 1];
        }

        mul_except_myself
    }
}
