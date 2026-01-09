use std::collections::{HashMap, HashSet};

struct Solution;

impl Solution {
    pub fn uncommon_from_sentences(s1: String, s2: String) -> Vec<String> {
        let mut appearance = HashMap::<String, i32>::new();

        for elem in s1.split(" ").into_iter().chain(s2.split(" ").into_iter()) {
            *appearance.entry(elem.to_string()).or_insert(0) += 1;
        }

        return appearance
            .iter()
            .filter(|(_, &count)| count == 1)
            .map(|(word, _)| word.clone())
            .collect::<Vec<String>>();
    }
}

pub fn run_tests() {
    assert_eq!(
        vec!["sweet", "sour"]
            .into_iter()
            .map(|x| String::from(x))
            .collect::<Vec<String>>()
            .into_iter()
            .collect::<HashSet<String>>(),
        Solution::uncommon_from_sentences(
            String::from("this apple is sweet"),
            String::from("this apple is sour")
        )
        .into_iter()
        .collect::<HashSet<String>>()
    );
    assert_eq!(
        vec!["banana"]
            .into_iter()
            .map(|x| String::from(x))
            .collect::<Vec<String>>()
            .into_iter()
            .collect::<HashSet<String>>(),
        Solution::uncommon_from_sentences(String::from("apple apple"), String::from("banana"))
            .into_iter()
            .collect::<HashSet<String>>()
    );
}
