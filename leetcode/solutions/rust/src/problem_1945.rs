struct Solution;

impl Solution {
    pub fn get_lucky(s: String, k: i32) -> i32 {
        let mut sum_of_digits: i32 = s
            .into_bytes()
            .iter()
            .flat_map(|&x| {
                let converted = x.checked_sub(b'a' - 1).unwrap() as i32;
                if converted >= 10 {
                    vec![converted / 10, converted % 10]
                } else {
                    vec![converted]
                }
            })
            .sum::<i32>();

        for _ in 1..k {
            sum_of_digits = sum_of_digits
                .to_string()
                .into_bytes()
                .iter()
                .map(|&x| x.checked_sub(b'0').unwrap() as i32)
                .sum::<i32>();
        }

        return sum_of_digits;
    }
}

pub fn run_tests() {
    assert_eq!(36, Solution::get_lucky(String::from("iiii"), 1));
    assert_eq!(6, Solution::get_lucky(String::from("leetcode"), 2));
    assert_eq!(8, Solution::get_lucky(String::from("zbax"), 2));
    assert_eq!(
        9,
        Solution::get_lucky(String::from("abcdefghijklmnopqrstuvwxyz"), 10)
    );
    assert_eq!(
        4,
        Solution::get_lucky(
            String::from("hwmqsaqvrliksiobdtbtxiztnextxsvpoqeyfvxlnrcwlaqh"),
            9
        )
    );
}
