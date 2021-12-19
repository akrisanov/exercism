use enum_iterator::IntoEnumIterator;
use std::fmt;

#[repr(usize)]
#[derive(Debug, Clone, PartialEq, Copy, IntoEnumIterator)]
pub enum ResistorColor {
    Black = 0,
    Brown = 1,
    Red = 2,
    Orange = 3,
    Yellow = 4,
    Green = 5,
    Blue = 6,
    Violet = 7,
    Grey = 8,
    White = 9,
}

impl fmt::Display for ResistorColor {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{:?}", self)
    }
}

pub fn color_to_value(_color: ResistorColor) -> usize {
    match ResistorColor::into_enum_iter().position(|val| val == _color) {
        Some(val) => val,
        // only for keeping the return type defined by task authors
        _ => panic!("unsupported color"),
    }
}

pub fn value_to_color_string(value: usize) -> String {
    match ResistorColor::into_enum_iter()
        .enumerate()
        .find(|&color| color.0 == value)
    {
        Some(color) => color.1.to_string(),
        _ => "value out of range".to_string(),
    }
}

pub fn colors() -> Vec<ResistorColor> {
    ResistorColor::into_enum_iter().collect::<Vec<_>>()
}
