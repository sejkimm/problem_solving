struct Solution;

impl Solution {
    pub fn are_sentences_similar(sentence1: String, sentence2: String) -> bool {
        let sentence1: Vec<&str> = sentence1.split(' ').collect();
        let sentence2: Vec<&str> = sentence2.split(' ').collect();

        let (shorter, longer) = if sentence1.len() < sentence2.len() {
            (sentence1, sentence2)
        } else {
            (sentence2, sentence1)
        };

        if shorter.len() == 1 {
            return shorter[0] == longer[0] || shorter[0] == longer[longer.len() - 1];
        }

        let mut from_start_samewords: usize = 0;
        let mut from_end_samewords: usize = 0;

        while from_start_samewords < shorter.len()
            && shorter[from_start_samewords] == longer[from_start_samewords]
        {
            from_start_samewords += 1;
        }

        while from_end_samewords < shorter.len()
            && shorter[shorter.len() - from_end_samewords - 1]
                == longer[longer.len() - from_end_samewords - 1]
        {
            from_end_samewords += 1;
        }

        return from_start_samewords + from_end_samewords >= shorter.len();
    }
}

pub fn run_tests() {
    assert_eq!(
        true,
        Solution::are_sentences_similar(String::from("My name is Haley"), String::from("My Haley"))
    );
    assert_eq!(
        false,
        Solution::are_sentences_similar(String::from("of"), String::from("A lot of words"))
    );
    assert_eq!(
        true,
        Solution::are_sentences_similar(String::from("Eating right now"), String::from("Eating"))
    );
    assert_eq!(
        false,
        Solution::are_sentences_similar(
            String::from("Eating now"),
            String::from("Eating tomorrow")
        )
    );
    assert_eq!(
        false,
        Solution::are_sentences_similar(
            String::from("eTUny i b R UFKQJ EZx JBJ Q xXz"),
            String::from("eTUny i R EZx JBJ xXz")
        )
    );
}
