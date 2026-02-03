package blackjack

// ParseCard returns the integer value of a card following blackjack ruleset.
func ParseCard(card string) int {
	switch card {
	case "ace":
		return 11
	case "two":
		return 2
	case "three":
		return 3
	case "four":
		return 4
	case "five":
		return 5
	case "six":
		return 6
	case "seven":
		return 7
	case "eight":
		return 8
	case "nine":
		return 9
	case "ten", "jack", "queen", "king":
		return 10
	default:
		return 0
	}
}

// FirstTurn returns the decision for the first turn, given two cards of the
// player and one card of the dealer.
func FirstTurn(card1, card2, dealerCard string) string {
	cardsSum := ParseCard(card1) + ParseCard(card2)
	blackJack := cardsSum == 21

	dealerHasAce := dealerCard == "ace"
	dealerHasTenValue := ParseCard(dealerCard) == 10

	switch {
	case card1 == "ace" && card2 == "ace":
		return "P"
	case blackJack && !(dealerHasAce || dealerHasTenValue):
		return "W"
	case blackJack:
		return "S"
	case cardsSum >= 17 && cardsSum <= 20:
		return "S"
	case cardsSum >= 12 && cardsSum <= 16 && ParseCard(dealerCard) < 7:
		return "S"
	default:
		return "H"
	}
}
