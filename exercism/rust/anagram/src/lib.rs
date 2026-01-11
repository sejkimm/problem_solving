use std::collections::{HashSet, HashMap};
use unicode_segmentation::UnicodeSegmentation;

pub fn anagrams_for<'a>(word: &str, possible_anagrams: &[&'a str]) -> HashSet<&'a str> {
    let target_word = word.to_lowercase();

    let mut target_wc: HashMap<String, usize> = HashMap::new();
    for g in target_word.graphemes(true) {
        *target_wc.entry(g.to_string()).or_insert(0) += 1;
    }

    let mut results: HashSet<&'a str> = HashSet::new();

    for &candidate in possible_anagrams {
        let cand_lc = candidate.to_lowercase();
        if cand_lc == target_word {
            continue;
        }

        let mut candidate_wc: HashMap<String, usize> = HashMap::new();
        for g in cand_lc.graphemes(true) {
            *candidate_wc.entry(g.to_string()).or_insert(0) += 1;
        }

        if candidate_wc == target_wc {
            results.insert(candidate);
        }
    }

    results
}
