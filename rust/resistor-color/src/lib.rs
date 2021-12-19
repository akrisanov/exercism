use enum_iterator::IntoEnumIterator;
use int_enum::IntEnum;
use std::cmp::Ordering;

#[repr(usize)]
#[derive(Debug, Clone, Eq, Copy, IntEnum, IntoEnumIterator)]
pub enum ResistorColor {
    Black = 0,
    Blue = 6,
    Brown = 1,
    Green = 5,
    Grey = 8,
    Orange = 3,
    Red = 2,
    Violet = 7,
    White = 9,
    Yellow = 4,
}

impl Ord for ResistorColor {
    fn cmp(&self, other: &Self) -> Ordering {
        self.int_value().cmp(&other.int_value())
    }
}

impl PartialOrd for ResistorColor {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl PartialEq for ResistorColor {
    fn eq(&self, other: &Self) -> bool {
        self.int_value() == other.int_value()
    }
}

pub fn color_to_value(_color: ResistorColor) -> usize {
    _color.int_value()
}

pub fn value_to_color_string(value: usize) -> String {
    if let Ok(color) = ResistorColor::from_int(value) {
        format!("{:?}", color)
    } else {
        "value out of range".to_string()
    }
}

pub fn colors() -> Vec<ResistorColor> {
    let mut r_colors = ResistorColor::into_enum_iter()
        .map(|color| color)
        .collect::<Vec<_>>();

    r_colors.sort();
    r_colors
}
