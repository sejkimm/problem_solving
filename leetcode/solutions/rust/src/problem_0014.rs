pub struct Solution;

impl Solution {
    pub fn longest_common_prefix(strs: Vec<String>) -> String {
        let min_len = strs.iter().map(|s| s.len()).min().unwrap_or(0);

        for str_idx in 0..min_len {
            let first_char_slice = &strs[0][0..=str_idx];

            if !strs.iter().all(|s| s.starts_with(first_char_slice)) {
                return strs[0][0..str_idx].to_string();
            }
        }

        strs[0][0..min_len].to_string()
    }
}

pub fn run_tests() {
    assert_eq!(
        "fl",
        Solution::longest_common_prefix(["flower", "flow", "flight"].map(String::from).to_vec())
    );
    assert_eq!(
        "",
        Solution::longest_common_prefix(["dog", "racecar", "car"].map(String::from).to_vec())
    );
    assert_eq!(
        "flower",
        Solution::longest_common_prefix(["flower", "flower", "flower"].map(String::from).to_vec())
    );
    assert_eq!(
        "",
        Solution::longest_common_prefix([""].map(String::from).to_vec())
    );
}
