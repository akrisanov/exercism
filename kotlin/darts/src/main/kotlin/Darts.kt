import kotlin.math.hypot

object Darts {
    private const val INNER_RING = 1.0
    private const val MIDDLE_RING = 5.0
    private const val OUTER_RING = 10.0

    fun score(x: Number, y: Number): Int {
        val toss = hypot(x.toDouble(), y.toDouble())

        return when {
            toss <= INNER_RING -> 10
            toss <= MIDDLE_RING -> 5
            toss <= OUTER_RING -> 1
            else -> 0
        }
    }
}
