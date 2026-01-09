pub struct Solution;

impl Solution {
    pub fn min_steps(n: i32) -> i32 {
        if n == 1 {
            return 0;
        }

        let mut sieve: Vec<bool> = vec![true; (n + 1) as usize];

        sieve[0] = false;
        sieve[1] = false;

        let n_sqrt: i32 = (n as f64).sqrt() as i32;

        fn filter_prime_numbers(sieve: &mut Vec<bool>, n_sqrt: i32) -> () {
            for outer_num in 2..=n_sqrt {
                for inner_num in 2..=outer_num {
                    sieve[(outer_num * inner_num) as usize] = false;
                }
            }
        }

        filter_prime_numbers(&mut sieve, n_sqrt);

        let prime_factors: Vec<usize> = sieve
            .into_iter()
            .enumerate()
            .filter(|(_, is_prime)| *is_prime)
            .map(|(idx, _)| idx)
            .collect();

        let mut n_factorized: usize = n as usize;
        let mut steps: usize = 0;

        while n_factorized > 1 {
            for &prime_factor in &prime_factors {
                if n_factorized % prime_factor == 0 {
                    n_factorized /= prime_factor;
                    steps += prime_factor;
                }
            }
        }

        match i32::try_from(steps) {
            Ok(steps) => return steps,
            Err(_) => return -1,
        }
    }
}

pub fn run_tests() {
    assert_eq!(0, Solution::min_steps(1));
    assert_eq!(3, Solution::min_steps(3));
    assert_eq!(9, Solution::min_steps(24));
    assert_eq!(35, Solution::min_steps(124));
}
