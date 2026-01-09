struct Solution;

impl Solution {
    pub fn construct2_d_array(original: Vec<i32>, m: i32, n: i32) -> Vec<Vec<i32>> {
        if (m * n) as usize != original.len() {
            return Vec::<Vec<i32>>::new();
        }

        let new_array: Vec<Vec<i32>> = original
            .chunks(n as usize)
            .map(|chunk| chunk.to_vec())
            .collect();

        return new_array;
    }
}

pub fn run_tests() {
    assert_eq!(
        vec![vec![1, 2], vec![3, 4]],
        Solution::construct2_d_array(vec![1, 2, 3, 4], 2, 2)
    );
    assert_eq!(
        vec![vec![1, 2, 3]],
        Solution::construct2_d_array(vec![1, 2, 3], 1, 3)
    );

    assert_eq!(
        Vec::<Vec::<i32>>::new(),
        Solution::construct2_d_array(vec![1, 2], 1, 1)
    );
}
