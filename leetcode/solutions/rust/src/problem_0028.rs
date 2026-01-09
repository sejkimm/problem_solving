pub struct Solution;

impl Solution {
    pub fn str_str(haystack: String, needle: String) -> i32 {
        if haystack.len() < needle.len() {
            return -1;
        }

        for idx in 0..=(haystack.len() - needle.len()) {
            if haystack[idx..idx + needle.len()] == needle {
                return idx as i32;
            }
        }

        return -1;

        /* or,

        match haystack.find(&needle) {
            Some(i) => return i as i32,
            None => return -1,
        }

         */
    }
}

pub fn run_tests() {
    assert_eq!(
        0,
        Solution::str_str(String::from("sadbutsad"), String::from("sad"))
    );
    assert_eq!(
        -1,
        Solution::str_str(String::from("leetcode"), String::from("leeto"))
    );
    assert_eq!(
        3,
        Solution::str_str(String::from("leleletcode"), String::from("elet"))
    );
    assert_eq!(
        4,
        Solution::str_str(String::from("mississippi"), String::from("issip"))
    );
    assert_eq!(0, Solution::str_str(String::from("a"), String::from("a")));
    assert_eq!(
        -1,
        Solution::str_str(String::from("aaa"), String::from("aaaaa"))
    );
}
