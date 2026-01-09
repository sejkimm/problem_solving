impl Solution {
    pub fn int_to_roman(num: i32) -> String {
        let mut temp_num: i32 = num;
        let mut answer: String = String::from("");

        while temp_num > 0 {
            if temp_num >= 1000 {
                temp_num -= 1000;
                answer.push_str("M");
            } else if temp_num >= 900 {
                temp_num -= 900;
                answer.push_str("CM");
            } else if temp_num >= 500 {
                temp_num -= 500;
                answer.push_str("D");
            } else if temp_num >= 400 {
                temp_num -= 400;
                answer.push_str("CD");
            } else if temp_num >= 100 {
                temp_num -= 100;
                answer.push_str("C");
            } else if temp_num >= 90 {
                temp_num -= 90;
                answer.push_str("XC");
            } else if temp_num >= 50 {
                temp_num -= 50;
                answer.push_str("L");
            } else if temp_num >= 40 {
                temp_num -= 40;
                answer.push_str("XL");
            } else if temp_num >= 10 {
                temp_num -= 10;
                answer.push_str("X");
            } else if temp_num >= 9 {
                temp_num -= 9;
                answer.push_str("IX");
            } else if temp_num >= 5 {
                temp_num -= 5;
                answer.push_str("V");
            } else if temp_num >= 4 {
                temp_num -= 4;
                answer.push_str("IV");
            } else {
                temp_num -= 1;
                answer.push_str("I");
            }
        }

        return answer;
    }
}
