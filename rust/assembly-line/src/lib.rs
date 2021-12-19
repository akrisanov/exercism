// This stub file contains items which aren't used yet; feel free to remove this module attribute
// to enable stricter warnings.
// #![allow(unused)]

const CARS_PER_HOUR: f64 = 221.0;
const MIN_IN_HOUR: u32 = 60;

pub fn production_rate_per_hour(speed: u8) -> f64 {
    CARS_PER_HOUR * speed as f64 * production_success_rate(speed)
}

pub fn working_items_per_minute(speed: u8) -> u32 {
    production_rate_per_hour(speed) as u32 / MIN_IN_HOUR
}

fn production_success_rate(speed: u8) -> f64 {
    match speed {
        0 => 0.0,
        1..=4 => 1.0,
        5..=8 => 0.9,
        9..=10 => 0.77,
        _ => panic!("The assembly line's speed can range from 0 (off) to 10 (maximum)."),
    }
}
