// This stub file contains items which aren't used yet; feel free to remove this module attribute
// to enable stricter warnings.
// #![allow(unused)]

use std::collections::HashMap;

pub fn can_construct_note(magazine: &[&str], note: &[&str]) -> bool {
    let mut magazine_counter: HashMap<&str, u32> = HashMap::new();
    let mut note_counter: HashMap<&str, u32> = HashMap::new();

    for word in magazine.iter() {
        *magazine_counter.entry(word).or_insert(0) += 1;
    }

    for word in note.iter() {
        *note_counter.entry(word).or_insert(0) += 1;
    }

    note_counter
        .iter()
        .all(&|(word, cut)| magazine_counter.get(word).unwrap_or(&0) >= cut)
}
