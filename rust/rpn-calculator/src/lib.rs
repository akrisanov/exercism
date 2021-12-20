#[derive(Debug)]
pub enum CalculatorInput {
    Add,
    Subtract,
    Multiply,
    Divide,
    Value(i32),
}

pub fn evaluate(inputs: &[CalculatorInput]) -> Option<i32> {
    let mut evaluation: Vec<i32> = Vec::new();

    for input in inputs {
        match input {
            CalculatorInput::Value(number) => evaluation.push(*number),
            _ => {
                let snd = evaluation.pop()?;
                let fst = evaluation.pop()?;

                match input {
                    CalculatorInput::Add => evaluation.push(fst + snd),
                    CalculatorInput::Subtract => evaluation.push(fst - snd),
                    CalculatorInput::Multiply => evaluation.push(fst * snd),
                    CalculatorInput::Divide => evaluation.push(fst / snd),
                    _ => return None,
                }
            }
        }
    }

    match evaluation.len() {
        1 => evaluation.pop(),
        _ => None,
    }
}
