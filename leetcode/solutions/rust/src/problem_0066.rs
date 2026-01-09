impl Solution {
    pub fn plus_one(digits: Vec<i32>) -> Vec<i32> {
        let mut added: Vec<i32> = Vec::new();
        let mut carry: bool = false;

        for (idx, &value) in digits.iter().rev().enumerate() {
            let mut value = value;

            if idx == 0 {
                value += 1;
            }

            if carry {
                value += 1;
            }

            if value > 9 {
                added.push(value - 10);
                carry = true;
            } else {
                added.push(value);
                carry = false;
            }
        }

        if carry {
            added.push(1);
        }

        return added.into_iter().rev().collect();
    }
}
