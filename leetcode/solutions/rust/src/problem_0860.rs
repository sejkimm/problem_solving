pub struct Solution;

impl Solution {
    pub fn lemonade_change(bills: Vec<i32>) -> bool {
        let mut count_5: i32 = 0;
        let mut count_10: i32 = 0;

        for &bill in bills.iter() {
            match bill {
                5 => {
                    count_5 += 1;
                }
                10 => {
                    if count_5 >= 1 {
                        count_5 -= 1;
                        count_10 += 1;
                    } else {
                        return false;
                    }
                }
                20 => {
                    if count_10 >= 1 && count_5 >= 1 {
                        count_5 -= 1;
                        count_10 -= 1;
                    } else if count_5 >= 3 {
                        count_5 -= 3;
                    } else {
                        return false;
                    }
                }
                _ => {}
            }
        }

        return true;
    }
}

pub fn run_tests() {
    assert_eq!(true, Solution::lemonade_change(vec![5, 5, 5, 10, 20]));
    assert_eq!(false, Solution::lemonade_change(vec![5, 5, 10, 10, 20]));
}
