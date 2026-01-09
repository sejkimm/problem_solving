impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        if x < 0 {
            return false;
        }

        let string_representation = x.to_string();
        let bytes_representation = string_representation.as_bytes();

        let mut left = 0;
        let mut right = bytes_representation.len() - 1;

        while left < right {
            if bytes_representation[left] != bytes_representation[right] {
                return false;
            }

            left += 1;
            right -= 1;
        }

        return true;
    }
}
