struct Solution;

impl Solution {
    pub fn xor_queries(arr: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        
        /*
        More Optimized Solution: 
        calculate every elem in arr from index 0 to end
        and access only left and right value when query applied.
        */ 
        let answer: Vec<i32> = queries
            .into_iter()
            .map(|query| {
                let left = query[0];
                let right = query[1];
                let mut xor_result: i32 = 0;

                for idx in left..=right {
                    xor_result = xor_result ^ arr[idx as usize];
                }

                xor_result
            })
            .collect();

        return answer;
    }
}

pub fn run_tests() {
    assert_eq!(
        vec![2, 7, 14, 8],
        Solution::xor_queries(
            vec![1, 3, 4, 8],
            vec![[0, 1], [1, 2], [0, 3], [3, 3]]
                .into_iter()
                .map(|x| Vec::from(x))
                .collect()
        )
    );
    assert_eq!(
        vec![8, 0, 4, 4],
        Solution::xor_queries(
            vec![4, 8, 2, 10],
            vec![[2, 3], [1, 3], [0, 0], [0, 3]]
                .into_iter()
                .map(|x| Vec::from(x))
                .collect()
        )
    );
}
