impl Solution {
    pub fn length_of_last_word(s: String) -> i32 {
        let mut last_word_len: i32 = 0;
        let mut current_word_len: i32 = 0;

        for c in s.chars() {
            match c {
                ' ' => current_word_len = 0,
                _ => current_word_len += 1,
            }

            if current_word_len > 0 {
                last_word_len = current_word_len;
            }
        }

        return last_word_len;
    }
}
