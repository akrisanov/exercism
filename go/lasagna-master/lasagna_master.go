package lasagna

func PreparationTime(layers []string, prepTimePerLayer int) int {
	if prepTimePerLayer == 0 {
		prepTimePerLayer = 2
	}
	return len(layers) * prepTimePerLayer
}

func Quantities(layers []string) (noodles int, sauce float64) {
	const noodlesPerLayer = 50
	const saucePerLayer = 0.2

	for _, l := range layers {
		switch l {
		case "noodles":
			noodles += noodlesPerLayer
		case "sauce":
			sauce += saucePerLayer
		}
	}

	return
}

func AddSecretIngredient(friendsList, myList []string) {
	myList[len(myList)-1] = friendsList[len(friendsList)-1]
}

func ScaleRecipe(quantities []float64, portions int) []float64 {
	const basePortions = 2
	factor := float64(portions) / basePortions
	scaled := make([]float64, len(quantities))

	for i, q := range quantities {
		scaled[i] = q * factor
	}
	return scaled
}
