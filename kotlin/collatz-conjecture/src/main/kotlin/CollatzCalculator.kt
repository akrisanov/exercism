object CollatzCalculator {
    fun isEven(number: Int) = number % 2 == 0

    fun computeStepCount(start: Int): Int {
        require(start > 0)

        var x = start
        var steps = 0

        while (x > 1) {
            x = if (isEven(x)) x / 2 else 3 * x + 1
            steps++
        }

        return steps
    }
}
