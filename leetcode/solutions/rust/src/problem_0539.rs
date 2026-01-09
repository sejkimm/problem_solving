struct Solution;

impl Solution {
    pub fn find_min_difference(time_points: Vec<String>) -> i32 {
        let time_points: Vec<i32> = time_points
            .into_iter()
            .map(|x| {
                let x_split: Vec<_> = x.split(':').collect();
                return x_split[0].parse::<i32>().unwrap() * 60
                    + x_split[1].parse::<i32>().unwrap();
            })
            .collect();

        let mut min_diff = i32::MAX;

        for (first_idx, &first) in time_points.iter().enumerate() {
            for &second in &time_points[first_idx + 1..] {
                let diff = first - second;

                min_diff = std::cmp::min(
                    min_diff,
                    std::cmp::min(diff.abs(), std::cmp::min(1440 + diff, 1440 - diff)),
                );
            }
        }

        return min_diff;
    }
}

pub fn run_tests() {
    assert_eq!(
        1,
        Solution::find_min_difference(
            vec!["23:59", "00:00"]
                .into_iter()
                .map(|x| String::from(x))
                .collect()
        )
    );
    assert_eq!(
        0,
        Solution::find_min_difference(
            vec!["00:00", "23:59", "00:00"]
                .into_iter()
                .map(|x| String::from(x))
                .collect()
        )
    );
    assert_eq!(
        40,
        Solution::find_min_difference(
            vec!["23:30", "00:10"]
                .into_iter()
                .map(|x| String::from(x))
                .collect()
        )
    );
}
