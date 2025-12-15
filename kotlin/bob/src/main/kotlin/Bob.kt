object Bob {
    fun isQuestion(s: String): Boolean =
        s.endsWith('?')

    fun isYelling(s: String): Boolean =
        s.any { it in 'A'..'Z' } &&
        s.none { it in 'a'..'z' }

    fun hey(input: String): String {
        val s = input.trim()
        if (s.isEmpty()) return "Fine. Be that way!"

        val yelling = isYelling(s)
        val question = isQuestion(s)

        return when {
            yelling && question -> "Calm down, I know what I'm doing!"
            yelling -> "Whoa, chill out!"
            question -> "Sure."
            else -> "Whatever."
        }
    }
}
