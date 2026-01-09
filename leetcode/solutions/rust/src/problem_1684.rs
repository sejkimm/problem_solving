use std::collections::HashSet;

struct Solution;

impl Solution {
    pub fn count_consistent_strings(allowed: String, words: Vec<String>) -> i32 {
        let allowed_set: HashSet<char> = allowed.chars().collect();

        let count: i32 = words
            .into_iter()
            .map(|word| word.chars().all(|c| allowed_set.contains(&c)))
            .filter(|&x| x)
            .count() as i32;

        return count;
    }
}

pub fn run_tests() {
    assert_eq!(
        2,
        Solution::count_consistent_strings(
            String::from("ab"),
            ["ad", "bd", "aaab", "baa", "badab"]
                .into_iter()
                .map(|x| String::from(x))
                .collect()
        )
    );
    assert_eq!(
        7,
        Solution::count_consistent_strings(
            String::from("abc"),
            ["a", "b", "c", "ab", "ac", "bc", "abc"]
                .into_iter()
                .map(|x| String::from(x))
                .collect()
        )
    );
    assert_eq!(
        4,
        Solution::count_consistent_strings(
            String::from("cad"),
            ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]
                .into_iter()
                .map(|x| String::from(x))
                .collect()
        )
    );
}
