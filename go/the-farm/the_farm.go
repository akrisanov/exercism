package thefarm

import "fmt"

func DivideFood(fc FodderCalculator, cows int) (float64, error) {
	amount, err := fc.FodderAmount(cows)
	if err != nil {
		return 0, err
	}
	factor, err := fc.FatteningFactor()
	if err != nil {
		return 0, err
	}
	if factor == 0 {
		return 0, fmt.Errorf("fattening factor is zero")
	}
	return (amount * factor) / float64(cows), nil
}

func ValidateInputAndDivideFood(fc FodderCalculator, cows int) (float64, error) {
	if cows <= 0 {
		return 0, fmt.Errorf("invalid number of cows")
	}
	return DivideFood(fc, cows)
}

type InvalidCowsError struct {
	cows    int
	message string
}

func (e *InvalidCowsError) Error() string {
	return fmt.Sprintf("%d cows are invalid: %s", e.cows, e.message)
}

func ValidateNumberOfCows(cows int) error {
	if cows < 0 {
		return &InvalidCowsError{cows, "there are no negative cows"}
	}
	if cows == 0 {
		return &InvalidCowsError{cows, "no cows don't need food"}
	}
	return nil
}
