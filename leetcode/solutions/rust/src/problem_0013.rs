use std::collections::HashMap;

impl Solution {
    pub fn roman_to_int(s: String) -> i32 {
        let mut symbol_to_value: HashMap<char, i32> = HashMap::new();
        let mut prev_c: Option<char> = None;
        let mut value: i32 = 0;

        symbol_to_value.insert('I', 1);
        symbol_to_value.insert('V', 5);
        symbol_to_value.insert('X', 10);
        symbol_to_value.insert('L', 50);
        symbol_to_value.insert('C', 100);
        symbol_to_value.insert('D', 500);
        symbol_to_value.insert('M', 1000);

        for c in s.chars() {
            match symbol_to_value.get(&c) {
                Some(match_value) => value += match_value,
                _ => {}
            };

            match c {
                'I' => {}
                'V' | 'X' => {
                    if prev_c == Some('I') {
                        match symbol_to_value.get(&'I') {
                            Some(match_value) => value -= 2 * match_value,
                            _ => {}
                        }
                    }
                }
                'L' | 'C' => {
                    if prev_c == Some('X') {
                        match symbol_to_value.get(&'X') {
                            Some(match_value) => value -= 2 * match_value,
                            _ => {}
                        }
                    }
                }
                'D' | 'M' => {
                    if prev_c == Some('C') {
                        match symbol_to_value.get(&'C') {
                            Some(match_value) => value -= 2 * match_value,
                            _ => {}
                        }
                    }
                }
                _ => {}
            }

            prev_c = Some(c);
        }

        value
    }
}
