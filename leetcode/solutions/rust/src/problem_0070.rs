impl Solution {
    pub fn climb_stairs(n: i32) -> i32 {
        let mut possible_steps: Vec<i32> = vec![0; (n + 1) as usize];

        possible_steps[0] = 1;
        possible_steps[1] = 1;

        for current_step in 2..=n {
            let cs: usize = current_step as usize;
            possible_steps[cs] = possible_steps[cs - 1] + possible_steps[cs - 2]
        }

        return possible_steps[n as usize];
    }
}
